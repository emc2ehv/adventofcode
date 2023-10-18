# Doesn't He Have Intern-Elves For This?
# https://adventofcode.com/2015/day/5

with open("2015/5.input", "r") as f:
    nice_string_count = 0
    for line in f:
        pattern1_check = False
        pattern2_check = False
        a_string = line.strip()
        str_len = len(a_string)
        for i, c in enumerate(a_string):
            if pattern1_check and pattern2_check:
                nice_string_count += 1
                break
            if i > 1 and i < str_len - 1:
                if a_string[i : i + 2] in a_string[0:i]:
                    pattern1_check = True
                if a_string[i + 1] == a_string[i - 1]:
                    pattern2_check = True

    print(nice_string_count)
