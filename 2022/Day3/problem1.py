import math
import copy

def main():
    with open("input.txt") as f:
        # entries = f.read().split("\n\n")
        entries = f.read().split("\n")

    total = 0

    for entry in entries:
        mid = int(len(entry) / 2)
        one = entry[:mid]
        two = entry[mid:]
        print(one)
        print(two)

        

        if ''.join(set(one).intersection(two)).islower():
            print(ord(''.join(set(one).intersection(two)))-96)
            total += (ord(''.join(set(one).intersection(two)))-96)
        else:
            print(ord(''.join(set(one).intersection(two)))-38)
            total += (ord(''.join(set(one).intersection(two)))-38)

    print(total)


main()