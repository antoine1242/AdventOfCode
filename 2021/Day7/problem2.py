def problem2():
	with open("Day7/input2.txt") as f:
	    numbers = f.readline() 

	numbers = [int(x) for x in numbers.split(",")]

	best = 0
	best_sum = 99999999999999

	for i in range(max(numbers)):
		sum = 0

		for number in numbers:
			sum += (abs(number-i) * (abs(number-i) + 1)) / 2

		if sum < best_sum:
			best_sum = sum
			best = i

	final_sum = 0

	for number in numbers:
		final_sum += (abs(number-best) * (abs(number-best) + 1)) / 2

	return final_sum
	
print(problem2())