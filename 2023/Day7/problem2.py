import math
import copy
import re

cards = {"A": "14", "K": "13", "Q": "12", "J": "1", "T": "10"}

def sort_hands(item):
    return item[0], item[1], item[2], item[3], item[4]

def count_cards(hand):
    cards_count = {}
    for card in hand:
        cards_count[card] = cards_count.get(card, 0) + 1
    return cards_count

def main():
    with open("Day7/input.txt") as f:
        lines = f.read().split("\n")

    hands = []
    hand_bid_dict = {}

    for line in lines:
        hand = list(line.split(" ")[0])
        for i in range(len(hand)):
            if hand[i].isalpha():
                hand[i] = cards[hand[i]] 

        hand_bid_dict["".join(hand)] = int(line.split(" ")[1])
        hands.append(hand)

    hands_arrays = [[],[],[],[],[],[],[]]

    for hand in hands:
        hand = [int(x) for x in hand]
        cards_count = count_cards(hand)
        jokers_count = cards_count.get(1, 0)
        if all(count == 1 for count in cards_count.values()):
            hands_arrays[jokers_count].append(hand)

        elif sum(1 for count in cards_count.values() if count == 2) == 1 and not any(count == 3 for count in cards_count.values()):
            if jokers_count == 1 or jokers_count == 2:
                hands_arrays[2].append(hand)
            else:
                hands_arrays[1].append(hand)

        elif sum(1 for count in cards_count.values() if count == 2) == 2:
            if jokers_count == 1:
                hands_arrays[-1].append(hand)
            elif jokers_count == 2:
                hands_arrays[3].append(hand)
            else:
                hands_arrays[-2].append(hand)

        elif any(count == 3 for count in cards_count.values()) and not any(count == 2 for count in cards_count.values()):
            if jokers_count == 0:
                hands_arrays[2].append(hand)
            elif jokers_count == 3 or jokers_count == 1:
                hands_arrays[3].append(hand)

        elif any(count == 3 for count in cards_count.values()) and any(count == 2 for count in cards_count.values()):
            if jokers_count == 0:
                hands_arrays[-1].append(hand)
            else:
                hands_arrays[4].append(hand)

        elif any(count == 4 for count in cards_count.values()):
            if jokers_count == 0:
                hands_arrays[3].append(hand)
            else:
                hands_arrays[4].append(hand)

        elif any(count == 5 for count in cards_count.values()):
            hands_arrays[4].append(hand)


    hands_1 = sorted(hands_arrays[0], key=sort_hands)
    hands_2 = sorted(hands_arrays[1], key=sort_hands)
    hands_2_pairs = sorted(hands_arrays[5], key=sort_hands)
    hands_3 = sorted(hands_arrays[2], key=sort_hands)
    hands_full_house = sorted(hands_arrays[6], key=sort_hands)
    hands_4 = sorted(hands_arrays[3], key=sort_hands)
    hands_5 = sorted(hands_arrays[4], key=sort_hands)

    hands = hands_1 + hands_2 + hands_2_pairs + hands_3 + hands_full_house + hands_4 + hands_5

    total_score = 0
    rank = 1
    for hand in hands:
        hand = [str(x) for x in hand]
        total_score += rank * hand_bid_dict["".join(hand)]
        rank += 1

    print(total_score) # 246285222  

main()
