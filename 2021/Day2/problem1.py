def problem1():
	with open("Day2/input1.txt") as f:
	    commands = f.readlines()
	numbers = [int(x.split(" ")[1]) for x in commands]
	commands = [x.split(" ")[0] for x in commands]

	x = 0
	y = 0

	for i in range(len(numbers)):
		if commands[i] == "forward":
			x += numbers[i]
		elif commands[i] == "up":
			y -= numbers[i]
		else:
			y += numbers[i]

	return x*y
	
print(problem1())