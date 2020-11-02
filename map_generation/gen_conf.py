import generator_info

MAP_SIZE = 1000
CONTINENT = 2
CORN_TUNDA = 3
CORN_FOREST = 2
CORN_DESERT = 2
CORN_STEPPE = 10
CORN_SEA = 100

CORN_LIST = [
    (generator_info.Landspace.TUNDA, CORN_TUNDA),
    (generator_info.Landspace.SEA, CORN_SEA),
    (generator_info.Landspace.FOREST, CORN_FOREST),
    (generator_info.Landspace.DESERT, CORN_DESERT),
    (generator_info.Landspace.STEPPE, CORN_STEPPE)
]