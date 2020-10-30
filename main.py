import pygame
from settings import *
from player import Player
import math
# from map import world_map
# from ray_casting import ray_casting
from sprite_object import *
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))

sprites = Sprites()

clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.move()
    sc.fill(BLACK)

    drawing.background(player.angle)

    #drawing.world(player.pos, player.angle)
    walls = ray_casting(player.pos, player.angle, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls)
                           for obj in sprites.list_of_objects])
    drawing.fps(clock)

    drawing.map(player)

    pygame.display.flip()
    clock.tick()
