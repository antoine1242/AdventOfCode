import math
import copy

def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    total = 0

    for line in lines:
        range1 = line.split(",")[0]
        range2 = line.split(",")[1]

        a = int(range1.split("-")[0])
        b = int(range1.split("-")[1])

        c = int(range2.split("-")[0])
        d = int(range2.split("-")[1])

        if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
            total += 1

    print(total)

main()