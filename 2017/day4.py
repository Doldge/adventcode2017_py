#!/usr/bin/env python3

# Day 4.

myInput = []
with open('day4.txt') as f:
    line = f.readline()
    line = line.strip()
    line = line.split(' ')
    myInput.append(line)

# Part 1.
valid_count = 0
for line in myInput:
    set_of_words = set(line)
    if len(set_of_words) == len(line):
        valid_count += 1
print(valid_count)

# Part 2.
valid_count = 0
for line in myInput:
    contains_anagram = False
    for i, word in enumerate(line):
        j = i + 1
        while j < (len(line)):
            if sorted(list(word)) == sorted(list(line[j])):
                contains_anagram = True
                break
            j += 1
        if contains_anagram:  # we've already failed.
            break
    if not contains_anagram:
        valid_count += 1
print(valid_count)
