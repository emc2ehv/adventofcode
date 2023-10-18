# Doesn't He Have Intern-Elves For This?
# https://adventofcode.com/2015/day/5

with open("2015/5.input", "r") as f:
    nice_string_count = 0
    for line in f:
        vowels = "aeiou"
        vowelCount = 0
        disallowed_check = False
        double_letter_check = False
        a_string = line.strip()
        if (
            ("ab" not in a_string)
            and ("cd" not in a_string)
            and ("pq" not in a_string)
            and ("xy" not in a_string)
        ):
            disallowed_check = True
        else:
            continue
        last_letter = ""
        for i, c in enumerate(a_string):
            if vowelCount > 2 and double_letter_check:
                break
            if c in vowels:
                vowelCount += 1
            if (not double_letter_check) and i > 0 and (last_letter == c):
                double_letter_check = True
            elif not double_letter_check:
                last_letter = c

        if (vowelCount > 2) and disallowed_check and double_letter_check:
            nice_string_count += 1
    print(nice_string_count)
