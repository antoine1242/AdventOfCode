def find_oxygen(binaries, curr_idx):	
	zeros = 0
	ones = 0

	for i in range(len(binaries)):
		if binaries[i][curr_idx] == '0':
			zeros += 1
		else:
			ones += 1

	kept = []
	for i in range(len(binaries)):
		if ones > zeros or zeros == ones:
			if binaries[i][curr_idx] == '1':
				kept.append(binaries[i]) 
		else:
			if binaries[i][curr_idx] == '0':
				kept.append(binaries[i])

	if len(kept) == 1:
		return kept[0]
	else:
		return find_oxygen(kept, curr_idx+1)

def find_co2(binaries, curr_idx):	
	zeros = 0
	ones = 0

	for i in range(len(binaries)):
		if binaries[i][curr_idx] == '0':
			zeros += 1
		else:
			ones += 1

	kept = []
	for i in range(len(binaries)):
		if zeros < ones or zeros == ones:
			if binaries[i][curr_idx] == '0':
				kept.append(binaries[i]) 
		else:
			if binaries[i][curr_idx] == '1':
				kept.append(binaries[i])

	if len(kept) == 1:
		return kept[0]
	else:
		return find_co2(kept, curr_idx+1)

def problem2():
	with open("Day3/input2.txt") as f:
	    lines = f.read().splitlines() 
	binaries = [x.strip("") for x in lines]

	oxygen = find_oxygen(binaries, 0)
	co2 = find_co2(binaries, 0)

	oxygen = int(''.join(oxygen), 2)
	co2 = int(''.join(co2), 2)

	return oxygen * co2
	
print(problem2())