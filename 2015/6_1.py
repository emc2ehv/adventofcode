# Probably a Fire Hazard
# https://adventofcode.com/2015/day/6

import numpy as np

light_grid = np.zeros((1000, 1000), dtype=int)


def turn_on(i, j):
    light_grid[i][j] |= 1


def turn_off(i, j):
    light_grid[i][j] &= 0


def toggle(i, j):
    if light_grid[i][j] == 0:
        light_grid[i][j] = 1
    else:
        light_grid[i][j] = 0


def update_light_grid(left_corner, right_corner, action):
    for i in range(left_corner[0], right_corner[0] + 1):
        for j in range(left_corner[1], right_corner[1] + 1):
            action(i, j)


with open("2015/6.input", "r") as f:
    for line in f:
        instructions = line.strip().split(" ")
        right_corner = [eval(x) for x in instructions[-1].split(",")]
        left_corner = [eval(x) for x in instructions[-3].split(",")]
        if instructions[0] == "turn":
            if instructions[1] == "on":
                update_light_grid(left_corner, right_corner, turn_on)
            else:
                update_light_grid(left_corner, right_corner, turn_off)
        else:
            update_light_grid(left_corner, right_corner, toggle)

print(light_grid.sum())
