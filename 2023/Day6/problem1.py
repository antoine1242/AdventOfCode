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

    times = lines[0].split(" ")
    times = [x.strip() for x in times]
    times = [x for x in times if x][1:]
    times = [int(x) for x in times]

    distances = lines[1].split(" ")
    distances = [x.strip() for x in distances]
    distances = [x for x in distances if x][1:]
    distances = [int(x) for x in distances]

    total_ways = 1

    for i in range(len(times)):
        total_ways *= calculate_ways(times[i], distances[i])

    print(total_ways)

main()
