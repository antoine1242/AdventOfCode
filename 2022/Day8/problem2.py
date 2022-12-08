import math
import copy

def calculate_scenic_score_left(grid, i, j):
    tree_height = grid[i][j]
    
    score = 0
    
    j -= 1
    while j >= 0:
        score += 1
        if tree_height <= grid[i][j]:
            break
        j -= 1

    return score

def calculate_scenic_score_right(grid, i, j):
    tree_height = grid[i][j]
    
    score = 0
    
    j += 1
    while j < len(grid[0]):
        score += 1
        if tree_height <= grid[i][j]:
            break
        j += 1

    return score

def calculate_scenic_score_top(grid, i, j):
    tree_height = grid[i][j]
    
    score = 0
    
    i -= 1
    while i >= 0:
        score += 1
        if tree_height <= grid[i][j]:
            break
        i -= 1

    return score

def calculate_scenic_score_bot(grid, i, j):
    tree_height = grid[i][j]
    
    score = 0
    
    i += 1
    while i < len(grid):
        score += 1
        if tree_height <= grid[i][j]:
            break
        i += 1

    return score

def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    highest_score = 0
    
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            score = calculate_scenic_score_left(lines, i, j) * calculate_scenic_score_right(lines, i, j) * calculate_scenic_score_top(lines, i, j) * calculate_scenic_score_bot(lines, i, j)

            highest_score = max(highest_score, score)

    print(highest_score)

main()