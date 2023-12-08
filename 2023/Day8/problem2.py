import math
import copy
import re

instructions_dict = {"L": 0, "R": 1}

def get_steps(start, network, directions):
    curr = start
    steps = 0
    direction = 0
    while curr[-1] != "Z":
        curr = network[curr][directions[direction]]
        steps += 1
        direction = (direction + 1) % len(directions)
    
    return steps

def main():
    with open("Day8/input.txt") as f:
        instructions = f.read().split("\n\n")

    directions = instructions[0]
    directions = [instructions_dict[char] for char in instructions[0]]

    network = {}  
    for line in instructions[1].split("\n"):
        curr = line.split(" = ")[0]
        left = line.split(" = ")[1].split(", ")[0].split("(")[1]
        right = line.split(" = ")[1].split(", ")[1].split(")")[0]

        network[curr] = (left, right)

    starts = []

    for key, value in network.items():
        if key[-1] == "A":
            starts.append(key)
        
    steps = []
    for start in starts:
        steps.append(get_steps(start, network, directions))

    lcm = 1
    for step in steps:
        lcm = lcm*step//math.gcd(lcm, step)
    print(lcm)

main()
