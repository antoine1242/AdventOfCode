def problem1():
	with open("input1.txt") as f:
	    numbers = f.readlines()
	numbers = [int(x.strip()) for x in numbers]

	count = 0

	for i in range(0, len(numbers)-1):
		if numbers[i+1] > numbers[i]:
			count += 1
	return count
	
print(problem1())