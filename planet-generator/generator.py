from __future__ import division

import random

from noise import pnoise2
from PIL import Image

from planets import PLANET_TYPES
from utils import spherize


def generate(planet_type, filename):
    height = 1024
    width = 1024

    planet_values = PLANET_TYPES[planet_type]
    octaves = random.randrange(planet_values['octaves_min'], planet_values['octaves_max'])
    freq = random.uniform(planet_values['frequency_min'], planet_values['frequency_max']) * octaves
    seed = random.randrange(1, 256)

    # Pick a colour option to use
    colour_set = random.choice(planet_values['colour_sets'])

    # Generate supersampled noise
    noise_array = []
    for y in range(height):
        for x in range(width):
            # Value ranges between roughly 60 and 196 (for gas anyway)
            noise_value = int(pnoise2(x / freq, y / freq, octaves, planet_values['persistence'], planet_values['lacunarity'], width, height, seed) * 127.0 + 128.0)
            # Colouring
            range_found = False
            for colour_range in colour_set:
                range_start = colour_range[0]
                range_end = colour_range[1]

                if noise_value >= range_start and noise_value <= range_end:
                    red_start = colour_range[2]
                    red_end = colour_range[3]
                    green_start = colour_range[4]
                    green_end = colour_range[5]
                    blue_start = colour_range[6]
                    blue_end = colour_range[7]

                    noise_percent = (noise_value - range_start) / (range_end - range_start)

                    red_value = int(red_start + (noise_percent * (red_end - red_start)))
                    green_value = int(green_start + (noise_percent * (green_end - green_start)))
                    blue_value = int(blue_start + (noise_percent * (blue_end - blue_start)))

                    noise_array.append((red_value, green_value, blue_value, 255))
                    range_found = True
                    break

            # If there's no matching range put transparency instead
            if not range_found:
                noise_array.append((255, 255, 255, 0))

    # Generate image from noise
    image = Image.new('RGBA', (width, height))
    image.putdata(noise_array)

    # Spherize
    image = spherize(image)

    # Apply circle mask
    temp = Image.new('RGBA', (width, height))
    mask = Image.open('mask.png')
    temp.paste(image, mask=mask)
    image = temp

    # Lighten/Darken to create spherical appearance

    # Add atmosphere if applicable

    # Downsample - resize it with filter=Image.ANTIALIAS
    image = image.resize((int(width / 2), int(width / 2)), Image.ANTIALIAS)

    # Save image
    image.save(filename)


if __name__ == "__main__":
    for x in range(1):
        generate('temperate', "test%s.png" % x)
