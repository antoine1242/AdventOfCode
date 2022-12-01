import copy

def read_pixel(i, j, grid):
	binary_string = ""

	for n in range(i-1, i+2):
		for m in range(j-1, j+2):
			if n < 0 or m < 0 or n >= len(grid) or m >= len(grid[0]):
				binary_string += "."
			else:
				binary_string += grid[n][m]

	binary_ints = ""

	for char in binary_string:
		if char == ".":
			binary_ints += '0'
		else:
			binary_ints += '1'

	return int(binary_ints, 2)

def apply_algorithm(padded_grid, algorithm, grid):
	new_grid = copy.deepcopy(padded_grid)

	for i in range(len(new_grid)):
		for j in range(len(new_grid[0])):
			temp_list = list(new_grid[i])
			temp_list[j] = algorithm[read_pixel(i, j, padded_grid)]
			new_grid[i] = "".join(temp_list)

	return new_grid

def build_padded_grid(grid):
    dots_string = "".join(["." for i in range(len(grid[0]) + 300)])
    half_dots = "".join(["." for i in range(150)])

    padded_grid = []

    for i in range(150):
    	padded_grid.append(dots_string)

    for line in grid:
    	padded_grid.append(half_dots + line + half_dots)

    for i in range(150):
    	padded_grid.append(dots_string)

    return padded_grid

def problem1():
	with open("Day20/input2.txt") as f:
	    lines = f.read().splitlines() 

	algorithm = lines[0]

	grid = lines[2:]

	padded_grid = build_padded_grid(grid)

	for i in range(2):
		padded_grid = apply_algorithm(padded_grid, algorithm, grid)
		if i % 2 == 1:
			padded_grid[0] = "".join(["." for i in range(len(grid[0]) + 300)])
			padded_grid[-1] = "".join(["." for i in range(len(grid[0]) + 300)])

	lit_pixels = 0

	for i in range(len(padded_grid)):
		for j in range(len(padded_grid[0])):
			if padded_grid[i][j] == "#":
				lit_pixels += 1

	return lit_pixels
	
print(problem1())