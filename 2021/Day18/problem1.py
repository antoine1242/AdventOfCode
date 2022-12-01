from ast import literal_eval

def add_left(line, i, number):
	has_1_more_digit = False
	has_2_digits = False

	for j in range(i-1, 1, -1):
		if line[j].isdigit():
			left_number = line[j]

			if line[j-1].isdigit():
				left_number = line[j-1] + left_number
				has_2_digits = True
				
			addition = int(number) + int(left_number)

			if len(str(addition)) > len(left_number):
				has_1_more_digit = True 

			if has_1_more_digit:
				return line[:]


def reduce(line):
	reduced = False
	depth = 0

	for i in range(1, len(line)-1):
		curr_char = line[i]
		if curr_char == "[":
			depth += 1
		elif curr_char == "]":
			depth -= 1
		elif curr_char.isdigit() and depth >= 4:
			curr_number = curr_char
			if line[i+1].isdigit():
				curr_char += line[i+1]
			
			line = add_left(line, i, number)


	#if depth == 4 and isinstance(pair.left, int) and isinstance(pair.left, int):


	#return reduced, pair

def problem1():
	with open("Day18/input1.txt") as f:
	    lines = f.read().splitlines() 

	lines = [literal_eval(line) for line in lines]

	for line in lines:
		reduced = True

		while reduced:
			reduced = False
			pair, reduced = reduce(pair)

	return lines[0]
	
print(problem1())