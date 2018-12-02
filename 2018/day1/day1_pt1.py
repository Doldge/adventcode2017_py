#!/usr/bin/env python3

answer = None
with open('./advent_2017_day_1_pt1_input.txt') as f:
    answer = sum([int(x) for x in f.readlines()])

print(answer)
