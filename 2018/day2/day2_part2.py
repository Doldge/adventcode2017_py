#!/usr/bin/env python3


# Read Input
with open('./day2_input.txt') as f:
    input_list = f.readlines()


# Our Lines
for i, line in enumerate(input_list):
	# Comparison Lines, ignore lines we've already compared against.
	for comp_line in input_list[i+1:]:
		diff = len(line)
		for char_index, char in enumerate(comp_line):
			if line[char_index] == comp_line[char_index]:
				diff = (diff - 1)
		if diff == 1:
			# these are our fabric boxes
			# print the diff and then exit
			output_string = ''
			for char_index, char in enumerate(comp_line):
				output_string += (
					char if char == line[char_index]
					else ''
				)
			print(output_string)
