from noise import snoise2
from PIL import Image

PLANET_TYPES = [
    'temperate',
    'gas',
    'ice',
    'lava',
    'dust',
]


def generate(planet_type, size):
    image = Image.new('RGB', (size, size))

    octaves = 1
    freq = 16.0 * octaves

    for y in range(size):
        for x in range(size):

            print("%s" % int(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0))

            # f.write("%s\n" % int(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0))