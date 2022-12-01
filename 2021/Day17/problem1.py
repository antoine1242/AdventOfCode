def problem1():
	with open("Day17/input1.txt") as f:
	    line = f.readline() 

	targets = line.split('..')
	target_x_1 = int(targets[0].split("=")[-1])
	target_x_2 = int(targets[1].split(",")[0])
	target_y_1 = int(targets[1].split("=")[-1])
	target_y_2 = int(targets[2])

	max_y_pos = 0

	for y_starting_velocity in range(1,200):
		y_velocity = y_starting_velocity
		y_pos = 0
		max_y_pos_curr = max_y_pos
		
		while y_pos >= target_y_1:
			y_pos += y_velocity
			y_velocity -= 1

			if y_pos > max_y_pos_curr:
				max_y_pos_curr = y_pos

			if y_pos >= target_y_1 and y_pos <= target_y_2:
				max_y_pos = max_y_pos_curr

	return max_y_pos

	
print(problem1())