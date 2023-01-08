from random import random

from main import *


def basic_fractal(vertices, jump, clr=0):
    pt = vertices[0]
    n = len(vertices)
    
    for i in range(1, points + 1):
        # if i % (points / updates) == 0:
        #     time.sleep(0.25)
        #     display.update()
        
        j = int(random() * n)
        pt = (pt[0] + (vertices[j][0] - pt[0]) / jump,
              pt[1] + (vertices[j][1] - pt[1]) / jump)
        draw_pt(pt, 0 if clr == 0 else j + 1)


def nflake(n, jump, clr=0):
    vertices = get_reg_poly_vertices(n)
    basic_fractal(vertices, jump, clr)


def perfect_nflake(sides, clr=0):
    nflake(sides, 3 / sides + 1, clr)


def carpet(clr=0):
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
                (bd + size / 2, bd), (bd + size / 2, bd + size),
                (bd, bd + size / 2), (bd + size, bd + size / 2))
    basic_fractal(vertices, 1.5, clr)


def vicsek(clr=0):
    vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
                (w / 2, h / 2))
    basic_fractal(vertices, 1.5, clr)


def avoiding_center_circle(r, jump, clr=0):
    vertices = get_reg_poly_vertices(4)
    pt_q = [vertices[0], vertices[0]]
    
    for i in range(1, points + 1):
        j = int(random() * 4)
        pt_q[0] = pt_q[1]
        pt_q[1] = (pt_q[1][0] + (vertices[j][0] - pt_q[1][0]) / jump,
                   pt_q[1][1] + (vertices[j][1] - pt_q[1][1]) / jump)
        
        if (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 < r ** 2:
            i -= 1
            pt_q[1] = pt_q[0]
            continue
        draw_pt(pt_q[1], 0 if clr == 0 else j + 1)


"""
    Fractals restricted by the vertex that can be chosen
"""


def restricted_fractal_2(sides, jump, clr=0):
    """
        written by GitHub Copilot

        the current vertex cannot be chosen in the next iteration
        and the next vertex cannot be the previous vertex
    """
    vertices = get_reg_poly_vertices(sides)
    vt_q = [vertices[0], vertices[0]]
    pt = vertices[0]
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        vt_q[0] = vt_q[1]
        vt_q[1] = vertices[j]
        if vt_q[0] == vt_q[1] or vt_q[0] == vertices[(j + 1) % sides]:
            i -= 1
            continue
            
        pt = (pt[0] + (vt_q[1][0] - pt[0]) / jump,
              pt[1] + (vt_q[1][1] - pt[1]) / jump)
        draw_pt(pt, 0 if clr == 0 else j + 1)


def no_neighbors_n_away_cw(sides, n, jump, clr=0):
    """
        the current vertex cannot be one place away (clockwise) from the previously chosen vertex
    """
    vertices = get_reg_poly_vertices(sides)
    vt_q = [vertices[0], vertices[0]]
    pt = vertices[0]
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        if vt_q[1] == vertices[(j + n) % sides]:
            i -= 1
            continue
        
        vt_q[0] = vt_q[1]
        vt_q[1] = vertices[j]
        pt = (pt[0] + (vt_q[1][0] - pt[0]) / jump,
              pt[1] + (vt_q[1][1] - pt[1]) / jump)
        draw_pt(pt, 0 if clr == 0 else j + 1)


def no_cw_neighbors_2(sides, jump, clr=0):
    """
        written by GitHub Copilot
        
        the current vertex cannot be one place away (clockwise) from the previously chosen vertex
        and the next vertex cannot be the opposite vertex
        
        (actually, the next vertex cannot be two places away (clockwise))
    """
    vertices = get_reg_poly_vertices(sides)
    vt_q = [vertices[0], vertices[0]]
    pt = vertices[0]
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        if vt_q[1] == vertices[(j + 1) % sides] or vt_q[1] == vertices[(j + 2) % sides]:
            i -= 1
            continue
        
        vt_q[0] = vt_q[1]
        vt_q[1] = vertices[j]
        pt = (pt[0] + (vt_q[1][0] - pt[0]) / jump,
              pt[1] + (vt_q[1][1] - pt[1]) / jump)
        draw_pt(pt, 0 if clr == 0 else j + 1)


def no_repeats_if_last_n_same(sides, n, jump, clr=0):
    """
        the currently chosen vertex cannot be the same as the previously chosen vertex
        if the two previously chosen vertices are the same.
    """
    vertices = get_reg_poly_vertices(sides)
    vt_q = [vertices[0], ] * n
    pt = vertices[0]
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        if vt_q.count(vt_q[0]) == n and vt_q[n - 1] == vertices[j]:
            i -= 1
            continue
        
        vt_q.append(vertices[j])
        vt_q = vt_q[1:]
        pt = (pt[0] + (vt_q[0][0] - pt[0]) / jump,
              pt[1] + (vt_q[0][1] - pt[1]) / jump)
        draw_pt(pt, 0 if clr == 0 else j + 1)


def no_neighbors_if_last_n_same(sides, n, jump, clr=0):
    """
        the currently chosen vertex cannot be one place away from the previously chosen vertex
        if the two previously chosen vertices are the same.
    """
    vertices = get_reg_poly_vertices(sides)
    vt_q = [vertices[0], ] * n
    pt = vertices[0]
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        
        if vt_q.count(vt_q[0]) == n and \
                (vt_q[0] == vertices[(j + 1) % sides] or
                 vt_q[0] == vertices[(j - 1) % sides]):
            i -= 1
            continue
        
        vt_q.append(vertices[j])
        vt_q = vt_q[1:]
        pt = (pt[0] + (vt_q[n - 1][0] - pt[0]) / jump,
              pt[1] + (vt_q[n - 1][1] - pt[1]) / jump)
        draw_pt(pt, 0 if clr == 0 else j + 1)


def no_cw_neighbor_if_last_n_same(sides, n, jump, clr=0):
    """
        the currently chosen vertex cannot be one place away (clockwise) from the previously chosen vertex
        if the two previously chosen vertices are the same.
    """
    vertices = get_reg_poly_vertices(sides)
    vt_q = [vertices[0], ] * n
    pt = vertices[0]
    
    for i in range(1, points + 1):
        j = int(random() * sides)
        
        if vt_q.count(vt_q[0]) == n and vt_q[0] == vertices[(j + 1) % sides]:
            i -= 1
            continue
        
        vt_q.append(vertices[j])
        vt_q = vt_q[1:]
        pt = (pt[0] + (vt_q[n - 1][0] - pt[0]) / jump,
              pt[1] + (vt_q[n - 1][1] - pt[1]) / jump)
        draw_pt(pt, 0 if clr == 0 else j + 1)
