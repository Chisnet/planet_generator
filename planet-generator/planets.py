"""
octaves: Number of passes of the algorithm
frequency: Initial frequency of the noise
persistence: Amplitude of each pass of the algorithm relative to the last
lacunarity: Frequency of each pass of algorithm relative to the last

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
                (0, 100, 0, 0, 0, 0, 0, 70),         # Deep sea
                (100, 130, 0, 0, 0, 0, 80, 110),     # Shallow sea
                (130, 131, 90, 130, 90, 130, 0, 0),  # Sandy shore
                (131, 255, 0, 30, 60, 110, 0, 30),   # Land
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
