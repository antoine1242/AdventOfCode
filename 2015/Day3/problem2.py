import math
import copy

def main():
    with open("input.txt") as f:
        entry = f.readline()


    santa_turn = True

    total_presents = 1

    currX1 = 0
    currY1 = 0

    currX2 = 0
    currY2 = 0

    houses_dict = {}
    houses_dict[str(currX1) + "," + str(currY1)] = 1

    for house in entry:
        if santa_turn:
            if house == "^":
                currY1 += 1
            elif house == "<":
                currX1 -= 1
            elif house == ">":
                currX1 += 1
            else:
                currY1 -=1

            coordinates = str(currX1) + "," + str(currY1)
            santa_turn = False

        else:
            if house == "^":
                currY2 += 1
            elif house == "<":
                currX2 -= 1
            elif house == ">":
                currX2 += 1
            else:
                currY2 -=1
                
            coordinates = str(currX2) + "," + str(currY2)
            santa_turn = True

        if coordinates not in houses_dict:
            houses_dict[coordinates] = 1
            total_presents += 1

    print(total_presents)

main()