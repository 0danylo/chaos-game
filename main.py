import time
from math import cos, pi, sin, sqrt

import pygame
from pygame import display

from fractals import *

size = 950  # size of the fractal
bd = 25  # border

w = h = size + 2 * bd
window = pygame.display.set_mode((w, h))

br = 255
bg_clr = (0,) * 3
pt_clr = (br,) * 3
clrs = ((br, 0, 0), (0, br, 0), (0, 0, br),
        (br, br, 0), (br, 0, br), (0, br, br))

max_br = 0  # to be updated as the fractal is drawn

points = 2 * pow(10, 6)
updates = 10


def main():
    initial = float(time.time() * 1000)
    
    # cool fractals for demonstration
    
    # fractal_avoiding_center_circle(100, 1.9)
    # fractal_avoiding_center_circle(100, 2)
    # fractal_avoiding_center_circle(100, 2.5)
    # restricted_fractal_2(3, 2)
    # restricted_fractal_2(4, 2)
    # no_repeats(5, 1.69)
    # no_repeats(5, 2.59)
    # no_repeats(6, 1.7)
    # no_neighbors_n_away_cw(3, 1, 2.667)
    # no_neighbors_n_away_cw(4, 2, 2)
    # no_neighbors_n_away_cw(5, 1, 2)
    # no_neighbors_n_away_cw(5, 2, 2)
    # no_cw_neighbors_2(4, 2.75)
    # no_repeats_if_last_n_same(4, 2, 2)
    # no_repeats_if_last_n_same(6, 4, 2)
    # no_neighbors_if_last_n_same(4, 2, 2)
    # no_neighbors_if_last_n_same(5, 2, 2)
    no_neighbors_if_last_n_same(6, 2, 2)
    
    # no_cw_neighbors_if_last_n_same(4, 2, 2)
    # no_cw_neighbors_if_last_n_same(5, 1, 2)
    # no_cw_neighbors_if_last_n_same(5, 10, 2)
    # no_cw_neighbors_if_last_n_same(6, 1, 1.475)
    # no_cw_neighbors_if_last_n_same(6, 1, 1.8)
    # no_cw_neighbors_if_last_n_same(6, 1, 1.9)
    # no_cw_neighbors_if_last_n_same(6, 1, 2)
    # no_cw_neighbors_if_last_n_same(6, 10, 1.85)
    # no_cw_neighbors_if_last_n_same(8, 10, 1.7)
    # no_cw_neighbors_if_last_n_same(10, 1, 1.8)
    
    final = float(time.time() * 1000)
    print(str(round((final - initial) / 1000, 3)) + 's')
    # normalize_brightness()  # doesn't work
    
    while True:
        for event in pygame.event.get():
            display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
            if event.type is pygame.QUIT:
                break


def get_reg_poly_vertices(n):
    vertices = []
    if n == 3:
        vertices = ((bd + size / 2, bd),
                    (bd, bd + size * sqrt(3) / 2),
                    (bd + size, bd + size * sqrt(3) / 2))
    elif n == 4:
        vertices = ((bd, bd), (bd + size, bd), (bd + size, bd + size), (bd, bd + size))
    else:
        for i in range(n):
            vertices.append((w / 2 + (size / 2) * cos(2 * pi * i / n - pi / 2),
                             h / 2 + (size / 2) * sin(2 * pi * i / n - pi / 2)))
    return vertices


def reg_poly_vertices(n):
    for v in get_reg_poly_vertices(n):
        window.set_at((int(v[0]), int(v[1])), pt_clr)


def draw_at(pt):
    """
        If there is already a point at (x, y), its brightness is increased.
    """
    global max_br
    x = int(pt[0])
    y = int(pt[1])
    pt_br = window.get_at((x, y))[0]
    
    num_shades = 16  # the precision of the brightness
    inc = 256 / num_shades
    
    if pt_br < 256 - inc:
        window.set_at((x, y), (pt_br + inc,) * 3)
        if pt_br + inc > max_br:
            max_br = pt_br + inc
    elif pt_br == 256 - inc:
        window.set_at((x, y), (255,) * 3)
        max_br = 255


def normalize_brightness():
    """
        Normalizes the brightness of the fractal to the range [0, 255].
        Best to use 256 shades when using this function
    """
    for x in range(bd, w):
        for y in range(bd, h):
            cur_clr = window.get_at((x, y))
            if cur_clr[0] > 0:
                print(max_br)
                window.set_at((x, y), (int(cur_clr[0] * 255 / max_br),) * 3)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Chaos Game')
    window.fill(bg_clr)
    pygame.display.flip()
    
    main()
