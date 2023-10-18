def getFeet(dims):
    dims = [eval(x) for x in dims]
    dims.sort()
    ribbonFeet = dims[0] * dims[1] * dims[2]
    smallestPerimiter = 2 * (dims[0] + dims[1])
    return ribbonFeet + smallestPerimiter


with open("2015/2.input", "r") as f:
    totalFeet = 0
    for line in f:
        totalFeet += getFeet(line.strip().split("x"))
print(totalFeet)
