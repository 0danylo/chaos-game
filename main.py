import time
from random import random

import pygame
from pygame import display

w = 800
h = 800
window = pygame.display.set_mode((w, h))

black = (0, 0, 0)
white = (255, 255, 255)
pts = 1000000

sierp = ((100, 100), (w - 100, 100), (int(w / 2), h - 100))


def draw_sierpinski():
    pt = sierp[2]
    window.set_at(pt, white)

    for i in range(pts):
        # time.sleep(0.01)
        vtx = int(random() * 3)
        pt = (int(pt[0] + (sierp[vtx][0] - pt[0]) / 2), int(pt[1] + (sierp[vtx][1] - pt[1]) / 2))
        window.set_at(pt, white)
        # print(i)
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

    draw_bounds(sierp)
    draw_sierpinski()

    while True:
        display.update()
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                break


pygame.init()
create_window()
