"""
octaves: Number of passes of the algorithm
frequency: Initial frequency of the noise
persistence: Amplitude of each pass of the algorithm relative to the last
lacunarity: Frequency of each pass of algorithm relative to the last

render_sets: A list of render variables defining the layers of the planet render, the order of those
             layers, and the settings for each type of layer (contour or rivers)
"""

PLANET_TYPES = {
    'temperate': {
        'octaves_min': 8,
        'octaves_max': 16,
        'frequency_min': 24.0,
        'frequency_max': 36.0,
        'persistence': 0.5,
        'lacunarity': 2.0,
        'render_sets': [
            {
                'name': 'earthlike',
                'layers': {
                    'sea': {
                        'type': 'contour',
                        'ranges': [
                            (0, 100, 0, 0, 0, 0, 0, 70),      # Deep sea
                            (100, 130, 0, 0, 0, 0, 80, 110),  # Shallow sea
                        ]
                    },
                    'land': {
                        'type': 'contour',
                        'ranges': [
                            (130, 131, 90, 110, 90, 110, 0, 0),  # Sandy shore
                            (131, 255, 0, 30, 60, 110, 0, 30),   # Land
                        ]
                    }
                },
                'layer_order': ['land', 'sea']
            }
        ]
    },
    'gas': {
        'octaves_min': 8,
        'octaves_max': 16,
        'frequency_min': 8.0,
        'frequency_max': 32.0,
        'persistence': 0.5,
        'lacunarity': 2.0,
        'render_sets': [
            {
                'name': 'red',
                'layers': {
                    'gas': {
                        'type': 'contour',
                        'ranges': [
                            (0, 255, 0, 255, 0, 128, 0, 128),  # Gas
                        ]
                    }
                },
                'layer_order': ['gas']
            },
            {
                'name': 'green',
                'layers': {
                    'gas': {
                        'type': 'contour',
                        'ranges': [
                            (0, 255, 0, 128, 0, 255, 0, 128),  # Gas
                        ]
                    }
                },
                'layer_order': ['gas']
            },
            {
                'name': 'blue',
                'layers': {
                    'gas': {
                        'type': 'contour',
                        'ranges': [
                            (0, 255, 0, 128, 0, 128, 0, 255),  # Gas
                        ]
                    }
                },
                'layer_order': ['gas']
            },
        ]
    },
    'ice': {

    },
    'lava': {
        'octaves_min': 8,
        'octaves_max': 16,
        'frequency_min': 24.0,
        'frequency_max': 36.0,
        'persistence': 0.5,
        'lacunarity': 2.0,
        'render_sets': [
            {
                'name': 'standard',
                'layers': {
                    'surface': {
                        'type': 'contour',
                        'ranges': [
                            (0, 90, 10, 15, 10, 15, 10, 15),     # Dark rock
                            (90, 110, 100, 200, 0, 100, 0, 0),   # Lava patches
                            (110, 150, 15, 33, 15, 33, 15, 33),  # Light rock
                            (150, 170, 200, 100, 100, 0, 0, 0),  # Lava patches
                            (170, 255, 10, 23, 10, 23, 10, 23),  # Dark rock patches
                        ]
                    }
                },
                'layer_order': ['surface']
            },
        ]
    },
    'desert': {

    }
}
