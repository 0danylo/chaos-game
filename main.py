import math
import time
from math import cos, pi, sin
from random import random

import pygame
from pygame import display

# the size of circle on which the vertices of the polygon are placed
size = 900
bd = 25  # border

w = size + bd
h = size + bd
window = pygame.display.set_mode((w, h))

black = (0, 0, 0)
white = (255, 255, 255)

pts = 1 * pow(10, 5)
updates = 10


def draw_carpet():
    coords = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
              )


def draw_perfect_polyflake(n):
    # approximate function for distance to jump
    # each section of the fractal (with n sections) is close together
    draw_polyflake(n, 3 / n + 1)


def draw_polyflake(n, frac):
    vertices = reg_poly_vertices(n)
    pt = vertices[0]
    window.set_at(pt, white)

    for i in range(1, pts + 1):
        if i % (pts / updates) == 0:
            time.sleep(0.25)
            display.update()
        j = int(random() * n)
        pt = (int(pt[0] + (vertices[j][0] - pt[0]) / frac), int(pt[1] + (vertices[j][1] - pt[1]) / frac))
        window.set_at(pt, white)
    print('DONE')


def draw_reg_poly_vertices(n):
    for v in reg_poly_vertices(n):
        window.set_at((int(v[0]), int(v[1])), white)


def reg_poly_vertices(n):
    vertices = []
    for i in range(n):
        vertices.append((int(w / 2 + (size / 2) * cos(2 * pi * i / n - pi / 2)),
                         int(h / 2 + (size / 2) * sin(2 * pi * i / n - pi / 2))))
    return vertices


def create_window():
    pygame.display.set_caption('Chaos Game')
    window.fill(black)
    pygame.display.flip()

    initial = float(time.time() * 1000)

    # draw_perfect_polyflake(3)
    draw_carpet()
    
    final = float(time.time() * 1000)
    print(str(round((final - initial) / 1000, 4)) + 's')

    while True:
        for event in pygame.event.get():
	        display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
            if event.type is pygame.QUIT:
                break


if __name__ == '__main__':
    pygame.init()
    create_window()
