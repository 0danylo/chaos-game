import time
from math import cos, pi, sin
from random import random

import pygame
from pygame import display

size = 950
bd = 25  # border

w = size + 2 * bd
h = size + 2 * bd
window = pygame.display.set_mode((w, h))

bg_clr = (0,) * 3
pt_clr = (192,) * 3
clrs = ((192, 0, 0), (0, 192, 0), (0, 0, 192),
        (192, 192, 0), (192, 0, 192), (0, 192, 192))

iterations = 1 * pow(10, 6)
updates = 10


def fractal_avoiding_center_circle(r, frac):
   verts = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size))
   pt_q = [verts[0], verts[0]]
   window.set_at(pt_q[1], pt_clr)
   
   for i in range(1, iterations + 1):
      # if i % (pts / updates) == 0:
      #     time.sleep(0.25)
      #     display.update()
      
      j = int(random() * 4)
      pt_q[0] = pt_q[1]
      pt_q[1] = (int(pt_q[1][0] + (verts[j][0] - pt_q[1][0]) / frac),
                 int(pt_q[1][1] + (verts[j][1] - pt_q[1][1]) / frac))
      if (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 < r ** 2:
         i -= 1
         pt_q[1] = pt_q[0]
         continue
      window.set_at(pt_q[1], pt_clr)


def vicsek_fractal():
   vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
               (w / 2, h / 2))
   basic_fractal(vertices, 1.5)


def sierpinski_carpet():
   vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
               (bd + size / 2, bd), (bd + size / 2, bd + size),
               (bd, bd + size / 2), (bd + size, bd + size / 2))
   basic_fractal(vertices, 1.5)


def perfect_nflake(n):
   nflake(n, 3 / n + 1)


def nflake(n, frac):
   vertices = get_reg_poly_vertices(n)
   basic_fractal(vertices, frac)


def basic_fractal(verts, frac):
   pt = verts[0]
   window.set_at(pt, pt_clr)
   
   for i in range(1, iterations + 1):
      if i % (iterations / updates) == 0:
         time.sleep(0.25)
         display.update()
      
      j = int(random() * len(verts))
      pt = (int(pt[0] + (verts[j][0] - pt[0]) / frac),
            int(pt[1] + (verts[j][1] - pt[1]) / frac))
      window.set_at(pt, clrs[j % len(clrs)])


def reg_poly_vertices(n):
   for v in get_reg_poly_vertices(n):
      window.set_at((int(v[0]), int(v[1])), pt_clr)


def get_reg_poly_vertices(n):
   vertices = []
   for i in range(n):
      vertices.append((int(w / 2 + (size / 2) * cos(2 * pi * i / n - pi / 2)),
                       int(h / 2 + (size / 2) * sin(2 * pi * i / n - pi / 2))))
   return vertices


def main():
   pygame.display.set_caption('Chaos Game')
   window.fill(bg_clr)
   pygame.display.flip()
   
   # pygame.draw.circle(window, clr, (w / 2, h / 2), size / 2, 1)
   initial = float(time.time() * 1000)
   
   perfect_nflake(5)
   # sierpinski_carpet()
   # vicsek_fractal()
   # fractal_avoiding_center_circle(100, 2.5) # !!!
   
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
