import math
import copy
import re

EXPANSION = 1000000

def get_distance(rows, columns, i1, j1, i2, j2):
    n_rows = 0
    for i in range(min(i1, i2)+1, max(i1, i2)):
        if i in rows:
            n_rows += 1
    n_columns = 0
    for j in range(min(j1, j2)+1, max(j1, j2)):
        if j in columns:
            n_columns += 1
    return abs(i1 - i2) + abs(j1 - j2) + (n_rows + n_columns) * (EXPANSION-1)

def main():
    with open("Day11/input.txt") as f:
        galaxies = f.read().split("\n")

    rows = []

    for index, line in enumerate(galaxies):
        if not "#" in line:
            rows.append(index)

    columns = []

    for j in range(len(galaxies[0])):
        has_one = False
        for i in range(len(galaxies)):
            if galaxies[i][j] == "#":
                has_one = True
        
        if not has_one:
            columns.append(j)
    
    coordinates = []
    for i in range(len(galaxies)):
        for j in range(len(galaxies[0])):
            if galaxies[i][j] == "#":
                coordinates.append([i,j])
    
    distance_total = 0
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distance_total += get_distance(rows, columns, coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])

    print(distance_total)
main()
