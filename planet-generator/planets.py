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
                    },
                    'rivers': {
                        'type': 'river',
                        'paths': {
                            'start_min': 150,
                            'start_max': 200,
                            'end_min': 120,
                            'end_max': 130,
                            'colour_start': (0, 20, 130, 255),
                            'colour_end': (0, 0, 110, 255),
                            'count_min': 5,
                            'count_max': 10,
                            'smooth': True,
                        }
                    }
                },
                'layer_order': ['land', 'rivers', 'sea']
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
        'octaves_min': 4,
        'octaves_max': 16,
        'frequency_min': 16.0,
        'frequency_max': 32.0,
        'persistence': 0.5,
        'lacunarity': 4.0,
        'render_sets': [
            {
                'name': 'white',
                'layers': {
                    'ice': {
                        'type': 'contour',
                        'ranges': [
                            (0, 109, 170, 220, 170, 220, 220, 240),
                            (109, 110, 190, 190, 190, 190, 220, 240),
                            (110, 114, 170, 180, 170, 180, 190, 200),
                            (114, 115, 190, 190, 190, 190, 220, 240),
                            (115, 119, 170, 180, 170, 180, 190, 200),
                            (119, 120, 190, 190, 190, 190, 220, 240),
                            (120, 124, 170, 180, 170, 180, 190, 200),
                            (124, 125, 190, 190, 190, 190, 220, 240),
                            (125, 129, 170, 180, 170, 180, 190, 200),
                            (129, 130, 190, 190, 190, 190, 220, 240),
                            (131, 255, 220, 170, 220, 170, 240, 220),
                        ]
                    },
                },
                'layer_order': ['ice']
            }
        ]
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
                    },
                    'rivers': {
                        'type': 'river',
                        'paths': {
                            'start_min': 150,
                            'start_max': 200,
                            'end_min': 120,
                            'end_max': 130,
                            'colour_start': (0, 20, 130, 255),
                            'colour_end': (0, 0, 110, 255),
                            'count_min': 5,
                            'count_max': 10,
                            'smooth': False,
                        }
                    }
                },
                'layer_order': ['surface', 'rivers']
            },
        ]
    },
    'desert': {

    },
    'star': {
        'octaves_min': 3,
        'octaves_max': 6,
        'frequency_min': 9.0,
        'frequency_max': 16.0,
        'persistence': 0.5,
        'lacunarity': 4.0,
        'render_sets': [
            {
                'name': 'G-class Main Sequence',  # Yellow-White
                'layers': {
                    'surface': {
                        'type': 'contour',
                        'ranges': [
                            (0, 50, 255, 255, 240, 245, 225, 235),     # Main body colour
                            (50, 90, 255, 255, 230, 240, 205, 225),    # Highlights
                            (90, 140, 255, 255, 240, 245, 225, 235),   # Main body colour
                            (140, 200, 255, 255, 230, 240, 205, 225),  # Highlights
                            (200, 255, 255, 255, 240, 245, 225, 235),  # Main body colour
                        ]
                    }
                },
                'layer_order': ['surface']
            },
            {
                'name': 'M-class Main Sequence',  # Light Orange
                'layers': {
                    'surface': {
                        'type': 'contour',
                        'ranges': [
                            (0, 50, 255, 255, 190, 185, 120, 130),     # Main body colour
                            (50, 90, 255, 255, 180, 190, 100, 120),    # Highlights
                            (90, 140, 255, 255, 190, 185, 120, 130),   # Main body colour
                            (140, 200, 255, 255, 180, 190, 100, 120),  # Highlights
                            (200, 255, 255, 255, 190, 185, 120, 130),  # Main body colour
                        ]
                    }
                },
                'layer_order': ['surface']
            }
        ],
        'shadow': False
    }
}


# Stellar Colours (Main Sequence) - http://www.vendian.org/mncharity/dir3/starcolor/

# O5(V)       157 180 255   #9db4ff

# B1(V)       162 185 255   #a2b9ff
# B3(V)       167 188 255   #a7bcff
# B5(V)       170 191 255   #aabfff
# B8(V)       175 195 255   #afc3ff

# A1(V)       186 204 255   #baccff
# A3(V)       192 209 255   #c0d1ff
# A5(V)       202 216 255   #cad8ff

# F0(V)       228 232 255   #e4e8ff
# F2(V)       237 238 255   #edeeff
# F5(V)       251 248 255   #fbf8ff
# F8(V)       255 249 249   #fff9f9

# K0(V)       255 235 209   #ffebd1
# K4(V)       255 215 174   #ffd7ae
# K7(V)       255 198 144   #ffc690
