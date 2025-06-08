from enum import Enum


class BiomeID(Enum):
    FRESHWATER_LAKE = 0
    COASTAL_OCEAN = 1
    RIVER = 2
    ARCTIC = 3


BIOMES = {
    BiomeID.FRESHWATER_LAKE: {
        "name": "Freshwater Lake",
        "fish": ["Bass", "Trout", "Catfish", "Bluegill"]
    },
    BiomeID.COASTAL_OCEAN: {
        "name": "Coastal Ocean",
        "fish": ["Mackerel", "Sea Bass", "Snapper", "Small Shark"]
    },
    BiomeID.RIVER: {
        "name": "River",
        "fish": ["Carp", "Eel", "Pike", "Goby"]
    },
    BiomeID.ARCTIC: {
        "name": "Arctic",
        "fish": ["Cod", "Arctic Char", "Halibut", "Icefish"]
    },
}


def get_biome_for_channel(channel_id: int):
    biome_id = channel_id % 4
    biome = BiomeID(biome_id)
    return BIOMES[biome]
