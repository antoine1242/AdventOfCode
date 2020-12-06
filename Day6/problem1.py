def problem1():
	with open("input1.txt") as f:
	    content = f.readlines()
	lines = [x.strip() for x in content]

	groups = [""]
	index = 0

	for line in lines:
		if line == "":
			groups.append("")
			index += 1
			
		else:
			groups[index] = groups[index] + line
			

	total = 0
	
	for group in groups:
		letters = []
		for letter in group:
			if letter not in letters:
				letters.append(letter)
				total += 1

	return total

print(problem1())
