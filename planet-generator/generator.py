from noise import snoise2
from PIL import Image

PLANET_TYPES = {
    'temperate': {

    },
    'gas': {
        'octaves': 16
    },
    'ice': {

    },
    'lava': {

    },
    'dust': {

    }
}


def generate(planet_type, size):
    image = Image.new('RGB', (size, size))

    octaves = 16
    freq = 16.0 * octaves

    image_array = []

    for y in range(size):
        for x in range(size):
            noise_value = int(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0)
            image_array.append((noise_value, noise_value, noise_value))

    image.putdata(image_array)

    image.save('test.jpg')
