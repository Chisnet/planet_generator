from __future__ import division

import math
import numpy

from PIL import Image


def spherize(image):
    # Spherize based on: https://gist.github.com/kspi/2820038
    a1 = numpy.array(image, dtype=numpy.double)
    height, width, channels = a1.shape
    a2 = numpy.zeros(a1.shape, dtype=numpy.double)

    for y2 in range(height):
        for x2 in range(width):
            x1, y1 = map_coords(x2 / width * 2 - 1, y2 / height * 2 - 1)
            a2[y2, x2] = sample(a1, (y1 * 0.5 + 0.5) * height, (x1 * 0.5 + 0.5) * width)

    output_image = Image.fromarray(numpy.clip(a2, 0, 0xff).astype(numpy.uint8))

    return output_image


def map_coords(x2, y2):
    r2 = math.sqrt(math.pow(x2, 2) + math.pow(y2, 2))

    if r2 > 1:
        x1 = x2
        y1 = y2
    else:
        theta1 = math.atan2(y2, x2)
        r1 = math.asin(r2) / (math.pi / 2)
        x1 = r1 * math.cos(theta1)
        y1 = r1 * math.sin(theta1)

    return (x1, y1)


def black_bounds(f, x, y):
    if 0 <= x < f.shape[0] and 0 <= y < f.shape[1]:
        return f[x, y]
    else:
        return 0


def sample(f, x, y):
    x0 = int(x)
    y0 = int(y)
    x1 = x0 + 1
    y1 = y0 + 1
    fy0 = black_bounds(f, x0, y0) * (x1 - x) + black_bounds(f, x1, y0) * (x - x0)
    fy1 = black_bounds(f, x0, y1) * (x1 - x) + black_bounds(f, x1, y1) * (x - x0)
    return fy0 * (y1 - y) + fy1 * (y - y0)
