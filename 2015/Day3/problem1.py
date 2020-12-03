import math
import copy

def main():
    with open("input.txt") as f:
        entry = f.readline()

    total_presents = 1

    currX = 0
    currY = 0

    houses_dict = {}
    houses_dict[str(currX) + "," + str(currY)] = 1

    for house in entry:
        if house == "^":
            currY += 1
        elif house == "<":
            currX -= 1
        elif house == ">":
            currX += 1
        else:
            currY -=1

        coordinates = str(currX) + "," + str(currY)

        if coordinates not in houses_dict:
            houses_dict[coordinates] = 1
            total_presents += 1

    print(total_presents)

main()