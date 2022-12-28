from math import cos, pi, sin

import pygame

from fractal_in_circle import *

size = 950  # size of the fractal
bd = 25  # border

w = h = size + 2 * bd
window = pygame.display.set_mode((w, h))

br = 192
bg_clr = (0,) * 3
pt_clr = (br,) * 3
clrs = ((br, 0, 0), (0, br, 0), (0, 0, br),
        (br, br, 0), (br, 0, br), (0, br, br))

iterations = 2 * pow(10, 6)
updates = 10


def main():
    initial = float(time.time() * 1000)

    from regular_fractal import restricted_fractal_1
    restricted_fractal_1(2)
    
    final = float(time.time() * 1000)
    print(str(round((final - initial) / 1000, 4)) + 's')
    
    while True:
        for event in pygame.event.get():
            display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.quit()
        if event.type is pygame.QUIT:
            break


def get_reg_poly_vertices(n):
    vertices = []
    for i in range(n):
        vertices.append((int(w / 2 + (size / 2) * cos(2 * pi * i / n - pi / 2)),
                         int(h / 2 + (size / 2) * sin(2 * pi * i / n - pi / 2))))
    return vertices


def reg_poly_vertices(n):
    for v in get_reg_poly_vertices(n):
        window.set_at((int(v[0]), int(v[1])), pt_clr)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Chaos Game')
    window.fill(bg_clr)
    pygame.display.flip()
    
    main()
