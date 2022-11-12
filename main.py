import time
from math import sqrt
from random import random

import pygame
from pygame import display

# the size of the fractal itself (the width of the triangle)
size = 800

w = size + 200
h = size / (2 / sqrt(3)) + 200
window = pygame.display.set_mode((w, h))

black = (0, 0, 0)
white = (255, 255, 255)
pts = 1000000

sierp = ((100, h - 100), (w - 100, h - 100), (int(w / 2), 100))


def draw_sierpinski():
    pt = sierp[2]
    window.set_at(pt, white)

    for i in range(pts):
        if i % 100 == 0:
            display.update()
        vtx = int(random() * 3)
        pt = (int(pt[0] + (sierp[vtx][0] - pt[0]) / 2), int(pt[1] + (sierp[vtx][1] - pt[1]) / 2))
        window.set_at(pt, white)
        # print(i) # for debugging
    print('DONE')


def draw_creepers():
    """
a failed attempt produced something terrifying
    """
    pt = sierp[2]
    window.set_at(pt, white)

    for i in range(pts):
        vtx = int(random() * 3)
        pt = (int(abs(pt[0] - sierp[vtx][0]) / 2), int(abs(pt[1] - sierp[vtx][1]) / 2))
        window.set_at(pt, white)
    print('DONE')


def draw_bounds(vertices):
    for v in vertices:
        window.set_at((int(v[0]), int(v[1])), white)


def create_window():
    pygame.display.set_caption("Chaos Game")
    window.fill(black)
    pygame.display.flip()

    # draw_bounds(sierp)
    draw_sierpinski()
    # draw_creepers()

    display.update()

    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                break


pygame.init()
create_window()
