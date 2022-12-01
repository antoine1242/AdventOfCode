import numpy as np

def get_min_neighbor(i, j, prog_dyn):
	min = 10000
	for m in range(i-1, i+2):
		for n in range(j-1, j+2):
			if m >= 0 and m < prog_dyn.shape[0] and n >=0 and n < prog_dyn.shape[1]:
				if not (m == i and n == j or m != i and n != j):
					if prog_dyn[m,n] < min:
						min = prog_dyn[m,n]

	return min


def problem1():
	with open("Day15/input1.txt") as f:
	    lines = f.read().splitlines() 
	lines = [line for line in lines]

	risk_levels = []
	for i in range(len(lines)):
		risk_level = []
		for j in range(len(lines[0])):
			risk_level.append(int(lines[i][j]))
		risk_levels.append(risk_level)
	
	risk_levels = np.matrix(risk_levels)

	prog_dyn = np.zeros((len(lines), len(lines[0])))

	for i in range(risk_levels.shape[0]):
		for j in range(risk_levels.shape[1]):
			if i == 0 and j == 0:
				prog_dyn[i,j] = risk_levels[i,j]
			
			elif i == 0:
				prog_dyn[i,j] = risk_levels[i,j] + prog_dyn[i,j-1]
			
			elif j == 0:
				prog_dyn[i,j] = risk_levels[i,j] + prog_dyn[i-1,j]

	for i in range(1, risk_levels.shape[0]):
		for j in range(1, risk_levels.shape[1]):
			prog_dyn[i,j] = risk_levels[i,j] + min(prog_dyn[i-1,j], prog_dyn[i, j-1])

	has_changed = True
	while(has_changed):
		has_changed = False

		for i in range(prog_dyn.shape[0]):
			for j in range(prog_dyn.shape[1]):
				min_neighbor = get_min_neighbor(i,j, prog_dyn)
				if risk_levels[i,j] + min_neighbor < prog_dyn[i,j]:
					prog_dyn[i,j] = risk_levels[i,j] + min_neighbor
					has_changed = True

	return prog_dyn
	
print(problem1())