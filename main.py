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

tri = ((100, h - 100), (w - 100, h - 100), (int(w / 2), 100))

pts = 4 * pow(10, 6)


def draw_triangle():
    frac = 2
    pt = tri[2]
    window.set_at(pt, white)

    for n in range(pts):
        if n % 100 == 0:
            display.update()
        i = int(random() * 3)
        pt = (int(pt[0] + (tri[i][0] - pt[0]) / frac), int(pt[1] + (tri[i][1] - pt[1]) / frac))
        window.set_at(pt, white)
    print('DONE')


def draw_creepers():
    """
a failed attempt produced something cryptic
    """
    pt = tri[2]
    window.set_at(pt, white)

    for n in range(pts):
        i = int(random() * 3)
        pt = (abs(pt[0] - tri[i][0]) / 1.75, abs(pt[1] - tri[i][1]) / 1.75)
        window.set_at((int(pt[0] * 1.85), int(pt[1] * 1.85)), white)  # zooming in
    print('DONE')


def draw_bounds(vertices):
    for v in vertices:
        window.set_at((int(v[0]), int(v[1])), white)


def create_window():
    pygame.display.set_caption('Chaos Game')
    window.fill(black)
    pygame.display.flip()

    # draw_bounds(tri)
    draw_triangle()
    # draw_creepers()

    display.update()

    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                break


pygame.init()
create_window()
