def count_trees(trees, d_x, d_y):
	x = 0
	y = 0
	hits = 0

	while y < len(trees) - 1:
		x += d_x
		y += d_y
		x = x % len(trees[0])

		if trees[y][x] == '#':
			hits += 1

	return hits

def problem1():
	with open("input2.txt") as f:
	    trees = f.readlines()
	trees = [x.strip() for x in trees]

	return count_trees(trees, 1, 1) * count_trees(trees, 3, 1) * count_trees(trees, 5, 1) * count_trees(trees, 7, 1) * count_trees(trees, 1, 2)
	

print(problem1())
