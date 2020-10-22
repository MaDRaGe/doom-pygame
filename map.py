from settings import *


text_map = [
    'wwwwwwwwww',
    'w..w.....w',
    'w.....w..w',
    'w........w',
    'w........w',
    'w........w',
    'w.....ww.w',
    'wwwwwwwwww'
]

world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    print(j, row)
    for i, char in enumerate(row):
        if char == 'w':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
