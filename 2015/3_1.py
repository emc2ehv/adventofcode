with open("2015/3.input", "r") as f:
    line = f.readline()
    homes = set()
    x = 0
    y = 0
    homes.add((x, y))

    for dir in line:
        if dir == "^":
            y += 1
        elif dir == "v":
            y -= 1
        elif dir == ">":
            x += 1
        else:
            x -= 1
        homes.add((x, y))
    print(len(homes))
