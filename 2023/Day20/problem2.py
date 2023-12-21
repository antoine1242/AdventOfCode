from aocd.models import Puzzle
import copy
from collections import deque
from enum import Enum
import os
import parse
import time

DAY = int(os.path.dirname(os.path.realpath(__file__)).split("Day")[1])

class FlipFlop():
    def __init__(self, name, dependants, state):
        self.name = name
        self.dependants = dependants
        self.state = state
        self.inputs = {}
    
class Conjunction():
    def __init__(self, name, dependants):
        self.name = name
        self.dependants = dependants
        self.inputs = {}

class Broadcaster():
    def __init__(self, name, dependants):
        self.name = name
        self.dependants = dependants

def send_signal(broadcaster, flip_flops, conjunctions, i):
    queue = deque([["broadcaster", "low", "button"]])   
    
    while len(queue) > 0:
        curr = queue.popleft()

        name = curr[0]
        signal = curr[1]
        sender = curr[2]

        if signal == "high" and sender in ["jg", "hf", "rh", "jm"]:
            print(f"{sender}: {i}")

        if name == "broadcaster":
            for dependant in broadcaster.dependants:
                queue.append([dependant, signal, name])

        elif name in flip_flops:
            if signal == "low":
                flip_flops[name].state = not flip_flops[name].state

                if flip_flops[name].state:
                    new_signal = "high"
                else: 
                    new_signal = "low"
                for dependant in flip_flops[name].dependants:
                    queue.append([dependant, new_signal, name])

        elif name in conjunctions:
            conjunctions[name].inputs[sender] = signal

            has_low_pulse = False
            for key, value in conjunctions[name].inputs.items():
                if value == "low":
                    has_low_pulse = True
                    break

            if has_low_pulse:
                new_signal = "high"
            else:
                new_signal = "low"
            
            for dependant in conjunctions[name].dependants:
                queue.append([dependant, new_signal, name])

def main(test=False):
    if test:
        with open(f"Day{DAY}/input.txt") as f:
            ls = f.read()
    else:
        ls = Puzzle(year=2023, day=DAY).input_data

    ls = ls.split("\n")

    flip_flops = {}
    conjunctions  = {}
    broadcaster = None

    for l in ls:
        if l[0] == "%":
            name = l.split("->")[0][1:-1]
            dependants = l.split("->")[1].strip().split(", ")
            flip_flops[name] = FlipFlop(name, dependants, False)
        elif l[0] == "&":
            name = l.split("->")[0][1:-1]
            dependants = l.split("->")[1].strip().split(", ")
            conjunctions[name] = Conjunction(name, dependants)
        else:
            dependants = l.split("->")[1].strip().split(", ")
            broadcaster = Broadcaster("broadcaster", dependants)

    for key, value in flip_flops.items():
        for dependant in value.dependants:
            if dependant in conjunctions:
                conjunctions[dependant].inputs[key] = "low"
            elif dependant in flip_flops:
                flip_flops[dependant].inputs[key] = True

    for key, value in conjunctions.items():
        for dependant in value.dependants:
            if dependant in conjunctions:
                conjunctions[dependant].inputs[key] = "low"
            elif dependant in flip_flops:
                flip_flops[dependant].inputs[key] = True

    for dependant in broadcaster.dependants:
        if dependant in conjunctions:
                conjunctions[dependant].inputs[key] = "low"
        elif dependant in flip_flops:
            flip_flops[dependant].inputs[key] = True

    i = 1
    while i < 5000:
        send_signal(broadcaster, flip_flops, conjunctions, i)
        i += 1

main() # 240853834793347 (3793*3947*4003*4019)
