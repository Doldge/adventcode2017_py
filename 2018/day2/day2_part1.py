#!/usr/bin/env python3


# Read Input
with open('./day2_input.txt') as f:
    input_list = f.readlines()


# Part 1.
twos_count = 0
threes_count = 0

for line in input_list:
	line_count = {}
	twos_counted = False
	threes_counted = False

	for character in line:
		line_count[character] = line.count(character)

	for character in line_count:
		if line_count[character] == 2 and not twos_counted:
			twos_count += 1
			twos_counted = True
		elif line_count[character] == 3 and not threes_counted:
			threes_count += 1
			threes_counted = True

print('{} * {}'.format(twos_count, threes_count))
print(twos_count * threes_count)
