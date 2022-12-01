def problem1():
	with open("input1.txt") as f:
	    trees = f.readlines()
	trees = [x.strip() for x in trees]

	x = 0
	y = 0
	hits = 0

	while y < len(trees) - 1:
		x += 3
		y += 1
		x = x % len(trees[0])

		if trees[y][x] == '#':
			hits += 1

	return hits

print(problem1())
