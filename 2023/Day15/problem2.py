from aocd.models import Puzzle
import re

DAY = 15

def HASH(op):
    temp = 0
    for char in op:
        temp += ord(char)
        temp *= 17
        temp = temp % 256

    return temp

def main(test=False):
    if test:
        with open(f"Day{DAY}/input.txt") as f:
            ls = f.read()
    else:
        ls = Puzzle(year=2023, day=DAY).input_data

    ls = ls.split("\n")

    operations = ls[0].split(",")

    split_characters = r'[=-]'

    labels = [re.split(split_characters, x)[0] for x in operations]

    substrings = ["=", "-"]

    ops = []
    nums = []
    for op in operations:
        for substring in substrings:
            last_index = op.rfind(substring)
            if last_index != -1:
                ops += op[last_index]

        if op[-1].isdigit():
            nums.append(int(op[-1]))
        else:
            nums.append(None)

    boxes = [[] for i in range(256)]

    for index, label in enumerate(labels):
        box_index = HASH(label)

        op = ops[index]

        if op == "=":
            found = False

            for index_lense, lense in enumerate(boxes[box_index]):
                if lense[0] == label:
                    found = True
                    boxes[box_index][index_lense] = [label, nums[index]]
            
            if not found:
                boxes[box_index].append([label, nums[index]])

        elif op == "-":
            for index_lense, lense in enumerate(boxes[box_index]):
 
                if lense[0] == label:
                    boxes[box_index].pop(index_lense)

    total = 0

    labels = set(labels)

    for label in labels:
        found = False

        temp = 0
        for index_box, box in enumerate(boxes):
            for index_lense, lense in enumerate(box):
                if lense[0] == label:
                    found = True
                    temp += (index_box + 1) * (index_lense + 1) * lense[1]

        if found:
            total += temp

    print(total)

#main(test=True)
main() # 215827
