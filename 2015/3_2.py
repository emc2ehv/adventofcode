def moveSanta(dir, x, y):
    if dir == "^":
        y += 1
    elif dir == "v":
        y -= 1
    elif dir == ">":
        x += 1
    else:
        x -= 1
    return x, y


with open("2015/3.input", "r") as f:
    line = f.readline()
    homes = set()
    xSanta = 0
    ySanta = 0
    xRoboSanta = 0
    yRoboSanta = 0

    homes.add((xSanta, ySanta))
    homes.add((xRoboSanta, yRoboSanta))

    for c, dir in enumerate(line):
        if c % 2 == 0:
            xSanta, ySanta = moveSanta(dir, xSanta, ySanta)
            homes.add((xSanta, ySanta))
        else:
            xRoboSanta, yRoboSanta = moveSanta(dir, xRoboSanta, yRoboSanta)
            homes.add((xRoboSanta, yRoboSanta))
    print(len(homes))
