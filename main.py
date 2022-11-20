import time
from math import cos, pi, sin
from random import random

import pygame
from pygame import display

# the size of circle on which the vertices of the polygon are placed
size = 1000

w = size + 25
h = size + 25
window = pygame.display.set_mode((w, h))

black = (0, 0, 0)
white = (255, 255, 255)

pts = 4 * pow(10, 6)
updates = 50


def draw_reg_poly_fractal(n, frac):
    vertices = reg_poly_vertices(n)
    pt = vertices[0]
    window.set_at(pt, white)

    for i in range(1, pts + 1):
        if i % (pts / updates) == 0:
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
        vertices.append((int(w / 2 + (size / 2) * cos(2 * pi * i / n)), int(h / 2 + (size / 2) * sin(2 * pi * i / n))))
    return vertices


def create_window():
    pygame.display.set_caption('Chaos Game')
    window.fill(black)
    pygame.display.flip()

    initial = float(time.time() * 1000)
    draw_reg_poly_fractal(9, 1.6)
    final = float(time.time() * 1000)
    print(str(round((final - initial) / 1000, 4)) + 's')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
            if event.type is pygame.QUIT:
                break


if __name__ == '__main__':
    pygame.init()
    create_window()
