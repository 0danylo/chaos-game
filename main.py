import time
from math import cos, pi, sin, sqrt

import pygame
from pygame import display
import numpy as np

from fractals import *

size = 950  # size of the fractal
bd = 25  # border

w = h = size + 2 * bd
window = pygame.display.set_mode((w, h))

num_shades = 16  # the precision of the brightness
inc = 256 / num_shades

bg_clr = (0,) * 3
pt_clr = (inc,) * 3
clrs = ((inc, inc, inc), (inc, 0, 0), (inc, inc, 0), (0, inc, 0),
        (0, inc, inc), (0, 0, inc), (inc, 0, inc))
num_clrs = len(clrs)

max_br = 0  # to be updated as the fractal is drawn

points = 1 * pow(10, 6)
updates = 10


def main():
    initial = float(time.time() * 1000)
    
    # fractals for demonstration
    
    # avoiding_center_circle(100, 1.9)
    # avoiding_center_circle(100, 2)
    # avoiding_center_circle(100, 2.5, 1)
    # restricted_fractal_2(3, 2)
    # restricted_fractal_2(3, 2.8)
    # restricted_fractal_2(4, 2.25)
    # restricted_fractal_2(5, 2)
    # restricted_fractal_2(6, 1.8)
    # no_neighbors_n_away_cw(3, 1, 2.667)
    # no_neighbors_n_away_cw(4, 2, 2)
    # no_neighbors_n_away_cw(5, 1, 2)
    # no_neighbors_n_away_cw(5, 2, 2)
    # no_cw_neighbors_2(4, 2.75)
    # no_repeats_if_last_n_same(4, 2, 2)
    # no_repeats_if_last_n_same(5, 1, 1.69)
    # no_repeats_if_last_n_same(5, 1, 2.59)
    # no_repeats_if_last_n_same(6, 1, 1.7)
    # no_repeats_if_last_n_same(6, 4, 2)
    # no_neighbors_if_last_n_same(4, 2, 2)
    # no_neighbors_if_last_n_same(4, 2, 2.6)
    # no_neighbors_if_last_n_same(4, 3, 2.6)
    # no_neighbors_if_last_n_same(4, 2, 3.15)
    # no_neighbors_if_last_n_same(5, 2, 2)
    # no_neighbors_if_last_n_same(5, 2, 2.6)
    # no_neighbors_if_last_n_same(6, 1, 2)
    # no_neighbors_if_last_n_same(6, 2, 2)
    # no_cw_neighbors_if_last_n_same(4, 2, 2)
    # no_cw_neighbors_if_last_n_same(5, 1, 2)
    # no_cw_neighbors_if_last_n_same(5, 10, 2)
    # no_cw_neighbors_if_last_n_same(6, 1, 1.475)
    # no_cw_neighbors_if_last_n_same(6, 1, 1.8)
    # no_cw_neighbors_if_last_n_same(6, 1, 1.9)
    # no_cw_neighbors_if_last_n_same(6, 1, 2)
    # no_cw_neighbors_if_last_n_same(6, 10, 1.85, 1)
    # no_cw_neighbors_if_last_n_same(8, 10, 1.7)
    
    final = float(time.time() * 1000)
    print(str(round((final - initial) / 1000, 3)) + 's')
    # normalize_brightness()  # doesn't work (max_br doesn't update)
    
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
        draw_pt(v)


def draw_pt(pt, n=0):
    """
        Add the amount of each color channel to the point's brightness,
        depending on n, which corresponds to the index of the color in clrs.
        Supports 6 colors and white.
    """
    global max_br
    x = int(pt[0])
    y = int(pt[1])
    cur_clr = window.get_at((x, y))
    add_clr = clrs[n]
    pt_br = max(cur_clr[0], cur_clr[1], cur_clr[2])
    
    if pt_br < 256 - inc:
        window.set_at((x, y), (cur_clr[0] + add_clr[0],
                               cur_clr[1] + add_clr[1],
                               cur_clr[2] + add_clr[2]))
        if pt_br + inc > max_br:
            max_br = pt_br + inc
    elif pt_br == 256 - inc:
        new_clr = (num_shades * add_clr[0] - 1 if add_clr[0] > 0 else 0,
                   num_shades * add_clr[1] - 1 if add_clr[1] > 0 else 0,
                   num_shades * add_clr[2] - 1 if add_clr[2] > 0 else 0)
        window.set_at((x, y), new_clr)
        max_br = 255


def normalize_brightness(new_max=255):
    """
        Normalizes the brightness of the fractal to the range [0, 255].
        Best to use 256 shades when using this function
    """
    global max_br
    for x in range(w):
        for y in range(h):
            cur_clr = window.get_at((x, y))
            pt_br = max(cur_clr[0], cur_clr[1], cur_clr[2])
            if pt_br > 0:
                window.set_at((x, y), (0 if max_br == 0 else cur_clr[0] * new_max / max_br,
                                       0 if max_br == 0 else cur_clr[1] * new_max / max_br,
                                       0 if max_br == 0 else cur_clr[2] * new_max / max_br))
    max_br = new_max


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Chaos Game')
    window.fill(bg_clr)
    pygame.display.flip()
    
    main()
