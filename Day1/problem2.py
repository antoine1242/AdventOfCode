def problem2():
	with open("input2.txt") as f:
	    numbers = f.readlines()
	numbers = [int(x.strip()) for x in numbers]

	for i in range(0, len(numbers)):
		for j in range(i, len(numbers)):
			for k in range(j, len(numbers)):
				if numbers[i] + numbers[j] + numbers[k] == 2020:
					return numbers[i] * numbers[j] * numbers[k]

print(problem2())