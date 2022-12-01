def problem2():
	with open("Day17/input1.txt") as f:
	    line = f.readline() 

	targets = line.split('..')
	target_x_1 = int(targets[0].split("=")[-1])
	target_x_2 = int(targets[1].split(",")[0])
	target_y_1 = int(targets[1].split("=")[-1])
	target_y_2 = int(targets[2])

	initial_velocities = set()

	for x_starting_velocity in range(-200,200):
		for y_starting_velocity in range(-200,200):

			x_velocity = x_starting_velocity
			y_velocity = y_starting_velocity

			x_pos = 0
			y_pos = 0
			
			while y_pos >= target_y_1 and x_pos < target_x_2:
				x_pos += x_velocity
				y_pos += y_velocity
				y_velocity -= 1
				
				if x_velocity < 0:
					x_velocity += 1
				if x_velocity > 0:
					x_velocity -= 1

				if x_pos >= target_x_1 and x_pos <= target_x_2 and y_pos >= target_y_1 and y_pos <= target_y_2:
					initial_velocities.add((x_starting_velocity, y_starting_velocity))
					continue

	return len(initial_velocities)

	
print(problem2())