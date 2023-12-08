import math
import copy
import re

def calculate_ways(time, distance):
    ways = 0
    i = 0
    while i < time:
        if (time - i) * i > distance:
            ways += 1
        i += 1
    return ways

def main():
    with open("Day6/input.txt") as f:
        lines = f.read().split("\n")

    time = int(lines[0].replace(" ", "").split(":")[1])
    distance = int(lines[1].replace(" ", "").split(":")[1])

    ways = calculate_ways(time, distance)

    print(ways)

main()
