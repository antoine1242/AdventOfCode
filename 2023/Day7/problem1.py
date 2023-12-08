import math
import copy
import re

cards = {"A": "14", "K": "13", "Q": "12", "J": "11", "T": "10"}

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

    hands_1 = []
    hands_2 = []
    hands_2_pairs = []
    hands_3 = []
    hands_full_house = []
    hands_4 = []
    hands_5 = []

    for hand in hands:
        hand = [int(x) for x in hand]
        cards_count = count_cards(hand)
        if all(count == 1 for count in cards_count.values()):
            hands_1.append(hand)
        elif sum(1 for count in cards_count.values() if count == 2) == 1 and not any(count == 3 for count in cards_count.values()):
            hands_2.append(hand)
        elif sum(1 for count in cards_count.values() if count == 2) == 2:
            hands_2_pairs.append(hand)
        elif any(count == 3 for count in cards_count.values()) and not any(count == 2 for count in cards_count.values()):
            hands_3.append(hand)
        elif any(count == 3 for count in cards_count.values()) and any(count == 2 for count in cards_count.values()):
            hands_full_house.append(hand)
        elif any(count == 4 for count in cards_count.values()):
            hands_4.append(hand)
        else:
            hands_5.append(hand)

    hands_1 = sorted(hands_1, key=sort_hands)
    hands_2 = sorted(hands_2, key=sort_hands)
    hands_2_pairs = sorted(hands_2_pairs, key=sort_hands)
    hands_3 = sorted(hands_3, key=sort_hands)
    hands_full_house = sorted(hands_full_house, key=sort_hands)
    hands_4 = sorted(hands_4, key=sort_hands)
    hands_5 = sorted(hands_5, key=sort_hands)

    hands = hands_1 = hands_2 + hands_2_pairs + hands_3 + hands_full_house + hands_4 + hands_5

    total_score = 0
    rank = 1
    for hand in hands:
        hand = [str(x) for x in hand]
        total_score += rank * hand_bid_dict["".join(hand)]
        rank += 1

    print(total_score)  # 159047777 no
                        # 159090272 no
                        # 158690712 no
main()
