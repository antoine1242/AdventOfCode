import math
import copy
import ast
from enum import Enum

class Status(Enum):
    ORDERED = 0
    UNORDERED = 1
    CONTINUE = 2

def compare(left, right, depth):
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

    good_pairs = []

    for index, pair in enumerate(pairs):
        if index == 5:
            x = 2
        left = ast.literal_eval(pair.split("\n")[0])
        right = ast.literal_eval(pair.split("\n")[1])

        if compare(left, right, depth=0) in [Status.ORDERED, Status.CONTINUE]:
            good_pairs.append(index+1)

    print(good_pairs)
    print(sum(good_pairs))

main() # 5340
