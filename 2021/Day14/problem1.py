def problem1():
	with open("Day14/input1.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines]

	first_line = lines[0]

	all_lines = lines[2:]

	all_lines = [line.split(" -> ") for line in all_lines]

	for j in range(10):
		new_line = ""
		for i in range(len(first_line)-1):	
			new_line += first_line[i] 

			for line in all_lines:
				if first_line[i] + first_line[i+1] == line[0]:
					new_line += line[1]
					break
		
		first_line = new_line + first_line[-1]

	freq = {}
	for i in first_line:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1
	leastFreq = min(freq, key = freq.get)
	mostFreq = max(freq, key = freq.get)

	return freq[mostFreq] - freq[leastFreq]
	
print(problem1())