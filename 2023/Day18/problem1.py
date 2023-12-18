from aocd.models import Puzzle
import copy
from enum import Enum
import parse

DAY = 18
PATTERN = parse.compile("{direction} {steps:d} ({hexcode})")

class Status(Enum):
    OUT = 1
    ENTERING = 2
    IN = 3
    EXITING = 4

def main(test=False):
    if test:
        with open(f"Day{DAY}/input.txt") as f:
            ls = f.read()
    else:
        ls = Puzzle(year=2023, day=DAY).input_data

    ls = ls.split("\n")

    vertices = []
    location = (0,0)
    vertices.append(location)
    perimeter = 0

    for l in ls:
        match = PATTERN.search(l)
        direction = match.named["direction"]
        steps = match.named["steps"]

        perimeter += steps

        if direction == "R":
            location = (location[0], location[1]+steps)
        elif direction == "L":
            location = (location[0], location[1]-steps)
        elif direction == "U":
            location = (location[0]-steps, location[1])
        elif direction == "D":
            location = (location[0]+steps, location[1])
        vertices.append(location)

    vertices.reverse()

    area = 0
    for i in range(len(vertices)-1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]
        area += (x2 + x1) * (y2 - y1) / 2

    print(area + perimeter/2 + 1)
    
#main(test=True)
main() # 62573

