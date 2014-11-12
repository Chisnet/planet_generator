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
        'octaves_min': 8,
        'octaves_max': 16,
        'frequency_min': 24.0,
        'frequency_max': 36.0,
        'persistence': 0.5,
        'lacunarity': 2.0,
        'colour_sets': [
            [
                (0,   100, 0,   0,   0,   0,   0,   70 ),
                (100, 130, 0,   0,   0,   0,   80,  110),
                (130, 131, 90 , 130, 90,  130, 0,   0  ),
                (131, 255, 0  , 30 , 60,  110, 0,   30 ),
            ],
        ]
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

    print octaves
    print freq

    # Pick a colour option to use
    colour_set = random.choice(planet_values['colour_sets'])

    # Generate supersampled noise
    noise_array = []
    for y in range(height):
        for x in range(width):
            # Value ranges between roughly 60 and 196 (for gas anyway)
            noise_value = int(pnoise2(x / freq, y / freq, octaves, planet_values['persistence'], planet_values['lacunarity'], width, height, seed) * 127.0 + 128.0)
            # Colouring
            for colour_range in colour_set:
                range_start = float(colour_range[0])
                range_end = float(colour_range[1])

                if noise_value >= range_start and noise_value <= range_end:
                    red_start = float(colour_range[2])
                    red_end = float(colour_range[3])
                    green_start = float(colour_range[4])
                    green_end = float(colour_range[5])
                    blue_start = float(colour_range[6])
                    blue_end = float(colour_range[7])

                    noise_percent = (noise_value - range_start) / (range_end - range_start)

                    red_value = int(red_start + (noise_percent * (red_end - red_start)))
                    green_value = int(green_start + (noise_percent * (green_end - green_start)))
                    blue_value = int(blue_start + (noise_percent * (blue_end - blue_start)))

                    noise_array.append((red_value, green_value, blue_value))
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
        generate('temperate', "test%s.png" % x)
