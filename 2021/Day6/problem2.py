def problem2():
	with open("Day6/input2.txt") as f:
	    numbers = f.readline() 

	numbers = [int(x) for x in numbers.split(",")]

	numbers_dict = {}

	for number in numbers:
		if str(number) in numbers_dict:
			numbers_dict[str(number)] += 1
		else:
			numbers_dict[str(number)] = 1

	for i in range(256):
		temp_dict = {}
		
		for j in range(9):

			if j == 0:
				
				if str(j) in numbers_dict:
					temp_dict["6"] = numbers_dict[str(j)]
					temp_dict["8"] = numbers_dict[str(j)]
				else: 
					temp_dict["8"] = 0
			
			elif j == 7:
				if str(j) in numbers_dict:
					temp_dict["6"] += numbers_dict[str(j)]
				else: 
					temp_dict["6"] = 0
			else:
				if str(j) in numbers_dict:
					temp_dict[str(j-1)] = numbers_dict[str(j)]
				else: 
					temp_dict[str(j-1)] = 0

		numbers_dict = temp_dict

	sum = 0		
	for key, value in numbers_dict.items():
		sum += value

	return sum
	
print(problem2())