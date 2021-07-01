"""
Created on: 2021-06-30

@author: Gabriel C.
"""

from vpython import *
import numpy as np
import timeit


def elastic_force(r) -> np.array:
    k, m = 10, 1
    x = r[0]
    Vx = r[1]

    dx = Vx
    dVx = -k * x/m

    return np.array([dx, dVx], float)


def rk4(r: np.array, h: float) -> float:
    k1 = h * elastic_force(r)
    k2 = h * elastic_force(r + 0.5 * k1)
    k3 = h * elastic_force(r + 0.5 * k2)
    k4 = h * elastic_force(r + k3)

    return (k1 + 2*(k2 + k3) + k4)/6



"""

Creating Support:

"""


def create_support() -> [box, box]:
    wall = box(pos=vector(-4.8, 0, 0), size=vector(0.4, 4, 2.5), texture=textures.wood)  # Create Wall command
    table = box(pos=vector(0, -2, 0), size=vector(10, 0.4, 2.5), texture=textures.wood)  # Create Table command

    return wall, table


"""

Set Background:

"""


def set_background() -> canvas:
    background = canvas(background=color.purple, width=1400)

    return background


"""

Creating a spiral spring:

"""


def create_spiral():
    spiral = helix(pos=vector(-4.8, -1.3, 0), axis=vector(3.5, 0, 0), radius=0.4, coils=8, color=color.gray(luminance=0))
    return spiral


"""

Creating the box:

"""


def create_box() -> box:
    my_box = box(pos=vector(-0.7, -1.3, 0), size=vector(1, 1, 1), color=vector(0.543, 0.965, 0.898))
    return my_box



"""

Creating a jot

"""


def create_jot():
    jot = cylinder(pos=vector(-1.3, -1.3, 0), axis=vector(0, 0, 0.4), radius=0.02, color=color.gray(luminance=0))
    return jot


def create_line():
    line = cylinder(pos=vector(-1.3, -1.3, 0), axis=vector(0.2, 0, 0), radius=0.02, color=color.gray(luminance=0))
    return line


def main():
    start = timeit.default_timer()
    background = set_background()
    wall, table = create_support()
    spiral = create_spiral()
    line = create_line()
    jot = create_jot()
    my_box = create_box()

    v0 = 40.0
    if v0 > 70.0:
        print('Max velocity is 70, setting to 70')
        v0 = 70.0
    print(f'Velocity: {v0}')

    r = np.array([0, v0])
    h = 0.05

    while True:

        rate(25)  # our fps
        dr = rk4(r, h)
        r += dr

        spiral.axis = vector(3.5 + dr[0], 0, 0)
        jot.pos = vector(-1.3 + dr[0], -1.3, 0)
        line.pos = vector(-1.3 + dr[0], -1.3, 0)
        my_box.pos = vector(-0.7 + dr[0], -1.3, 0)


if __name__ == '__main__':
    main()


