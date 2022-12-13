import math
import copy
import ast
from enum import Enum

class Status(Enum):
    ORDERED = 0
    UNORDERED = 1
    CONTINUE = 2

class Packet:
    def __init__(self, packet):
        self.packet = packet

    def __gt__(self, other):
        return compare(self.packet, other.packet) == Status.UNORDERED

def compare(left, right, depth=0):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return Status.CONTINUE
        elif left < right:
            return Status.ORDERED
        elif left > right:
            return Status.UNORDERED

    if isinstance(left, int):
        left = [left]
    
    if isinstance(right, int):
        right = [right]

    for i in range(len(left)):
        if i == len(right):
            return Status.UNORDERED

        status = compare(left[i], right[i], depth+1)
        if status == Status.UNORDERED:
            return Status.UNORDERED
        elif status == Status.ORDERED:
            return Status.ORDERED

    if len(left) != len(right):
        return Status.ORDERED

    if depth == 0:
        return Status.ORDERED
    else:
        return Status.CONTINUE

def main():
    with open("Day13/input.txt") as f:
        pairs = f.read().split("\n\n")

    packets = [Packet(ast.literal_eval(x)) for x in "\n".join(pairs).split("\n")]
    packets.append(Packet([[2]]))
    packets.append(Packet([[6]]))

    unordered = True

    while unordered:
        unordered = False
        i = 0
        while i < len(packets)-1:
            if packets[i] > packets[i+1]:
                tmp = packets[i]
                packets[i] = packets[i+1]
                packets[i+1] = tmp
                unordered = True
            
            i += 1

    result = 1
    for i in range(len(packets)):
        if packets[i].packet in [[[2]], [[6]]]:
            result *= i+1 

    print(result)

main() #21276
