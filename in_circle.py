"""
    Fractals in circles
"""


# def ic_basic(verts, zoom, r):
#     pt_q = [verts[0], verts[0]]
#
#     for i in range(1, points + 1):
#         j = int(random() * len(verts))
#         pt_q[0] = pt_q[1]
#         pt_q[1] = (pt_q[1][0] + (verts[j][0] - pt_q[1][0]) / zoom,
#                    pt_q[1][1] + (verts[j][1] - pt_q[1][1]) / zoom)
#         if (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 > r ** 2:
#             i -= 1
#             pt_q[1] = pt_q[0]
#             continue
#         draw_pt(pt_q[1])
#
#
# def ic_nflake(n, r):
#     vertices = get_reg_poly_vertices(n)
#     ic_basic(vertices, 3 / n + 1, r)
#
#
# def ic_perfect_nflake(n):
#     ic_nflake(n, size / 2.75)
#
#
# def ic_carpet():
#     vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
#                 (bd + size / 2, bd), (bd + size / 2, bd + size),
#                 (bd, bd + size / 2), (bd + size, bd + size / 2))
#     ic_basic(vertices, 1.5, size / 2.333)
#
#
# def ic_vicsek():
#     vertices = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size),
#                 (w / 2, h / 2))
#     ic_basic(vertices, 1.5, size / 2)
#
#
# def ic_avoid_center(r_i, zoom, r_o):
#     verts = ((bd, bd), (bd + size, bd), (bd, bd + size), (bd + size, bd + size))
#     pt_q = [verts[0], verts[0]]
#
#     for i in range(1, points + 1):
#         j = int(random() * 4)
#         pt_q[0] = pt_q[1]
#         pt_q[1] = (pt_q[1][0] + (verts[j][0] - pt_q[1][0]) / zoom,
#                    pt_q[1][1] + (verts[j][1] - pt_q[1][1]) / zoom)
#
#         if (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 < r_i ** 2 or \
#               (pt_q[1][0] - w / 2) ** 2 + (pt_q[1][1] - h / 2) ** 2 > r_o ** 2:
#             i -= 1
#             pt_q[1] = pt_q[0]
#             continue
#         draw_pt(pt_q[1])
#
