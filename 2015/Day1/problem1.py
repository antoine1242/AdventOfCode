import math
import copy

def main():
    with open("input.txt") as f:
        entry = f.readline()

    openning = entry.count("(")
    closing = entry.count(")")

    print(openning - closing)
main()