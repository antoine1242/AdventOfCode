def problem1():
	with open("Day7/input1.txt") as f:
	    numbers = f.readline() 

	numbers = [int(x) for x in numbers.split(",")]

	best = 0
	best_sum = 99999999999999
	print(max(numbers))
	for i in range(max(numbers)):
		sum = 0
		for number in numbers:
			sum += abs(number-i)

		if sum < best_sum:
			best_sum = sum
			best = i

	final_sum = 0

	for number in numbers:
		final_sum += abs(number - best)

	return final_sum
	
print(problem1())