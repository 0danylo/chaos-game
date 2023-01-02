from random import random

from main import *


def basic_fractal(verts, zoom):
    pt = verts[0]
    
    for i in range(1, points + 1):
        if i % (points / updates) == 0:
            time.sleep(0.25)
            display.update()
        
        j = int(random() * len(verts))
        pt = (pt[0] + (verts[j][0] - pt[0]) / zoom,
              pt[1] + (verts[j][1] - pt[1]) / zoom)
        draw_at(pt)


def nflake(n, zoom):
    vertices = get_reg_poly_vertices(n)
    basic_fractal(vertices, zoom)


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


def fractal_avoiding_center_circle(r, zoom):
    verts = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size))
    pt_q = [verts[0], verts[0]]
    
    for i in range(1, points + 1):
        # if i % (pts / updates) == 0:
        #     time.sleep(0.25)
        #     display.update()
        
        j = int(random() * 4)
        pt_q[0] = pt_q[1]
        pt_q[1] = (pt_q[1][0] + (verts[j][0] - pt_q[1][0]) / zoom,
                   pt_q[1][1] + (verts[j][1] - pt_q[1][1]) / zoom)
        if (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 < r ** 2:
            i -= 1
            pt_q[1] = pt_q[0]
            continue
        draw_at(pt_q[1])


"""
    Fractals in circles
"""


def ic_basic(verts, zoom, r):
    pt_q = [verts[0], verts[0]]
    
    for i in range(1, points + 1):
        j = int(random() * len(verts))
        pt_q[0] = pt_q[1]
        pt_q[1] = (pt_q[1][0] + (verts[j][0] - pt_q[1][0]) / zoom,
                   pt_q[1][1] + (verts[j][1] - pt_q[1][1]) / zoom)
        if (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 > r ** 2:
            i -= 1
            pt_q[1] = pt_q[0]
            continue
        draw_at(pt_q[1])


def ic_nflake(n, r):
    vertices = get_reg_poly_vertices(n)
    ic_basic(vertices, 3 / n + 1, r)


def ic_perfect_nflake(n):
    ic_nflake(n, size / 2.75)


def ic_carpet():
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
                (bd + size / 2, bd), (bd + size / 2, bd + size),
                (bd, bd + size / 2), (bd + size, bd + size / 2))
    ic_basic(vertices, 1.5, size / 2.333)


def ic_vicsek():
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
                (w / 2, h / 2))
    ic_basic(vertices, 1.5, size / 2)


def ic_avoid_center(r_i, zoom, r_o):
    verts = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size))
    pt_q = [verts[0], verts[0]]
    
    for i in range(1, points + 1):
        j = int(random() * 4)
        pt_q[0] = pt_q[1]
        pt_q[1] = (pt_q[1][0] + (verts[j][0] - pt_q[1][0]) / zoom,
                   pt_q[1][1] + (verts[j][1] - pt_q[1][1]) / zoom)
        
        if (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 < r_i ** 2 or \
           (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 > r_o ** 2:
            i -= 1
            pt_q[1] = pt_q[0]
            continue
        draw_at(pt_q[1])


"""
    Fractals restricted by the vertex that can be chosen
"""


def restricted_fractal_2(n, zoom):
    """
        written by GitHub Copilot

        the current vertex cannot be chosen in the next iteration
        and the next vertex cannot be the previous vertex
    """
    # verts = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size))  # Z-pattern of points
    verts = get_reg_poly_vertices(n)
    vt_q = [verts[0], verts[0]]
    pt = verts[0]
    draw_at(pt)
    
    for i in range(1, points + 1):
        j = int(random() * n)
        vt_q[0] = vt_q[1]
        vt_q[1] = verts[j]
        
        if vt_q[0] == vt_q[1] or vt_q[0] == verts[(j + 1) % n]:
            i -= 1
            continue
        pt = (pt[0] + (vt_q[1][0] - pt[0]) / zoom,
              pt[1] + (vt_q[1][1] - pt[1]) / zoom)
        draw_at(pt)


def no_repeats(n, zoom):
    """
        the current vertex cannot be chosen in the next iteration
    """
    verts = get_reg_poly_vertices(n)
    vt_q = [verts[0], verts[0]]
    pt = verts[0]
    draw_at(pt)
    
    for i in range(1, points + 1):
        j = int(random() * n)
        vt_q[0] = vt_q[1]
        vt_q[1] = verts[j]
        
        if vt_q[0] == vt_q[1]:
            i -= 1
            continue
        pt = (pt[0] + (vt_q[1][0] - pt[0]) / zoom,
              pt[1] + (vt_q[1][1] - pt[1]) / zoom)
        draw_at(pt)


def no_neighbors_n_away_cw(sides, n, zoom):
    """
        the current vertex cannot be one place away (clockwise) from the previously chosen vertex
    """
    verts = get_reg_poly_vertices(sides)
    vt_q = [verts[0], verts[0]]
    pt = verts[0]
    draw_at(pt)
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        
        if vt_q[1] == verts[(j + n) % sides]:
            i -= 1
            continue
        
        vt_q[0] = vt_q[1]
        vt_q[1] = verts[j]
        pt = (pt[0] + (vt_q[1][0] - pt[0]) / zoom,
              pt[1] + (vt_q[1][1] - pt[1]) / zoom)
        draw_at(pt)
        
        
def no_cw_neighbors_2(n, zoom):
    """
        written by GitHub Copilot
        
        the current vertex cannot be one place away (clockwise) from the previously chosen vertex
        and the next vertex cannot be the opposite vertex
        
        (actually, the next vertex cannot be two places away (clockwise))
    """
    verts = get_reg_poly_vertices(n)
    vt_q = [verts[0], verts[0]]
    pt = verts[0]
    draw_at(pt)
    
    for i in range(1, points + 1):
        j = int(random() * n)
        
        if vt_q[1] == verts[(j + 1) % n] or vt_q[1] == verts[(j + 2) % n]:
            i -= 1
            continue
        
        vt_q[0] = vt_q[1]
        vt_q[1] = verts[j]
        pt = (pt[0] + (vt_q[1][0] - pt[0]) / zoom,
              pt[1] + (vt_q[1][1] - pt[1]) / zoom)
        draw_at(pt)


def no_repeats_if_last_n_same(sides, n, zoom):
    """
        the currently chosen vertex cannot be the same as the previously chosen vertex
        if the two previously chosen vertices are the same.
    """
    verts = get_reg_poly_vertices(sides)
    vt_q = [verts[0], ] * n
    pt = verts[0]
    draw_at(pt)
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        
        if vt_q.count(vt_q[0]) == len(vt_q) and vt_q[n - 1] == verts[j]:
            i -= 1
            continue
        
        vt_q.append(verts[j])
        vt_q = vt_q[1:]
        pt = (pt[0] + (vt_q[n - 1][0] - pt[0]) / zoom,
              pt[1] + (vt_q[n - 1][1] - pt[1]) / zoom)
        draw_at(pt)
    
    
def no_neighbors_if_last_n_same(sides, n, zoom):
    """
        the currently chosen vertex cannot be one place away from the previously chosen vertex
        if the two previously chosen vertices are the same.
    """
    verts = get_reg_poly_vertices(sides)
    vt_q = [verts[0], ] * n
    pt = verts[0]
    draw_at(pt)
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        
        if vt_q.count(vt_q[0]) == len(vt_q) and \
           (vt_q[n - 1] == verts[(j + 1) % sides] or vt_q[n - 1] == verts[(j - 1) % sides]):
            i -= 1
            continue
        
        vt_q.append(verts[j])
        vt_q = vt_q[1:]
        pt = (pt[0] + (vt_q[n - 1][0] - pt[0]) / zoom,
              pt[1] + (vt_q[n - 1][1] - pt[1]) / zoom)
        draw_at(pt)


def no_cw_neighbors_if_last_n_same(sides, n, zoom):
    """
        the currently chosen vertex cannot be one place away (clockwise) from the previously chosen vertex
        if the two previously chosen vertices are the same.
    """
    verts = get_reg_poly_vertices(sides)
    vt_q = [verts[0], ] * n
    pt = verts[0]
    draw_at(pt)
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        
        if vt_q.count(vt_q[0]) == len(vt_q) and vt_q[n - 1] == verts[(j + 1) % sides]:
            i -= 1
            continue
        
        vt_q.append(verts[j])
        vt_q = vt_q[1:]
        pt = (pt[0] + (vt_q[n - 1][0] - pt[0]) / zoom,
              pt[1] + (vt_q[n - 1][1] - pt[1]) / zoom)
        draw_at(pt)
