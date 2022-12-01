
def problem1():
	with open("Day8/input1.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines] 

	digits = [x.split("|")[0] for x in lines]
	outputs = [x.split("|")[1] for x in lines]

	outputs = [output.split() for output in outputs]

	sum_of_1478 = 0

	for output in outputs:
		for digit in output:
			if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
				sum_of_1478 += 1

	return sum_of_1478
	
print(problem1())