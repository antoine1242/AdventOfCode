import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.read().split("\n")

    results = {"A": {"X": "draw", "Y": "win", "Z": "lose"}, "B": {"X": "lose", "Y": "draw", "Z": "win"}, "C": {"X": "win", "Y": "lose", "Z": "draw"}}
    score_result = {"win": 6, "lose": 0, "draw": 3}

    score_choice = {"X": 1, "Y": 2, "Z": 3}

    total_score = 0

    for entry in entries:
        choice_A = entry.split(" ")[0]
        choice_B = entry.split(" ")[1]

        total_score += score_choice[choice_B]
        total_score += score_result[results[choice_A][choice_B]]

    print(total_score)
main()