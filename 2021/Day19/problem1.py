def problem1():
	with open("Day19/input1.txt") as f:
	    lines = f.read().splitlines()

	scanners = []

	i = 0

	curr_scan = []
	while i < len(lines):
		if 'scanner' in lines[i] and len(curr_scan) > 0:
			scanners.append(curr_scan)
			curr_scan = []
		elif len(lines[i]) > 0:
			curr_scan.append(lines[i])

	return scanners
	
print(problem1())