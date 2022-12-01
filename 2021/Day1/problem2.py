def problem2():
	with open("input1.txt") as f:
	    numbers = f.readlines()
	numbers = [int(x.strip()) for x in numbers]

	count = 0

	for i in range(0, len(numbers)-3):
		if numbers[i+1] + numbers[i+2] + numbers[i+3] > numbers [i] + numbers[i+1] + numbers[i+2]:
			count += 1
	return count
	
print(problem2())