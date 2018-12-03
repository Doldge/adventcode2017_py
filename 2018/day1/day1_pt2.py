#!/usr/bin/env python3

# Read the inputs
input_list = []
with open('./advent_2018_day_1_pt1_input.txt') as f:
    input_list = [int(x) for x in f.readlines()]


def find_dup_freq(current_value, seen):
    for x in input_list:
        current_value += x
        if current_value in seen:
            break
        seen.add(current_value)
    else:
        current_value = find_dup_freq(current_value, seen)
    return current_value


# Initialization.
current_frequency = 0
set_of_seen_frequencies = set([current_frequency])

current_frequency = find_dup_freq(current_frequency, set_of_seen_frequencies)

print(current_frequency)
