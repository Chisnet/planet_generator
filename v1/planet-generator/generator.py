import getopt
import random
import sys
from pathlib import Path

from noise import pnoise2
from PIL import Image

from planets import PLANET_TYPES
from utils import spherize

MAX_ITERATIONS = 50

script_dir = Path(__file__).absolute().parent


def main(argv):
    planet_type = None
    planet_count = 1

    # Read options
    try:
        opts, args = getopt.getopt(argv, "t:n:", ["type", "number"])
    except getopt.GetoptError:
        print("Error! Invalid or missing options provided.")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-t", "--type"):
            planet_type = arg
        if opt in ("-n", "--number"):
            planet_count = arg

    if not planet_type:
        print("Error! Planet type not provided.")
        sys.exit()
    try:
        planet_count = int(planet_count)
    except TypeError:
        print("Error! Invalid planet count.")
        sys.exit()

    # Generate!
    for planet_num in range(planet_count):
        print(f"Generating celestial body {planet_num+1}...")
        generate(planet_type, "../test%s.png" % (planet_num + 1))


def generate(planet_type, filename):
    height = 1080
    width = 1080
    planet_height = 1000
    planet_width = 1000

    # Generate seed for noise generation
    seed = random.randrange(1, 256)

    # Load universal planet type values
    planet_values = PLANET_TYPES[planet_type]
    octaves = random.randrange(planet_values['octaves_min'], planet_values['octaves_max'])
    freq = random.uniform(planet_values['frequency_min'], planet_values['frequency_max']) * octaves
    apply_shadow = planet_values.get('shadow', True)

    # Pick a render set to use
    render_set = random.choice(planet_values['render_sets'])

    # Initialise image
    image = Image.new('RGBA', (planet_width, planet_height))

    # Generate noise
    print("Generating noise...")
    noise = generate_noise(freq, octaves, planet_values['persistence'], planet_values['lacunarity'], planet_width, planet_height, seed)

    # Loop over the layers
    for layer_name in render_set['layer_order']:
        layer = render_set['layers'][layer_name]
        print(f"Generating {layer_name} layer...")
        if layer['type'] == 'contour':
            generate_contours(image, noise, layer['ranges'])
        elif layer['type'] == 'river':
            generate_rivers(image, noise, layer['paths'])

    # Spherize
    print("Spherizing image...")
    image = spherize(image)

    # Pad image to full size for masking
    black = Image.new('RGB', (width, height))
    black.paste(image, (40, 40))
    image = black

    # Apply shadow mask
    print("Applying masks...")
    if apply_shadow:
        temp = Image.new('RGB', (width, height))
        mask = Image.open(f'{script_dir}/shadow-mask.png')
        temp.paste(image, mask=mask)
    else:
        temp = image

    # Apply transparency mask
    temp2 = Image.new('RGBA', (width, height))
    mask2 = Image.open(f'{script_dir}/transparency-mask.png')
    temp2.paste(temp, mask=mask2)
    image = temp2

    # Add atmosphere if applicable
    atmo = Image.open(f'{script_dir}/atmosphere.png')
    atmo_mask = Image.new('L', (width, height))
    atmo_mask.paste(atmo)
    image.paste(atmo, mask=atmo_mask)

    # Downsample - resize it with filter=Image.ANTIALIAS
    print("Downsampling...")
    image = image.resize((int(width / 2), int(width / 2)))

    # Save image
    print("Saving...")
    image.save(f'{script_dir}/{filename}')


def generate_noise(freq, octaves, persistence, lacunarity, width, height, seed):
    noise_array = []
    for y in range(height):
        for x in range(width):
            # Value ranges between roughly 60 and 196
            noise_value = int(pnoise2(x / freq, y / freq, octaves, persistence, lacunarity, width, height, seed) * 127.0 + 128.0)
            noise_array.append(noise_value)

    return noise_array


def generate_contours(image, noise, ranges):
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


def generate_rivers(image, noise, paths):
    # Takes random greyscale noise and draws downhill paths
    width, height = image.size

    path_count = random.randrange(paths['count_min'], paths['count_max'])

    iterations = 0

    # while path_count > 0 and iterations <= MAX_ITERATIONS:
    #     successful_path = False

    #     # Find a suitable ending point for the river
    #     start_pos = random.randrange(0, (width * height) - 1)
    #     while (noise[start_pos] < paths['end_min'] and noise[start_pos] > paths['end_max']) and (start_pos < (width * height) -1):
    #         start_pos += 1

    #     if (noise[start_pos] > paths['end_min'] and noise[start_pos] < paths['end_max']):
    #         river_steps = 0

    #     if successful_path:
    #         path_count -= 1
    #     iterations += 1

if __name__ == "__main__":
    main(sys.argv[1:])
