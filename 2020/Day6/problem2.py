def problem2():
	with open("input2.txt") as f:
	    content = f.readlines()
	lines = [x.strip() for x in content]

	groups = [""]
	groups_len = []
	index = 0
	group_len = 0

	for line in lines:
		if line == "":
			groups.append("")
			index += 1
			groups_len.append(group_len)
			group_len = 0
			
		else:
			groups[index] = groups[index] + line
			group_len += 1

	groups_len.append(group_len)

	total = 0
	

	for index, group in enumerate(groups):
		letters = dict.fromkeys([])
		for letter in group:
			if letter not in letters.keys():
				letters[letter] = 1
			else:
				letters[letter] += 1
		
		for key, value in letters.items():
			if value == groups_len[index]:
				total += 1

	return total

print(problem2())
