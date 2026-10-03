/*
 *
 * Copyright (c) 2026 Théo Sépulcre
 * SPDX-License-Identifier: MIT
 *
 */

#include <stdbool.h>
#include <string.h>

#include "moon.h"
#include "moon_bitmap.h"

/* Disk geometry in the base bitmap, must match tools/gen_moon.py */
#define MOON_R 31.0f
#define MOON_CX 34.0f
#define MOON_CY 48.0f

/* Sunlight comes from 20 degrees below horizontal, as seen from mid-northern latitudes */
#define TILT_COS 0.93969262f
#define TILT_SIN 0.34202014f

#define PI_F 3.14159265f

static const uint8_t bayer4[4][4] = {
    {0, 8, 2, 10}, {12, 4, 14, 6}, {3, 11, 1, 9}, {15, 7, 13, 5}};

/* Small float helpers, avoiding a libm dependency */
static float moon_sqrt(float x) {
    if (x <= 0.0f) {
        return 0.0f;
    }
    float r = x > 1.0f ? x : 1.0f;
    for (int i = 0; i < 12; i++) {
        r = 0.5f * (r + x / r);
    }
    return r;
}

static float moon_cos(float a) {
    while (a > PI_F) {
        a -= 2.0f * PI_F;
    }
    while (a < -PI_F) {
        a += 2.0f * PI_F;
    }
    float a2 = a * a, term = 1.0f, sum = 1.0f;
    for (int n = 1; n <= 7; n++) {
        term *= -a2 / ((2 * n - 1) * (2 * n));
        sum += term;
    }
    return sum;
}

static bool base_pixel(int px, int py) {
    return moon_base[py * MOON_BASE_STRIDE + px / 8] & (0x80 >> (px % 8));
}

void moon_render(uint8_t buf[MOON_IMG_DATA_SIZE], uint32_t step, uint32_t steps) {
    /*
     * Fixed palette: the night sky stays dark even with the inverted widget colors.
     * The nice!view shows LVGL white as a dark pixel, so index 0 (sky) is white
     * and index 1 (lit) is black, matching the LVGL_BACKGROUND of the status strip.
     */
    static const uint8_t palette[8] = {0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0xff};
    memcpy(buf, palette, sizeof(palette));
    uint8_t *data = buf + sizeof(palette);
    memset(data, 0, MOON_IMG_STRIDE * MOON_IMG_H);

    step %= steps;
    bool waxing = 2 * step < steps;
    /* Terminator half-width: 1 at new moon (all dark), -1 at full moon (all lit) */
    float c = moon_cos(2.0f * PI_F * step / steps);
    /* Direction of the sunlight: lower right while waxing, lower left while waning */
    float lx = waxing ? TILT_COS : -TILT_COS, ly = -TILT_SIN;

    for (int py = 0; py < MOON_BASE_H; py++) {
        for (int px = 0; px < MOON_BASE_W; px++) {
            bool on = base_pixel(px, py);
            float x = (px + 0.5f - MOON_CX) / MOON_R, y = -(py + 0.5f - MOON_CY) / MOON_R;
            float rr = x * x + y * y;

            if (rr <= 1.0f) {
                float u = x * lx + y * ly, w = -x * ly + y * lx;
                float t = c * moon_sqrt(1.0f - w * w);
                if (u <= t) {
                    /* Night side: only a faint earthshine rim */
                    on = rr > 0.93f && (px + py) % 2 == 0;
                } else if (u - t < 0.09f) {
                    /* Dim the lit side along the terminator */
                    on = on && bayer4[py % 4][px % 4] <= 9;
                }
            }
            if (!on) {
                continue;
            }

            /* The screen is mounted sideways: map viewing coords to image coords */
#ifdef CONFIG_NICE_VIEW_DISP_ROTATE_180
            int xs = py, ys = MOON_BASE_W - 1 - px;
#else
            int xs = MOON_BASE_H - 1 - py, ys = px;
#endif
            data[ys * MOON_IMG_STRIDE + xs / 8] |= 0x80 >> (xs % 8);
        }
    }
}
