from __future__ import division

import random

from noise import pnoise2
from PIL import Image

from planets import PLANET_TYPES
from utils import spherize


def generate(planet_type, filename):
    height = 1024
    width = 1024
    planet_height = 1000
    planet_width = 1000

    # Generate seed for noise generation
    seed = random.randrange(1, 256)

    # Load universal planet type values
    planet_values = PLANET_TYPES[planet_type]
    octaves = random.randrange(planet_values['octaves_min'], planet_values['octaves_max'])
    freq = random.uniform(planet_values['frequency_min'], planet_values['frequency_max']) * octaves

    # Pick a render set to use
    render_set = random.choice(planet_values['render_sets'])

    # Initialise image
    image = Image.new('RGBA', (planet_width, planet_height))

    # Generate noise
    print "Generating noise..."
    noise = generate_noise(freq, octaves, planet_values['persistence'], planet_values['lacunarity'], planet_width, planet_height, seed)

    # Loop over the layers
    for layer_name in render_set['layer_order']:
        layer = render_set['layers'][layer_name]
        print "Generating %s layer..." % layer_name
        if layer['type'] == 'contour':
            generate_contours(image, noise, layer['ranges'], layer_name)
        elif layer['type'] == 'rivers':
            generate_rivers(image, layer['colour'])

    # Spherize
    print "Spherizing image..."
    image = spherize(image)

    # Pad image to full size for masking
    black = Image.new('RGB', (width, height))
    black.paste(image, (12, 12))
    image = black

    # Apply shadow mask
    print "Applying masks..."
    temp = Image.new('RGB', (width, height))
    mask = Image.open('shadow-mask.png')
    temp.paste(image, mask=mask)

    # Apply transparency mask
    temp2 = Image.new('RGBA', (width, height))
    mask2 = Image.open('transparency-mask.png')
    temp2.paste(temp, mask=mask2)
    image = temp2

    # Add atmosphere if applicable

    # Downsample - resize it with filter=Image.ANTIALIAS
    print "Downsampling..."
    image = image.resize((int(width / 2), int(width / 2)), Image.ANTIALIAS)

    # Save image
    print "Saving..."
    image.save(filename)


def generate_noise(freq, octaves, persistence, lacunarity, width, height, seed):
    noise_array = []
    for y in range(height):
        for x in range(width):
            # Value ranges between roughly 60 and 196
            noise_value = int(pnoise2(x / freq, y / freq, octaves, persistence, lacunarity, width, height, seed) * 127.0 + 128.0)
            noise_array.append(noise_value)

    return noise_array


def generate_contours(image, noise, ranges, layer_name):
    # Takes random greyscale noise and colours it based on colour ranges
    width, height = image.size

    noise_array = []
    for noise_value in noise:
        range_found = False
        for colour_range in ranges:
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
            noise_array.append((0, 0, 0, 0))

    temp_image = Image.new('RGBA', (width, height))
    temp_image.putdata(noise_array)

    image.paste(temp_image, temp_image)


def generate_rivers(image, colour):
    pass


if __name__ == "__main__":
    for x in range(1):
        generate('temperate', "../test%s.png" % x)
