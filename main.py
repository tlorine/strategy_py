import pygame
import game_config
import map_reader
import event_const
from create_world import StaticWorld

def game_run():
    screen = pygame.display.set_mode(game_config.WINDOW_SIZE)
    running = True

    game_map = map_reader.load_map("test.json")
    world = StaticWorld(game_map)
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                world.new_act(event_const.BIAS_LEFT)
            if event.key == pygame.K_RIGHT:
                world.new_act(event_const.BIAS_RIGHT)
            if event.key == pygame.K_UP:
                world.new_act(event_const.BIAS_UP)
            if event.key == pygame.K_DOWN:
                world.new_act(event_const.BIAS_DOWN)
        world.update(screen)
        world.draw_girds(screen)
        pygame.display.flip()
pygame.init()       
game_run()
pygame.quit()