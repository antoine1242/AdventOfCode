import numpy as np


def problem1():
	with open("Day13/input1.txt") as f:
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

	fold = folds[0]
	axis = fold[0]
	row = int(fold[1])

	grid_split_1 = grid[0:row]
	grid_split_2 = grid[row+1:]

	new_grid = []
	dots=0
	for i in range(len(grid_split_1)):
		new_row = []
		for j in range(len(grid_split_1[0])):
			if grid_split_1[i][j] == "#" or grid_split_2[len(grid_split_1)-i-1][j] == "#":
				new_row.append("#")
				dots += 1
			else:
				new_row.append(".")
		new_grid.append(new_row)

	return dots
	
print(problem1())