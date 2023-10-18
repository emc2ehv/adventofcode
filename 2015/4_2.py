# The Ideal Stocking Stuffer
# https://adventofcode.com/2015/day/4

import hashlib

key = "ckczppom"

result = 0

while True:
    input = f"{key}{result}"
    if hashlib.md5(input.encode()).hexdigest()[0:6] == "000000":
        break
    result += 1

print(result)
