import numpy as np

def problem2():
	with open("Day5/input1.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines]

	splited_lines = [line.split(" -> ") for line in lines]

	splited_lines_coordinates = []

	for line in splited_lines:
		new_line = []
		for coordinates in line:
			curr_coordinates = coordinates.split(",")
			new_line.append((int(curr_coordinates[0]), int(curr_coordinates[1])))
		splited_lines_coordinates.append(new_line)
	
	h_v_lines = []
	diag_lines = []
	for line in splited_lines_coordinates:
		if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
			diag_lines.append(line)
		else:
			h_v_lines.append(line)

	board = np.zeros((1000,1000))
	
	for line in h_v_lines:
		# si ligne verticale
		if line[0][0] == line[1][0]:
			for i in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1):
				board[line[0][0], i] += 1
		# si ligne horizontale
		else:
			for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1):
				board[i, line[0][1]] += 1
	
	for line in diag_lines:
		if line[0][0] < line[1][0] and line[0][1] < line[1][1]:
			i = line[0][0]
			j = line[0][1]
			total = abs(line[0][0] - line[1][0])
			while total >= 0:
				board[i, j] += 1
				i += 1
				j += 1
				total -= 1
		
		elif line[0][0] > line[1][0] and line[0][1] > line[1][1]:
			i = line[0][0]
			j = line[0][1]
			total = abs(line[0][0] - line[1][0])
			while total >= 0:
				board[i, j] += 1
				i -= 1
				j -= 1
				total -= 1

		elif line[0][0] < line[1][0] and line[0][1] > line[1][1]:
			i = line[0][0]
			j = line[0][1]
			total = abs(line[0][0] - line[1][0])
			while total >= 0:
				board[i, j] += 1
				i += 1
				j -= 1
				
				total -= 1

		elif line[0][0] > line[1][0] and line[0][1] < line[1][1]:
			i = line[0][0]
			j = line[0][1]
			total = abs(line[0][0] - line[1][0])
			while total >= 0:
				board[i, j] += 1
				i -= 1
				j += 1
				total -= 1
	board = board.T
	occurrences_more_than_1 = board > 1

	return occurrences_more_than_1.sum()
	
print(problem2())