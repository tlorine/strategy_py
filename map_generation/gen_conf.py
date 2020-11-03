import generator_info

MAP_SIZE = 100

CONTINENT = 5
SIZE_CONTINENT = 10

CORN_TUNDA = 1
CORN_FOREST = 2
CORN_DESERT = 1
CORN_STEPPE = 5
CORN_SEA = 3

CORN_LIST = [
    (generator_info.Landspace.TUNDA, CORN_TUNDA),
    (generator_info.Landspace.SEA, CORN_SEA),
    (generator_info.Landspace.FOREST, CORN_FOREST),
    (generator_info.Landspace.DESERT, CORN_DESERT),
    (generator_info.Landspace.STEPPE, CORN_STEPPE)
]