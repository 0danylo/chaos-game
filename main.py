import time
from math import cos, pi, sin
from random import random

import pygame
from pygame import display

# the size of circle on which the vertices of the polygon are placed
size = 900
bd = 25  # border

w = size + 2 * bd
h = size + 2 * bd
window = pygame.display.set_mode((w, h))

black = (0, 0, 0)
white = (255, 255, 255)

pts = 10 * pow(10, 5)
updates = 10


# needs more research (supposed to draw circles everywhere, but maybe try a different shape?)
def avoid_center_circle(r):
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size))
    pt = vertices[0]
    window.set_at(pt, white)
    for i in range(1, pts + 1):
        if i % (pts / updates) == 0:
            time.sleep(0.25)
            display.update()
        j = int(random() * 5)
        pt = (int(pt[0] + (vertices[j][0] - pt[0]) / 1.5), int(pt[1] + (vertices[j][1] - pt[1]) / 1.5))
        if (pt[0] - w / 2) ** 2 + (pt[1] - h / 2) ** 2 < r ** 2:
            i -= 1
            continue
        window.set_at(pt, white)


def vicsek_fractal():
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size), (w / 2, h / 2))
    pt = vertices[0]
    window.set_at(pt, white)

    for i in range(1, pts + 1):
        if i % (pts / updates) == 0:
            time.sleep(0.25)
            display.update()
        j = int(random() * 5)
        pt = (int(pt[0] + (vertices[j][0] - pt[0]) / 1.5), int(pt[1] + (vertices[j][1] - pt[1]) / 1.5))
        window.set_at(pt, white)
    print('DONE')


def sierpinski_carpet():
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
                (bd + size / 2, bd), (bd + size / 2, bd + size),
                (bd, bd + size / 2), (bd + size, bd + size / 2))
    pt = vertices[0]
    window.set_at(pt, white)
    for i in range(1, pts + 1):
        if i % (pts / updates) == 0:
            time.sleep(0.25)
            display.update()
        j = int(random() * 8)
        pt = (int(pt[0] + (vertices[j][0] - pt[0]) / 1.5), int(pt[1] + (vertices[j][1] - pt[1]) / 1.5))
        window.set_at(pt, white)
    print('DONE')


def perfect_nflake(n):
    # approximate function for distance to jump such that
    # each section of the fractal (with n sections) is close together
    nflake(n, 3 / n + 1)


def nflake(n, frac):
    vertices = get_reg_poly_vertices(n)
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


def reg_poly_vertices(n):
    for v in get_reg_poly_vertices(n):
        window.set_at((int(v[0]), int(v[1])), white)


def get_reg_poly_vertices(n):
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

    # draw_perfect_nflake(3)
    # sierpinski_carpet()
    # vicsek_fractal()
    avoid_center_circle(100)

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
