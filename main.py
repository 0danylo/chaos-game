import time
from math import cos, pi, sin
from random import random

import pygame
from pygame import display

size = 900
bd = 25  # border

w = size + 2 * bd
h = size + 2 * bd
window = pygame.display.set_mode((w, h))

bg = (0,) * 3
clr = (192,) * 3

pts = 1 * pow(10, 6)
updates = 10


def fractal_avoiding_center_circle(r, frac):
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size))
    pt_q = [vertices[0], vertices[0]]
    window.set_at(pt_q[1], clr)

    for i in range(1, pts + 1):
        # if i % (pts / updates) == 0:
        #     time.sleep(0.25)
        #     display.update()

        j = int(random() * 4)
        pt_q[0] = pt_q[1]
        pt_q[1] = (int(pt_q[1][0] + (vertices[j][0] - pt_q[1][0]) / frac),
                   int(pt_q[1][1] + (vertices[j][1] - pt_q[1][1]) / frac))
        if (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 < r ** 2:
            i -= 1
            pt_q[1] = pt_q[0]
            continue
        window.set_at(pt_q[1], clr)


def vicsek_fractal():
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size), (w / 2, h / 2))
    pt = vertices[0]
    window.set_at(pt, clr)

    for i in range(1, pts + 1):
        if i % (pts / updates) == 0:
            time.sleep(0.25)
            display.update()

        j = int(random() * 5)
        pt = (int(pt[0] + (vertices[j][0] - pt[0]) / 1.5),
              int(pt[1] + (vertices[j][1] - pt[1]) / 1.5))
        window.set_at(pt, clr)


def sierpinski_carpet():
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
                (bd + size / 2, bd), (bd + size / 2, bd + size),
                (bd, bd + size / 2), (bd + size, bd + size / 2))
    pt = vertices[0]
    window.set_at(pt, clr)

    for i in range(1, pts + 1):
        if i % (pts / updates) == 0:
            time.sleep(0.25)
            display.update()

        j = int(random() * 8)
        pt = (int(pt[0] + (vertices[j][0] - pt[0]) / 1.5),
              int(pt[1] + (vertices[j][1] - pt[1]) / 1.5))
        window.set_at(pt, clr)


def perfect_nflake(n):
    """
        Uses a function of n to determine the jump distance between vertices
        to create a visually appealing n-flake, or polyflake
    """
    nflake(n, 3 / n + 1)


def nflake(n, frac):
    vertices = get_reg_poly_vertices(n)
    pt = vertices[0]
    window.set_at(pt, clr)

    for i in range(1, pts + 1):
        if i % (pts / updates) == 0:
            time.sleep(0.25)
            display.update()

        j = int(random() * n)
        pt = (int(pt[0] + (vertices[j][0] - pt[0]) / frac), int(pt[1] + (vertices[j][1] - pt[1]) / frac))
        window.set_at(pt, clr)


def reg_poly_vertices(n):
    for v in get_reg_poly_vertices(n):
        window.set_at((int(v[0]), int(v[1])), clr)


def get_reg_poly_vertices(n):
    vertices = []
    for i in range(n):
        vertices.append((int(w / 2 + (size / 2) * cos(2 * pi * i / n - pi / 2)),
                         int(h / 2 + (size / 2) * sin(2 * pi * i / n - pi / 2))))
    return vertices


def main():
    """
        Window freezes if run for over a few seconds, but shows the fractal in the end
    """

    pygame.display.set_caption('Chaos Game')
    window.fill(bg)
    pygame.display.flip()

    # pygame.draw.circle(window, clr, (w / 2, h / 2), size / 2, 1)
    initial = float(time.time() * 1000)

    # perfect_nflake(3)
    # sierpinski_carpet()
    # vicsek_fractal()
    fractal_avoiding_center_circle(100, 2.5) # !!!

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
    main()
