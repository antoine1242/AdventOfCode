def problem1():
	with open("Day3/input1.txt") as f:
	    lines = f.read().splitlines() 
	binaries = [x.strip("") for x in lines]

	most_common = []
	least_common = []
	
	for i in range(len(binaries[0])):
		zeros = 0
		ones = 0
		for j in range(len(binaries)):
			if binaries[j][i] == '0':
				zeros += 1
			else:
				ones += 1
		if ones > zeros:
			most_common.append('1')
			least_common.append('0')
		else:
			most_common.append('0')
			least_common.append('1')

	gamma = int(''.join(most_common), 2)
	epsilon = int(''.join(least_common), 2)

	return gamma * epsilon
	
print(problem1())