import math
import copy

def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    total = 0

    for line in lines:
        range1 = line.split(",")[0]
        range2 = line.split(",")[1]

        range1_1 = int(range1.split("-")[0])
        range1_2 = int(range1.split("-")[1])

        range2_1 = int(range2.split("-")[0])
        range2_2 = int(range2.split("-")[1])

        if (range1_1 >= range2_1 and range1_2 <= range2_2) or (range1_1 <= range2_1 and range1_2 >= range2_2):
            total += 1

    print(total)

main()