def move_player(p, score, dice_value, dice_rolls):
	move = 0

	for i in range(3):
		move += dice_value
		dice_value = dice_value + 1

		if dice_value == 101:
			dice_value = 1

	p = (p + move) % 10

	if p == 0:
		p = 10

	score += p

	return p, score, dice_value, dice_rolls + 3

def problem1():
	with open("Day21/input1.txt") as f:
	    lines = f.read().splitlines()

	positon1 = int(lines[0].split(" ")[-1])
	position2 = int(lines[1].split(" ")[-1])

	score1 = 0
	score2 = 0

	dice_value = 1

	dice_rolls = 0

	while True:
		print(score1)
		print(score2)
		positon1, score1, dice_value, dice_rolls = move_player(positon1, score1, dice_value, dice_rolls)
		if score1 >= 1000:
			return score2 * dice_rolls
		position2, score2, dice_value, dice_rolls = move_player(position2, score2, dice_value, dice_rolls)
		if score2 >= 1000:
			return score1 * dice_rolls
	
print(problem1())