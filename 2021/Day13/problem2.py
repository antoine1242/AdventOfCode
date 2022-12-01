import numpy as np


def problem1():
	with open("Day13/input2.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines]
	
	numbers = [x.split(",") for x in lines if not x.startswith("f")][:-1]

	folds = [x for x in lines if x.startswith("f")]

	folds = [x[11:].split('=') for x in folds]

	x_coordinates = [int(number[0]) for number in numbers]
	y_coordinates = [int(number[1]) for number in numbers]

	grid = []
	for i in range(max(x_coordinates)+1):
		row = []
		for j in range(max(y_coordinates)+1):
			row.append(".")
		grid.append(row)

	for number in numbers:
		grid[int(number[0])][int(number[1])] = "#"


	for fold in folds:
		axis = fold[0]
		row_or_column = int(fold[1])

		if axis == "x":
			grid_split_1 = grid[0:row_or_column]
			grid_split_2 = grid[row_or_column+1:]

			new_grid = []
			for i in range(len(grid_split_1)):
				new_row = []
				for j in range(len(grid_split_1[0])):
					if grid_split_1[i][j] == "#" or grid_split_2[len(grid_split_1)-i-1][j] == "#":
						new_row.append("#")
					else:
						new_row.append(".")
				new_grid.append(new_row)

		else:
			np_grid = np.array(grid)

			grid_split_1 = np_grid[:,0:row_or_column].tolist()
			grid_split_2 = np_grid[:,row_or_column+1:].tolist()

			new_grid = []
			for i in range(len(grid_split_1)):
				new_row = []
				for j in range(len(grid_split_1[0])):
					if grid_split_1[i][j] == "#" or grid_split_2[i][len(grid_split_2[0])-j-1] == "#":
						new_row.append("#")
					else:
						new_row.append(".")
				new_grid.append(new_row)

		grid = new_grid

		for row in np.transpose(np.array(new_grid)).tolist():
			print(repr(row).replace(",", "").replace("'", ""))

	

	return 0
	
print(problem1())