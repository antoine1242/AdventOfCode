def find_winner(position1, position2, score1=0, score2=0, curr_player=True):
	if score1 >= 21:
		return (1, 0)
	elif score2 >= 21:
		return (0, 1)

	if curr_player:
		return \
			1*find_winner(max(1, (position1+3) % 11), position2, score1+max(1, (position1+3) % 11), score2, not curr_player) + \
			3*find_winner(max(1, (position1+4) % 11), position2, score1+max(1, (position1+4) % 11), score2, not curr_player) + \
			6*find_winner(max(1, (position1+5) % 11), position2, score1+max(1, (position1+5) % 11), score2, not curr_player) + \
			7*find_winner(max(1, (position1+6) % 11), position2, score1+max(1, (position1+6) % 11), score2, not curr_player) + \
			6*find_winner(max(1, (position1+7) % 11), position2, score1+max(1, (position1+7) % 11), score2, not curr_player) + \
			3*find_winner(max(1, (position1+8) % 11), position2, score1+max(1, (position1+8) % 11), score2, not curr_player) + \
			1*find_winner(max(1, (position1+9) % 11), position2, score1+max(1, (position1+9) % 11), score2, not curr_player) 

	else:
		return \
			1*find_winner(position1, max(1, (position2+3) % 11), score1, score2+max(1, (position2+3) % 11), not curr_player) + \
			3*find_winner(position1, max(1, (position2+4) % 11), score1, score2+max(1, (position2+4) % 11), not curr_player) + \
			6*find_winner(position1, max(1, (position2+5) % 11), score1, score2+max(1, (position2+5) % 11), not curr_player) + \
			7*find_winner(position1, max(1, (position2+6) % 11), score1, score2+max(1, (position2+6) % 11), not curr_player) + \
			6*find_winner(position1, max(1, (position2+7) % 11), score1, score2+max(1, (position2+7) % 11), not curr_player) + \
			3*find_winner(position1, max(1, (position2+8) % 11), score1, score2+max(1, (position2+8) % 11), not curr_player) + \
			1*find_winner(position1, max(1, (position2+9) % 11), score1, score2+max(1, (position2+9) % 11), not curr_player)

def problem1():
	with open("Day21/input1.txt") as f:
	    lines = f.read().splitlines()

	positon1 = 4#int(lines[0].split(" ")[-1])
	position2 = 8#int(lines[1].split(" ")[-1])

	wins1, wins2 = find_winner(positon1, position2)

	return max(wins1, wins2)
	
print(problem1())