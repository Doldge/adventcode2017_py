#!/usr/bin/env python3

# Day 4.

myInput = []
with open('day4.txt') as f:
    myInput = f.readlines()

# Part 1.
valid_count = 0
for line in myInput:
    line = line.strip()
    words = line.split(' ')
    set_of_words = set(words)
    if len(set_of_words) == len(words):
        valid_count += 1
print(valid_count)

# Part 2.
valid_count = 0
for line in myInput:
    line = line.strip()
    words = line.split(' ')
    contains_anagram = False
    for i, word in enumerate(words):
        j = i + 1
        while j < (len(words)):
            if sorted(list(word)) == sorted(list(words[j])):
                contains_anagram = True
                break
            j += 1
        if contains_anagram:  # we've already failed.
            break
    if not contains_anagram:
        valid_count += 1
print(valid_count)
