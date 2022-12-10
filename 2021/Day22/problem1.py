def main():
	with open("Day22/input.txt") as f:
	    lines = f.read().split("\n")

	cube = [[["off" for k in range(101)] for j in range(101)] for i in range(101)]

	for line in lines:
		mode = line.split(" ")[0]

		x_range = [int(value) for value in line.split(" ")[1].split(",")[0].split("=")[1].split("..")]
		y_range = [int(value) for value in line.split(" ")[1].split(",")[1].split("=")[1].split("..")]
		z_range = [int(value) for value in line.split(" ")[1].split(",")[2].split("=")[1].split("..")]

		if (x_range[0]+50 > 100 or x_range[1]+51 < 0) or (y_range[0]+50 > 100 or y_range[1]+51 < 0) or (z_range[0]+50 > 100 or z_range[1]+51 < 0):
			continue

		for i in range(x_range[0]+50, x_range[1]+50+1):
			for j in range(y_range[0]+50, y_range[1]+50+1):
				for k in range(z_range[0]+50, z_range[1]+50+1):
					if i < len(cube) and j < len(cube[0]) and k < len(cube[0][0]):
						cube[i][j][k] = mode

	count = 0 

	for plane in cube:
		for row in plane:
			for mode in row:
				if mode == "on":
					count += 1

	print(count)
	
main()