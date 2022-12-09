import math
import copy

def touching(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

def move_first_knot(knots, direction):
    if direction == "R":
        knots[0][1] += 1
        
        return "R"

    elif direction == "L":
        knots[0][1] -= 1
        
        return "L"

    elif direction == "U":
        knots[0][0] += 1
        
        return "U"
    
    elif direction == "D":
        knots[0][0] -= 1
        
        return "D"

def move_knot(number, knots):
    if not touching(knots[number], knots[number-1]):
        if abs(knots[number][0] - knots[number-1][0]) > abs(knots[number][1] - knots[number-1][1]):
            knots[number][1] = knots[number-1][1]

            if knots[number][0] > knots[number-1][0]:
                knots[number][0] = knots[number-1][0]+1
            else:
                knots[number][0] = knots[number-1][0]-1

        elif abs(knots[number][0] - knots[number-1][0]) < abs(knots[number][1] - knots[number-1][1]):
            knots[number][0] = knots[number-1][0]

            if knots[number][1] > knots[number-1][1]:
                knots[number][1] = knots[number-1][1]+1
            else:
                knots[number][1] = knots[number-1][1]-1

        else:
            if knots[number][0] > knots[number-1][0]:
                knots[number][0] = knots[number-1][0]+1
            else:
                knots[number][0] = knots[number-1][0]-1

            if knots[number][1] > knots[number-1][1]:
                knots[number][1] = knots[number-1][1]+1
            else:
                knots[number][1] = knots[number-1][1]-1

    else:
        return "no"

def main():
    with open("input.txt") as f:
        moves = f.read().split("\n")

    knots = [[0, 0] for x in range(10)]

    visited = set()
    visited.add(tuple(knots[-1]))

    for move in moves:
        direction = move.split(" ")[0]
        nb_moves = int(move.split(" ")[1])

        for i in range(nb_moves):
            last_knot_direction = move_first_knot(knots, direction)

            for j in range(1, len(knots)):
                last_knot_direction = move_knot(j, knots)

                if last_knot_direction == "no":
                    break
                
                if j == len(knots)-1:
                    visited.add(tuple(knots[-1]))

    print(len(visited))

main()