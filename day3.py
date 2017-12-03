#!/usr/bin/env python3
import math

# Part 1
# We need to find the position of our square in it's row,
# and then we need to find the shortest path from that position to the center
# of our memory map.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18 5  4  3  12 29
#40 19 6  1  2  11 28
#41 20 7  8  9  10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

# The square of the square root gets you the highest number in a memory square.
# The memory square's position relative to the 1 is based on the square root of
# the highest number in the square.

myInput = 325489


def calc_distance_to_center(input_value):
    # Length of the side of the squarei
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
    # The position of our number, relative to the bottom right corner of the
    # square.
    # FIXME FIXME FIXME - This is wrong.
    distance_from_end = divmod((last_value+cycle+1 - input_value), sqr_len)
    print('distance_from_end: {}'.format(distance_from_end))
    position_relative_to_middle = cycle + (sqr_len // 2) - distance_from_end[1]
    print('position from middle: {}'.format(position_relative_to_middle))
    print('*'*8+'\n')
    return position_relative_to_middle


calc_distance_to_center(1)
calc_distance_to_center(4)
calc_distance_to_center(12)
calc_distance_to_center(23)
calc_distance_to_center(49)
calc_distance_to_center(1024)
