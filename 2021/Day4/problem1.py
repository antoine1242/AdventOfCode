import numpy as np

def play_bingo(card, number):
	for i in range(len(card)):
		for j in range(len(card[i])):
			if card[i][j] == number:
				card[i][j] = None

	return card

def check_if_bingo(card):
	for line in card:
		if all(element == None for element in line):
			return True

	numpy_card = np.array(card, dtype='object')
	for column in numpy_card.T:
		if all(element == None for element in column):
			return True

	return False

def find_first_card(numbers, cards):
	for number in numbers:
		for card in cards:
			play_bingo(card, number)
		
		for index, card in enumerate(cards):
			if check_if_bingo(card):
				return index, number

def problem1():
	with open("Day4/input1.txt") as f:
		numbers = f.readline()
		numbers = numbers.split(",")
		numbers = [int(x) for x in numbers]

	with open("Day4/input1.txt") as f:
		cards_dirty = f.read().splitlines() 

	cards_dirty = cards_dirty[1:]

	cards = []
	for i in range(len(cards_dirty)):
		new_cards = []
		while i < len(cards_dirty) and cards_dirty[i] != "":
			new_cards.append([int(x) for x in cards_dirty[i].split()])
			i += 1
		
		if len(new_cards) > 0:
			cards.append(new_cards)
		i+=1

	cards = cards[0::5]


	best_card_idx = None
	best_card_idx, winning_number = find_first_card(numbers, cards)

	best_card = cards[best_card_idx]

	sum = 0

	for i in range(len(best_card)):
		for j in range(len(best_card[i])):
			if best_card[i][j] != None:
				sum += int(best_card[i][j])

	return sum * int(winning_number)
	
print(problem1())