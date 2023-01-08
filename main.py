import time
from asyncio import sleep
from math import cos, pi, sin, sqrt

import pygame
from pygame import display
import numpy as np

from fractals import *

size = 950  # size of the fractal
bd = 25  # border

w = h = size + 2 * bd
window = pygame.display.set_mode((w, h))

num_shades = 256  # the precision of the brightness
inc = 256 / num_shades  # increment when overwriting brightness

bg_clr = (0,) * 3  # background color (black)
pt_clr = (inc,) * 3  # base point color
clrs = ((inc, inc, inc),
        (inc, 0, 0), (inc, inc, 0), (0, inc, 0),
        (0, inc, inc), (0, 0, inc), (inc, 0, inc))
num_clrs = len(clrs)

points = 4 * pow(10, 6)  # number of points to draw
updates = 10  # number of times to update the screen


def main():
    initial = float(time.time() * 1000)
    
    # fractals for demonstration
    
    # avoiding_center_circle(100, 1.9)
    # avoiding_center_circle(100, 2)
    # avoiding_center_circle(100, 2.5)
    # no_neighbors_n_away_cw(3, 1, 2.667)
    # no_neighbors_n_away_cw(4, 2, 2)
    # no_neighbors_n_away_cw(5, 1, 2)
    # no_neighbors_n_away_cw(5, 2, 2)
    # no_repeats_if_last_n_same(4, 2, 2)
    # no_repeats_if_last_n_same(5, 1, 1.69)
    # no_repeats_if_last_n_same(5, 1, 2.59)
    # no_repeats_if_last_n_same(6, 1, 1.7)
    # no_repeats_if_last_n_same(6, 4, 2)
    # no_neighbors_if_last_n_same(4, 2, 2)  # wtf
    # no_neighbors_if_last_n_same(4, 2, 2.6)
    # no_neighbors_if_last_n_same(4, 3, 2.6)
    # no_neighbors_if_last_n_same(4, 2, 3.15)
    # no_neighbors_if_last_n_same(5, 2, 2)
    # no_neighbors_if_last_n_same(5, 2, 2.6)
    # no_neighbors_if_last_n_same(6, 1, 2)
    # no_neighbors_if_last_n_same(6, 2, 2)
    # no_cw_neighbor_if_last_n_same(4, 2, 2)
    # no_cw_neighbor_if_last_n_same(5, 10, 2)
    # no_cw_neighbor_if_last_n_same(6, 1, 1.5)
    # no_cw_neighbor_if_last_n_same(6, 1, 1.8)
    # no_cw_neighbor_if_last_n_same(6, 1, 1.9)
    # no_cw_neighbor_if_last_n_same(6, 1, 2)
    # no_cw_neighbor_if_last_n_same(6, 10, 1.85)
    # no_cw_neighbor_if_last_n_same(8, 10, 1.7)
    
    # restricted_fractal_2(3, 2)  # wtf
    # restricted_fractal_2(3, 2.8)
    # restricted_fractal_2(4, 2.25)
    # restricted_fractal_2(5, 2)
    # restricted_fractal_2(6, 1.8)
    # no_cw_neighbors_2(4, 2.615)
    # no_cw_neighbors_2(4, 3.15)
    # no_cw_neighbors_2(5, 1.97)
    # no_cw_neighbors_2(5, 2.24)
    # no_cw_neighbors_2(5, 2.42)
    # no_cw_neighbors_2(6, 1.7)
    # no_cw_neighbors_2(6, 2)
    # no_cw_neighbors_2(6, 2.2)
    no_cw_neighbors_2(8, 1.8)
    
    final = float(time.time() * 1000)
    print(str(round((final - initial) / 1000, 3)) + 's')
    normalize_brightness()  # doesn't work
    # pygame.image.save(window, "test_fractal.png")
    
    while True:
        for event in pygame.event.get():
            display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
            if event.type is pygame.QUIT:
                break


def get_reg_poly_vertices(n):
    vertices = []
    if n == 3:  # maximum size triangle
        vertices = ((bd + size / 2, bd),
                    (bd, bd + size * sqrt(3) / 2),
                    (bd + size, bd + size * sqrt(3) / 2))
    elif n == 4:  # maximum size square
        vertices = ((bd, bd), (bd + size, bd), (bd + size, bd + size), (bd, bd + size))
    else:
        for i in range(n):
            vertices.append((w / 2 + (size / 2) * cos(2 * pi * i / n - pi / 2),
                             h / 2 + (size / 2) * sin(2 * pi * i / n - pi / 2)))
    return vertices


def draw_pt(pt, n=0):
    """
        Add the amount of each color channel to the point's brightness,
        depending on n, which corresponds to the index of the color in clrs.
        Supports 6 colors and white.
    """
    x = int(pt[0])
    y = int(pt[1])
    cur_clr = window.get_at((x, y))
    add_clr = clrs[n]
    pt_br = max(cur_clr[0], cur_clr[1], cur_clr[2])
    
    if pt_br < 256 - inc:
        window.set_at((x, y), (cur_clr[0] + add_clr[0],
                               cur_clr[1] + add_clr[1],
                               cur_clr[2] + add_clr[2]))
    elif pt_br == 256 - inc:
        new_clr = (255 if add_clr[0] > 0 else 0,
                   255 if add_clr[1] > 0 else 0,
                   255 if add_clr[2] > 0 else 0)
        window.set_at((x, y), new_clr)


def normalize_brightness(new_max=255):
    """
        Normalizes the brightness of the fractal to the range [0, 255].
        Using 256 shades with this function makes the fractal perfectly accurate,
        but quite dim since many points are only visited a few times.
        With more points, the fractal is more visually appealing, though only
        accurate up to a certain point.
    """
    max_br = 0
    for y in range(bd, size + bd):
        for x in range(bd, size + bd):
            cur_clr = window.get_at((x, y))
            pt_br = max(cur_clr[0], cur_clr[1], cur_clr[2])
            if pt_br > max_br:
                max_br = pt_br
    
    """
        When the maximum brightness is low, the fractal is more visible because
        the brightness is more evenly distributed. This allows for a greater number
        of points, but its not necessary. However, this does not account for the black
        background on fairly empty fractals. Instead, the visibility should be calculated
        using the number of points visited. This can be used to determine the maximum
        number of points that can be placed without diminishing accuracy.
    """
    print(max_br)
    
    for y in range(bd, size + bd):
        for x in range(bd, size + bd):
            cur_clr = window.get_at((x, y))
            pt_br = max(cur_clr[0], cur_clr[1], cur_clr[2])
            if pt_br > 0:
                window.set_at((x, y), (cur_clr[0] * new_max / max_br,
                                       cur_clr[1] * new_max / max_br,
                                       cur_clr[2] * new_max / max_br))
        display.update()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Chaos Game')
    window.fill(bg_clr)
    pygame.display.flip()
    
    main()
