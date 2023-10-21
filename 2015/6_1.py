# Probably a Fire Hazard
# https://adventofcode.com/2015/day/6

import numpy as np
from utils import timeit

light_grid = np.zeros((1000, 1000), dtype=int)


def turn_on(left_corner, right_corner):
    light_grid[
        left_corner[0] : right_corner[0] + 1, left_corner[1] : right_corner[1] + 1
    ] |= 1


def turn_off(left_corner, right_corner):
    light_grid[
        left_corner[0] : right_corner[0] + 1, left_corner[1] : right_corner[1] + 1
    ] &= 0


def toggle(left_corner, right_corner):
    light_grid[
        left_corner[0] : right_corner[0] + 1, left_corner[1] : right_corner[1] + 1
    ] = (
        1
        - light_grid[
            left_corner[0] : right_corner[0] + 1, left_corner[1] : right_corner[1] + 1
        ]
    )


@timeit
def main():
    with open("2015/6.input", "r") as f:
        for line in f:
            instructions = line.strip().split(" ")
            right_corner = [eval(x) for x in instructions[-1].split(",")]
            left_corner = [eval(x) for x in instructions[-3].split(",")]
            if instructions[0] == "turn":
                if instructions[1] == "on":
                    turn_on(left_corner, right_corner)
                else:
                    turn_off(left_corner, right_corner)
            else:
                toggle(left_corner, right_corner)

    print(light_grid.sum())


if __name__ == "__main__":
    main()
