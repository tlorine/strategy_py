import json
import os.path
import game_config

def get_map(map_name):
    if not os.path.exists("maps"):
        print("maps dont exists")
        return None
    with open(os.path.join("maps", map_name), "r") as maps_file:
        game_map = json.loads(maps_file.read())
    return game_map

def maps_valited(game_map):
    if not game_map:
        return False
    if (not "map" in game_map) or (not game_map["map"]):
        return False
    tmp_map = game_map["map"]
    height = len(tmp_map)
    width = len(tmp_map[0])

    game_map["height"] = height
    game_map["width"] = width
    if height < game_config.MAP_HEIGHT_SIZE["min"] or height > game_config.MAP_HEIGHT_SIZE["max"]:
        print("wrong height size")
        return False
    if width < game_config.MAP_WIDTH_SIZE["min"] or width > game_config.MAP_WIDTH_SIZE["max"]:
        print("wrong width size")
        return False
    return True

def load_map(map_name):
    game_map = get_map(map_name)
    if maps_valited(game_map) == False:
        return None
    return game_map