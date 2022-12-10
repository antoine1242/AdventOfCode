import math
import copy

def main():
    with open("Day6/input.txt") as f:
        line = f.read()
    
    chars = []

    total_reads = 0

    i = 0
    while i < len(line):
        if len(chars) < 4:
            total_reads += 1
            chars.append(line[i])
            i += 1
        else:
            if len(chars) == len(set(chars)):
                print(total_reads)
                return total_reads
                
            chars.pop(0)
            total_reads += 1
            chars.append(line[i])
            i += 1

main()