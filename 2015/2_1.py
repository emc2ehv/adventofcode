def getArea(dims):
    dims = [eval(x) for x in dims]
    l = dims[0]
    w = dims[1]
    h = dims[2]
    area1 = 2 * l * w
    area2 = 2 * w * h
    area3 = 2 * h * l
    minArea = min(area1, area2, area3) / 2
    area = area1 + area2 + area3
    return minArea + area


with open("2015/2.input", "r") as f:
    totalArea = 0
    for line in f:
        totalArea += getArea(line.strip().split("x"))
print(totalArea)
