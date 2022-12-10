import math
import copy

def touching(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1 

def main():
    with open("Day9/input.txt") as f:
        moves = f.read().split("\n")

    print(moves)

    head_position = [0, 0]
    tail_position = [0, 0]

    visited = set()
    visited.add(tuple(tail_position))

    for move in moves:
        direction = move.split(" ")[0]
        nb_moves = int(move.split(" ")[1])

        for i in range(nb_moves):

            if direction == "R":
                head_position[1] += 1
                if not touching(head_position, tail_position):
                    tail_position[0] = head_position[0]
                    tail_position[1] = head_position[1]-1

            elif direction == "L":
                head_position[1] -= 1
                if not touching(head_position, tail_position):
                    tail_position[0] = head_position[0]
                    tail_position[1] = head_position[1]+1

            elif direction == "U":
                head_position[0] -= 1
                if not touching(head_position, tail_position):
                    tail_position[0] = head_position[0]+1
                    tail_position[1] = head_position[1]
            
            elif direction == "D":
                head_position[0] += 1
                if not touching(head_position, tail_position):
                    tail_position[0] = head_position[0]-1
                    tail_position[1] = head_position[1]

            visited.add(tuple(tail_position))

    print(len(visited))

main()