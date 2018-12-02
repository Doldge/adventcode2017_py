#!/usr/bin/env python3

# Day 2
# Setup input as list of list of ints.
lines = []
with open('day2.txt') as f:
    for line in f.readlines():
        lines.append(list(map(int, line.split('\t'))))


# Part 1
check_sum = 0
for line in lines:
    check_sum += (max(line) - min(line))
print(check_sum)

# Part 2
div_sum = 0
for line in lines:
    numerator, denominator = 0, 1  # init values picked to avoid div-by-zero
    for i, num in enumerate(line):
        j = (i + 1)
        while j < len(line):
            if num % line[j] == 0:
                numerator, denominator = num, line[j]
                break
            elif line[j] % num == 0:
                numerator, denominator = line[j], num
                break
            j += 1
        if numerator and denominator:
            break
    # / gives you a float, // gives you an int
    div_sum += numerator // denominator

print(div_sum)
