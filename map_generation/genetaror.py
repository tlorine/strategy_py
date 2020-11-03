import gen_conf
import random
import json
from generator_info import Landspace

def seed_coordinates(cont_x, cont_y, id):
    if id == Landspace.SEA:
        x = random.randint(0, gen_conf.MAP_SIZE - 1)
        y = random.randint(0, gen_conf.MAP_SIZE - 1)
    else:            
        x = random.randint(cont_x, cont_x + gen_conf.SIZE_CONTINENT)
        y = random.randint(cont_y, cont_y + gen_conf.SIZE_CONTINENT)
    return x, y

def create_continent(map_list):
    cont_x = random.randint(0, gen_conf.MAP_SIZE - 1)
    cont_y = random.randint(0, gen_conf.MAP_SIZE - 1)
    while cont_x + gen_conf.SIZE_CONTINENT >= gen_conf.MAP_SIZE or cont_y + gen_conf.SIZE_CONTINENT >= gen_conf.MAP_SIZE:
            cont_x = random.randint(0, gen_conf.MAP_SIZE - 1)
            cont_y = random.randint(0, gen_conf.MAP_SIZE - 1)

    for corn in gen_conf.CORN_LIST:
        for _ in range(corn[1]):
            x, y = seed_coordinates(cont_x, cont_y, corn[0])
            while map_list[y][x] != -1:
                x, y = seed_coordinates(cont_x, cont_y, corn[0])
            map_list[y][x] = corn[0]

def gen():
    js_dict = dict()
    map_list = [[-1 for _ in range(gen_conf.MAP_SIZE)] for _ in range(gen_conf.MAP_SIZE)]
    
    for _ in range(gen_conf.CONTINENT):
        create_continent(map_list)
    
    while (True):
        count_ad = 0
        for y in range(gen_conf.MAP_SIZE):
            place_list = list()
            for x in range(gen_conf.MAP_SIZE):
                if map_list[y][x] != -1:
                    if x + 1 < gen_conf.MAP_SIZE and map_list[y][x + 1] == -1 and random.randint(0, 1) == 1:
                        place_list.append((y, x + 1, map_list[y][x]))
                    if x - 1 >= 0 and map_list[y][x - 1] == -1 and random.randint(0, 1) == 1:
                        place_list.append((y, x - 1, map_list[y][x]))
                    if y + 1 < gen_conf.MAP_SIZE and map_list[y + 1][x] == -1 and random.randint(0, 1) == 1:
                        place_list.append((y + 1, x, map_list[y][x]))
                    if y - 1 >= 0 and map_list[y - 1][x] == -1 and random.randint(0, 1) == 1:
                        place_list.append((y - 1, x, map_list[y][x]))
                if map_list[y][x] == -1:
                    count_ad += 1
            for i in place_list:
                map_list[i[0]][i[1]] = i[2]
        if count_ad == 0:
            break



    js_dict["map"] = map_list
    with open("test_map.json", "w") as maps_file:
        maps_file.write(json.dumps(js_dict))
gen()