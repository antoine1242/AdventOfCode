def get_lowpoints(lines):
	low_points = []

	for i in range(len(lines)):
		for j in range(len(lines[0])):
			if i == 0 and j == 0:
				if lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j+1]:
					low_points.append((i, j))
			
			elif i == 0 and j == len(lines[0]) - 1:
				if lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j-1]:
					low_points.append((i, j))
			
			elif i == 0:
				if lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j-1] and lines[i][j]< lines[i][j+1]:
					low_points.append((i, j))

			elif i == len(lines) - 1:
				if lines[i][j] < lines[i-1][j] and lines[i][j]< lines[i][j-1] and lines[i][j]< lines[i][j+1]:
					low_points.append((i, j))
			
			elif i == len(lines) - 1 and j == 0:
				if lines[i][j] < lines[i-1][j] and lines[i][j]< lines[i][j+1]:
					low_points.append((i, j))

			elif i == len(lines) - 1 and j == len(lines[0]) - 1:
				if lines[i][j] < lines[i-1][j] and lines[i][j]< lines[i][j-1]:
					low_points.append((i, j))

			elif j == 0:
				if lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j+1]:
					low_points.append((i, j))

			elif j == len(lines[0]) - 1:
				if lines[i][j] < lines[i-1][j] and lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i][j-1]:
					low_points.append((i, j))

			else:
				if lines[i][j] < lines[i+1][j] and lines[i][j]< lines[i-1][j] and lines[i][j] < lines[i][j+1] and lines[i][j] < lines[i][j-1]:
					low_points.append((i, j))

	return low_points

def get_basin(current_point, lines, basin_points):
	if current_point in basin_points or lines[current_point[0]][current_point[1]] == '9':
		return basin_points

	basin_points.add(current_point)

	i = current_point[0]
	j = current_point[1]

	if i + 1 != len(lines):
		get_basin((i+1, j), lines, basin_points)

	if i - 1 >= 0:
		get_basin((i-1, j), lines, basin_points)

	if j + 1 != len(lines[0]):
		get_basin((i, j+1), lines, basin_points)

	if j - 1 >= 0:
		get_basin((i, j-1), lines, basin_points)
	
	return basin_points	
	
def problem2():
	with open("Day9/input2.txt") as f:
	    lines = f.read().splitlines()

	low_points = get_lowpoints(lines)

	sizes = []

	for low_point in low_points:
		basin_points = get_basin(low_point, lines, set())
		basin_points = [t for t in (set(tuple(i) for i in basin_points))]
		sizes.append(len(basin_points))


	sizes.sort(reverse=True)

	return sizes[0] * sizes[1] * sizes[2]

print(problem2())