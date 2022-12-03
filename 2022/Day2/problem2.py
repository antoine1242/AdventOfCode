import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.read().split("\n")

    choice = {"A": {"X": "Z", "Y": "X", "Z": "Y"}, "B": {"X": "X", "Y": "Y", "Z": "Z"}, "C": {"X": "Y", "Y": "Z", "Z": "X"}}
    score_result = {"X": 0, "Y": 3, "Z": 6}

    score_choice = {"X": 1, "Y": 2, "Z": 3}

    total_score = 0

    for entry in entries:
        choice_A = entry.split(" ")[0]
        result = entry.split(" ")[1]

        curr_choice = choice[choice_A][result]

        total_score += score_choice[choice[choice_A][result]]
        total_score += score_result[result]


    print(total_score)
main()