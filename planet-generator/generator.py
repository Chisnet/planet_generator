import noise

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
