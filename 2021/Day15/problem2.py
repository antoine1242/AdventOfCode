import numpy as np
import copy

def get_min_neighbor(i, j, prog_dyn):
	min = 10000
	for m in range(i-1, i+2):
		for n in range(j-1, j+2):
			if m >= 0 and m < prog_dyn.shape[0] and n >=0 and n < prog_dyn.shape[1]:
				if not (m == i and n == j or m != i and n != j):
					if prog_dyn[m,n] < min:
						min = prog_dyn[m,n]

	return min

def add_one(risk_levels, times):
	new_risk_levels = copy.deepcopy(risk_levels)

	for k in range(times):
		for i in range(risk_levels.shape[0]):
			for j in range(risk_levels.shape[1]):
				new_risk_levels[i,j] = (new_risk_levels[i,j] % 9) + 1

	return new_risk_levels

def problem1():
	with open("Day15/input2.txt") as f:
	    lines = f.read().splitlines() 
	lines = [line for line in lines]

	risk_levels = []
	for i in range(len(lines)):
		risk_level = []
		for j in range(len(lines[0])):
			risk_level.append(int(lines[i][j]))
		risk_levels.append(risk_level)

	risk_levels = np.matrix(risk_levels)
	whole_risk_levels = np.zeros((len(lines)*5, len(lines[0])*5))

	for i in range(0,5):
		for j in range(0,5):
			whole_risk_levels[risk_levels.shape[0]*i:risk_levels.shape[0]*i+risk_levels.shape[0] , risk_levels.shape[0]*j:risk_levels.shape[0]*j+risk_levels.shape[0]] = add_one(risk_levels, i+j)

	risk_levels = whole_risk_levels

	prog_dyn = np.zeros((len(lines)*5, len(lines[0])*5))

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
	changes = 0
	while(has_changed):
		has_changed = False

		for i in range(prog_dyn.shape[0]):
			for j in range(prog_dyn.shape[1]):
				min_neighbor = get_min_neighbor(i,j, prog_dyn)
				if risk_levels[i,j] + min_neighbor < prog_dyn[i,j]:
					prog_dyn[i,j] = risk_levels[i,j] + min_neighbor
					has_changed = True
					changes += 1
		print(changes)			
		changes = 0

	print(int(prog_dyn[prog_dyn.shape[0]-1,prog_dyn.shape[1]-1]))
	
	return prog_dyn
	
print(problem1())