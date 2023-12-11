import math
import copy
import re

def get_distance(i1, j1, i2, j2):
    return abs(i1 - i2) + abs(j1 - j2)

def main():
    with open("Day11/input.txt") as f:
        lines = f.read().split("\n")

    galaxies = []

    for line in lines:
        galaxies.append(line)
        if not "#" in line:
            galaxies.append(line)

    galaxies_expanded = [[] for row in galaxies]

    for j in range(len(galaxies[0])):
        has_one = False
        for i in range(len(galaxies)):
            if galaxies[i][j] == "#":
                has_one = True
        for index, row in enumerate(galaxies_expanded):
                row += galaxies[index][j]
        if not has_one:

            for index, row in enumerate(galaxies_expanded):
                row += galaxies[index][j]
    
    coordinates = []
    for i in range(len(galaxies_expanded)):
        for j in range(len(galaxies_expanded[0])):
            if galaxies_expanded[i][j] == "#":
                coordinates.append([i,j])
    
    distance_total = 0
    for i in range(len(coordinates)):
        for j in range(i, len(coordinates)):
            distance_total += get_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])

    print(distance_total) # 10231178
main()
