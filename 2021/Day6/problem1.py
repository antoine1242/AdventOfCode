import copy

def problem1():
	with open("Day6/input1.txt") as f:
	    numbers = f.readline() 

	numbers = [int(x) for x in numbers.split(",")]

	for i in range(80):
		curr_numbers = copy.deepcopy(numbers)

		for index, number in enumerate(curr_numbers):
			if number == 0:
				numbers[index] = 6
				numbers.append(8)
			else:
				numbers[index] = numbers[index] - 1

	return len(numbers)
	
print(problem1())