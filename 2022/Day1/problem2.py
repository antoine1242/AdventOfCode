import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.read().split("\n\n")

    

    for entry in entries:
        print(entry.split("\n"))

main()

#720660