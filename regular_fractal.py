import time
from random import random

from pygame import display

from main import window, iterations, pt_clr, updates, clrs, get_reg_poly_vertices, bd, size, h, w


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


def nflake(n, frac):
    vertices = get_reg_poly_vertices(n)
    basic_fractal(vertices, frac)


def perfect_nflake(n):
    nflake(n, 3 / n + 1)


def sierpinski_carpet():
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
                (bd + size / 2, bd), (bd + size / 2, bd + size),
                (bd, bd + size / 2), (bd + size, bd + size / 2))
    basic_fractal(vertices, 1.5)


def vicsek_fractal():
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
                (w / 2, h / 2))
    basic_fractal(vertices, 1.5)


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


def restricted_fractal_1(frac):
    """
        the current vertex cannot be chosen in the next iteration
    """
    verts = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size))
    vt_q = [verts[0], verts[0]]
    pt = verts[0]
    window.set_at(pt, pt_clr)
    
    for i in range(1, iterations + 1):
        j = int(random() * 4)
        vt_q[0] = vt_q[1]
        vt_q[1] = verts[j]
        
        if vt_q[0] == vt_q[1]:
            i -= 1
            continue
        pt = (int(pt[0] + (vt_q[1][0] - pt[0]) / frac),
              int(pt[1] + (vt_q[1][1] - pt[1]) / frac))
        window.set_at(pt, pt_clr)
