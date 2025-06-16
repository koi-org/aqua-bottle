from enum import Enum


class BiomeID(Enum):
    FRESHWATER_LAKE = 0
    COASTAL_OCEAN = 1
    RIVER = 2
    ARCTIC = 3


# Detailed fish data with name, rarity, size (example properties)
FISH_DATA = {
    "Bass": {
        "rarity": "Common",
        "size_cm": 35,
        "description": "A popular freshwater game fish.",
    },
    "Trout": {
        "rarity": "Common",
        "size_cm": 40,
        "description": "Freshwater fish found in cold streams.",
    },
    "Catfish": {
        "rarity": "Uncommon",
        "size_cm": 70,
        "description": "Bottom-dwelling fish with whiskers.",
    },
    "Bluegill": {
        "rarity": "Common",
        "size_cm": 15,
        "description": "Small sunfish species.",
    },
    "Mackerel": {
        "rarity": "Common",
        "size_cm": 30,
        "description": "Fast-swimming ocean fish.",
    },
    "Sea Bass": {
        "rarity": "Uncommon",
        "size_cm": 50,
        "description": "Coastal ocean predator.",
    },
    "Snapper": {"rarity": "Rare", "size_cm": 60, "description": "Colorful reef fish."},
    "Small Shark": {
        "rarity": "Rare",
        "size_cm": 120,
        "description": "Smaller shark species found near coast.",
    },
    "Carp": {"rarity": "Common", "size_cm": 40, "description": "Large river fish."},
    "Eel": {
        "rarity": "Uncommon",
        "size_cm": 50,
        "description": "Slender, snake-like fish.",
    },
    "Pike": {
        "rarity": "Rare",
        "size_cm": 90,
        "description": "Aggressive river predator.",
    },
    "Goby": {"rarity": "Common", "size_cm": 12, "description": "Small bottom-dweller."},
    "Cod": {
        "rarity": "Common",
        "size_cm": 60,
        "description": "Cold water fish found in arctic regions.",
    },
    "Arctic Char": {
        "rarity": "Uncommon",
        "size_cm": 55,
        "description": "Cold-water salmonid.",
    },
    "Halibut": {"rarity": "Rare", "size_cm": 150, "description": "Large flatfish."},
    "Icefish": {
        "rarity": "Rare",
        "size_cm": 35,
        "description": "Fish adapted to freezing waters.",
    },
}

BIOMES = {
    BiomeID.FRESHWATER_LAKE: {
        "name": "Freshwater Lake",
        "fish": ["Bass", "Trout", "Catfish", "Bluegill"],
    },
    BiomeID.COASTAL_OCEAN: {
        "name": "Coastal Ocean",
        "fish": ["Mackerel", "Sea Bass", "Snapper", "Small Shark"],
    },
    BiomeID.RIVER: {"name": "River", "fish": ["Carp", "Eel", "Pike", "Goby"]},
    BiomeID.ARCTIC: {
        "name": "Arctic",
        "fish": ["Cod", "Arctic Char", "Halibut", "Icefish"],
    },
}


def get_biome_for_channel(channel_id):
    channel_int = int(channel_id)
    # print("channel id:", channel_id)
    biome_id = channel_int % 4
    # print("biome id:", biome_id)
    biome = BiomeID(biome_id)
    return BIOMES[biome]


def get_fish_info(fish_name: str):
    return FISH_DATA.get(fish_name)
