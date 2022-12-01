def problem2():
	with open("Day2/input2.txt") as f:
	    commands = f.readlines()
	numbers = [int(x.split(" ")[1]) for x in commands]
	commands = [x.split(" ")[0] for x in commands]

	x = 0
	y = 0
	aim = 0

	for i in range(len(numbers)):
		if commands[i] == "forward":
			x += numbers[i]
			y += aim*numbers[i]
		elif commands[i] == "up":
			aim -= numbers[i]
		else:
			aim += numbers[i]

	return x*y
	
print(problem2())