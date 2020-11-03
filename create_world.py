import pygame
import map_info
import game_config
import event_const


class StaticObj(pygame.sprite.Sprite):
    act = 0

    def __init__(self, x, y, color=(0, 0, 0), img=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((game_config.DEFAULT_SCALE, game_config.DEFAULT_SCALE))
        if img != None:
            self.image = pygame.image.load(img).convert()
        else:
            self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if not StaticObj.act:
            return
        if StaticObj.act == event_const.BIAS_RIGHT:
                self.rect.x -= game_config.SCROLL_SPEED
        elif StaticObj.act == event_const.BIAS_LEFT:
                self.rect.x += game_config.SCROLL_SPEED
        elif StaticObj.act == event_const.BIAS_UP:
                self.rect.y += game_config.SCROLL_SPEED
        elif StaticObj.act == event_const.BIAS_DOWN:
                self.rect.y -= game_config.SCROLL_SPEED

class StaticWorld:
    def create_world(self, game_map):
        sprites = pygame.sprite.Group()
        sprites_map = list()

        for y in range(game_map["height"]):
            sprites_map.append(list())
            for x in range(game_map["width"]):
                new_sprite = None
                if game_map["map"][y][x] == map_info.Id.SEA:
                    new_sprite = StaticObj(x * game_config.DEFAULT_SCALE, y * game_config.DEFAULT_SCALE, color=map_info.Colors.SEA)
                elif game_map["map"][y][x] == map_info.Id.DESERT:
                    new_sprite = StaticObj(x * game_config.DEFAULT_SCALE, y * game_config.DEFAULT_SCALE, color=map_info.Colors.DESERT)
                elif game_map["map"][y][x] == map_info.Id.FOREST:
                    new_sprite = StaticObj(x * game_config.DEFAULT_SCALE, y * game_config.DEFAULT_SCALE, color=map_info.Colors.FOREST)
                elif game_map["map"][y][x] == map_info.Id.CITY:
                    new_sprite = StaticObj(x * game_config.DEFAULT_SCALE, y * game_config.DEFAULT_SCALE, color=map_info.Colors.CITY)
                elif game_map["map"][y][x] == map_info.Id.STEPPE:
                    new_sprite = StaticObj(x * game_config.DEFAULT_SCALE, y * game_config.DEFAULT_SCALE, color=map_info.Colors.STEPPE)
                elif game_map["map"][y][x] == map_info.Id.TUNDA:
                     new_sprite = StaticObj(x * game_config.DEFAULT_SCALE, y * game_config.DEFAULT_SCALE, color=map_info.Colors.TUNDA)
                else:
                    print(game_map["map"][y][x])
                    exit(1)
                sprites.add(new_sprite)
                sprites_map[y].append(new_sprite)
        return sprites, sprites_map

    def __init__(self, game_map):
        self.game_map = game_map
        self.all_sprites, self.spr_maps = self.create_world(game_map)
    
    def new_act(self, act):
        StaticObj.act = act

    def draw_girds(self, screen):
        x = self.spr_maps[0][0].rect.x
        y = self.spr_maps[0][0].rect.y
        width = self.game_map["width"]
        height = self.game_map["height"]
        for y_f in range(height):
            y_f = y_f * game_config.DEFAULT_SCALE
            pygame.draw.line(screen, (255, 255, 255), [x, y + y_f], [x + (width * game_config.DEFAULT_SCALE), y + y_f])
        for x_f in range(width):
            x_f = x_f * game_config.DEFAULT_SCALE
            pygame.draw.line(screen, (255, 255, 255), [x + x_f, y], [x + x_f, y + (height * game_config.DEFAULT_SCALE)])



    def update(self, screen=None):
        self.all_sprites.update()
        StaticObj.act = 0
        if screen:
            self.all_sprites.draw(screen)