import gen_conf

def gen():
    map_list = [[-1 for _ in range(gen_conf.MAP_SIZE)] for _ in range(gen_conf.MAP_SIZE)]
    print(*map_list, sep='\n')

gen()