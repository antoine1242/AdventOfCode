def problem1():
	with open("Day9/input1.txt") as f:
	    lines = f.read().splitlines()

	sum = 0

	for i in range(len(lines)):
		for j in range(len(lines[0])):
			if i == 0 and j == 0:
				if lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j+1]:
					sum += int(lines[i][j]) + 1
			
			elif i == 0 and j == len(lines[0]) - 1:
				if lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j-1]:
					sum += int(lines[i][j]) + 1
			
			elif i == 0:
				if lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j-1] and lines[i][j]< lines[i][j+1]:
					sum += int(lines[i][j]) + 1

			elif i == len(lines) - 1:
				if lines[i][j] < lines[i-1][j] and lines[i][j]< lines[i][j-1] and lines[i][j]< lines[i][j+1]:
					sum += int(lines[i][j]) + 1
			
			elif i == len(lines) - 1 and j == 0:
				if lines[i][j] < lines[i-1][j] and lines[i][j]< lines[i][j+1]:
					sum += int(lines[i][j]) + 1

			elif i == len(lines) - 1 and j == len(lines[0]) - 1:
				if lines[i][j] < lines[i-1][j] and lines[i][j]< lines[i][j-1]:
					sum += int(lines[i][j]) + 1

			elif j == 0:
				if lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j+1]:
					sum += int(lines[i][j]) + 1

			elif j == len(lines[0]) - 1:
				if lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j-1]:
					sum += int(lines[i][j]) + 1

			else:
				if lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i-1][j] and lines[i][j] < lines[i][j+1] and lines[i][j] < lines[i][j-1]:
					sum += int(lines[i][j]) + 1

	return sum
	
print(problem1())