def is_in_grid(i,j):
	if i >= 0 and i < 10 and j >= 0 and j < 10:
		return True
	
	return False

def problem1():
	with open("Day11/input1.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines]

	octopuses = []
	
	for line in lines:
		curr_line = []
		for char in line:
			curr_line.append(int(char))
		
		octopuses.append(curr_line)

	flashes = 0

	for k in range(100):
		flashed = set()
		incremented = set()

		has_flashed = True

		while has_flashed == True:
			has_flashed = False

			for i in range(len(octopuses)):
				for j in range(len(octopuses[0])):
					if (i,j) not in incremented:
						octopuses[i][j] += 1
						incremented.add((i,j))

					if octopuses[i][j] >= 10 and (i,j) not in flashed:
						flashes += 1
						flashed.add((i,j))
						has_flashed = True

						for m in range(i-1, i+2):
							for n in range(j-1, j+2):
								if m == i and n == j:
									continue

								if is_in_grid(m, n):
									octopuses[m][n] += 1


		for i in range(len(octopuses)):
			for j in range(len(octopuses[0])):
				if octopuses[i][j] >= 10:
					octopuses[i][j] = 0
			
	return flashes
	
print(problem1())