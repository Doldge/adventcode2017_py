#!/usr/bin/env python3
import math

# Part 1
# We need to find the position of our square in it's row,
# and then we need to find the shortest path from that position to the center
# of our memory map.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18 5  4  3  12 29
# 40 19 6  1  2  11 28
# 41 20 7  8  9  10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# The square of the square root gets you the highest number in a memory square.
# The memory square's position relative to the 1 is based on the square root of
# the highest number in the square.

myInput = 325489


# Part 1.
def calc_distance_to_center(input_value):
    # Length of the side of the square
    print('*'*8)
    print('Input: {}'.format(input_value))
    sqr_len = math.ceil(math.sqrt(input_value))
    sqr_len = sqr_len if sqr_len % 2 != 0 else sqr_len + 1
    # bottom right corner of our square
    last_value = math.pow(sqr_len, 2)
    print('Square Corner:{}'.format(last_value))

    # The squares outter position relative to the center. (how many cycles have
    # we gone).
    cycle = (sqr_len - 1) / 2
    print('Square Cycles: {}'.format(cycle))
    axises = [
        sqr_len**2 - ((sqr_len-1) * i) - math.floor(sqr_len/2)
        for i in range(0, 4)
    ]  # get the axis "cells"
    steps_to_reach_axix_from_input = min([
        abs(axis - input_value) for axis in axises
    ]) + cycle
    print('position from middle: {}'.format(steps_to_reach_axix_from_input))
    print('*'*8+'\n')
    return steps_to_reach_axix_from_input


# Tests
#calc_distance_to_center(1)
#calc_distance_to_center(4)
#calc_distance_to_center(12)
#calc_distance_to_center(23)
#calc_distance_to_center(49)
#calc_distance_to_center(1024)
#calc_distance_to_center(myInput)

# Part 2.
matrix = [[0 for j in range(0, 10000)] for i in range(0, 10000)]
start_pos = (5000, 5000)
cur_pos = start_pos
relative_positions = [(cur_pos[0] + x, cur_pos[1]+y) for x, y in [(tuple(range(-1, 2)), tuple(range(-1, 2)))]]
print(relative_positions)
input('')
i = 1
while i <= myInput:
    matrix[cur_pos[0]][cur_pos[1]] = i
    next_x = abs(cur_pos[0] - start_pos[0])
    next_y = abs(cur_pos[1] - start_pos[1])
    
    i = 0
    for position in relative_positions:
        i += matrix[position[0]][position[1]]
    print(next_value)
    input('')
    # from my current position I need to work out where the next position is.
