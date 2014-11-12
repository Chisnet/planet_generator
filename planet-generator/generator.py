import random

from noise import pnoise2
from PIL import Image

PLANET_TYPES = {
    'temperate': {

    },
    'gas': {
        'octaves_min': 8,
        'octaves_max': 16,
        'frequency_min': 8.0,
        'frequency_max': 32.0,
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
    seed = random.randrange(1, 512)

    # Generate supersampled noise
    noise_array = []
    for y in range(height):
        for x in range(width):
            # Value ranges between roughly 60 and 196 (for gas anyway)
            noise_value = int(pnoise2(x / freq, y / freq, octaves, repeatx=width, repeaty=height, base=seed) * 127.0 + 128.0)
            # Colouring
            noise_array.append((noise_value / 2, noise_value, noise_value / 2))

    # Generate image from noise
    image = Image.new('RGB', (height, width))
    image.putdata(noise_array)

    # Apply circle mask

    # Downsample - resize it with filter=Image.ANTIALIAS
    image = image.resize((512, 512), Image.ANTIALIAS)

    # Save image
    image.save(filename)


if __name__ == "__main__":
    for x in range(1):
        generate('gas', "test%s.png" % x)
