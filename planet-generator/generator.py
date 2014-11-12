import random

from noise import pnoise2
from PIL import Image

"""
octaves: Number of passes of the algorithm
frequency:
persistence: Amplitude of each pass of the algorithm relative to the last
lacunarity: Frequency of each pass of algorithm relatve to the last

colour_sets: A list of tuples defining the range cutofss for colours in the planet
             (cutoff_start, cutoff_end, red_min, red_max, green_min, green_max, blue_min, blue_max)
             The lowest possible cutoff will be used if there are several in the list
"""

PLANET_TYPES = {
    'temperate': {

    },
    'gas': {
        'octaves_min': 8,
        'octaves_max': 16,
        'frequency_min': 8.0,
        'frequency_max': 32.0,
        'persistence': 0.5,
        'lacunarity': 2.0,
        'colour_sets': [
            [(0, 255, 0, 128, 0, 255, 0, 128)],  # Greenish
            [(0, 255, 0, 255, 0, 128, 0, 128)],  # Redish
            [(0, 255, 0, 128, 0, 128, 0, 255)],  # Blueish
        ]
    },
    'ice': {

    },
    'lava': {

    },
    'dust': {

    }
}


def generate(planet_type, filename):
    height = 1024
    width = 1024

    planet_values = PLANET_TYPES[planet_type]
    octaves = random.randrange(planet_values['octaves_min'], planet_values['octaves_max'])
    freq = random.uniform(planet_values['frequency_min'], planet_values['frequency_max']) * octaves
    seed = random.randrange(1, 256)

    # Pick a colour option to use
    colour_set = random.choice(planet_values['colour_sets'])

    print colour_set

    # Generate supersampled noise
    noise_array = []
    for y in range(height):
        for x in range(width):
            # Value ranges between roughly 60 and 196 (for gas anyway)
            noise_value = int(pnoise2(x / freq, y / freq, octaves, planet_values['persistence'], planet_values['lacunarity'], width, height, seed) * 127.0 + 128.0)
            # Colouring - Temp
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

                    noise_range = range_end - range_start
                    red_range = red_end - red_start
                    green_range = green_end - green_start
                    blue_range = blue_end - blue_start

                    noise_array.append((noise_value / 2, noise_value, noise_value / 2))
                    break

    # Generate image from noise
    image = Image.new('RGBA', (height, width))
    image.putdata(noise_array)

    # Apply circle mask
    temp = Image.new('RGB', (height, width))
    mask = Image.open('mask.png')
    temp.paste(image, mask=mask)
    image = temp

    # Lighten/Darken to create spherical appearance

    # Downsample - resize it with filter=Image.ANTIALIAS
    image = image.resize((512, 512), Image.ANTIALIAS)

    # Save image
    image.save(filename)


if __name__ == "__main__":
    for x in range(1):
        generate('gas', "test%s.png" % x)
