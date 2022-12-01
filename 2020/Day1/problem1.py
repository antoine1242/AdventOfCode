def problem1():
	with open("input1.txt") as f:
	    numbers = f.readlines()
	numbers = [int(x.strip()) for x in numbers]

	for i in range(0, len(numbers)):
		for j in range(i, len(numbers)):
			if numbers[i] + numbers[j] == 2020:
				return numbers[i] * numbers[j]

print(problem1())