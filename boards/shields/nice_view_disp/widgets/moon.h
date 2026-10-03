/*
 *
 * Copyright (c) 2026 Théo Sépulcre
 * SPDX-License-Identifier: MIT
 *
 */

#pragma once

#include <stdint.h>

#define MOON_IMG_W 140
#define MOON_IMG_H 68
#define MOON_IMG_STRIDE ((MOON_IMG_W + 7) / 8)
/* 2-entry palette (2 x 4 bytes) followed by the 1-bit pixel rows */
#define MOON_IMG_DATA_SIZE (8 + MOON_IMG_STRIDE * MOON_IMG_H)

/*
 * Render the moon at `step` out of `steps` phases (0 = new moon, steps / 2 = full)
 * into `buf` as an LV_IMG_CF_INDEXED_1BIT image, rotated for the nice!view.
 */
void moon_render(uint8_t buf[MOON_IMG_DATA_SIZE], uint32_t step, uint32_t steps);
