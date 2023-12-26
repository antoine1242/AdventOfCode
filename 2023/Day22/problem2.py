from aocd.models import Puzzle
import copy
from collections import deque
from enum import Enum
import os
import parse
import time
import numpy as np

DAY = int(os.path.dirname(os.path.realpath(__file__)).split("Day")[1])
PATTERN = parse.compile("{x1:d},{y1:d},{z1:d}~{x2:d},{y2:d},{z2:d}")

def collide(brick1, brick2):
    rangex1 = sorted([brick1[0][0], brick1[1][0]])
    rangex2 = sorted([brick2[0][0], brick2[1][0]])

    rangey1 = sorted([brick1[0][1], brick1[1][1]])
    rangey2 = sorted([brick2[0][1], brick2[1][1]])

    rangez1 = sorted([brick1[0][2], brick1[1][2]])
    rangez2 = sorted([brick2[0][2], brick2[1][2]])

    if ((rangex1[0] <= rangex2[0] and rangex1[1] >= rangex2[0]) or (rangex1[0] <= rangex2[1] and rangex1[1] >= rangex2[1]) or (rangex1[0] >= rangex2[0] and rangex1[1] <= rangex2[1])) and \
        ((rangey1[0] <= rangey2[0] and rangey1[1] >= rangey2[0]) or (rangey1[0] <= rangey2[1] and rangey1[1] >= rangey2[1]) or (rangey1[0] >= rangey2[0] and rangey1[1] <= rangey2[1])) and \
        ((rangez1[0] <= rangez2[0] and rangez1[1] >= rangez2[0]) or (rangez1[0] <= rangez2[1] and rangez1[1] >= rangez2[1]) or (rangez1[0] >= rangez2[0] and rangez1[1] <= rangez2[1])):
        return True
    
    return False

def make_bricks_fall(bricks, simulate=False):
    if simulate:
        bricks = copy.deepcopy(bricks)
    fell = True
    falling_bricks = set()
    while fell:
        fell = False
        
        for i in range(len(bricks)):
            brick1 = copy.deepcopy(bricks[i])
            brick1[0][2] -= 1
            brick1[1][2] -= 1

            if brick1[0][2] >= 1 and brick1[1][2] >= 1:
                collision = False
                for j in range(i, -1, -1):
                    if not i == j:
                        brick2 = bricks[j]
                        if not min(brick2[0][2], brick2[1][2]) > max(brick1[0][2], brick1[1][2]):
                            if collide(brick1, brick2):
                                collision = True
                                break

                if not collision:
                    falling_bricks.add(i)
                    fell = True
                    bricks[i][0][2] -= 1
                    bricks[i][1][2] -= 1

    return len(falling_bricks)

def would_bricks_fall(bricks):
    for i in range(len(bricks)):
        brick1 = copy.deepcopy(bricks[i])
        brick1[0][2] -= 1
        brick1[1][2] -= 1
        if brick1[0][2] >= 1 and brick1[1][2] >= 1:
            collision = False
            for j in range(0, len(bricks)):
                if i != j:
                    brick2 = bricks[j]
                    if collide(brick1, brick2):
                        collision = True
                        break
            
            if not collision:
                return True
            
    return False

def main(test=False):
    if test:
        with open(f"Day{DAY}/input.txt") as f:
            ls = f.read()
    else:
        ls = Puzzle(year=2023, day=DAY).input_data

    ls = ls.split("\n")

    bricks = []

    for l in ls:
        match = PATTERN.search(l)
        coords = match.named
        bricks.append([[coords["x1"], coords["y1"], coords["z1"]], [coords["x2"], coords["y2"], coords["z2"]]])

    bricks.sort(key= lambda x: min(x[0][2], x[1][2]))
    
    make_bricks_fall(bricks)

    falling_bricks = 0

    for brick in bricks:
        curr_bricks = copy.deepcopy(bricks)
        curr_bricks.remove(brick)

        falling_bricks += make_bricks_fall(curr_bricks, True)
    

    print(falling_bricks)

start_time = time.time()
#main(test=True)
main() # 

print(f"--- Ran in {time.time() - start_time} seconds ---")