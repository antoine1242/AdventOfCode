import math
import copy
import re

def main():
    with open("Day10/input.txt") as f:
        lines = f.read().split("\n")

    nodes = {}

    for index_line, line in enumerate(lines):
        for index_char, char in enumerate(line):
            neighbors = []
            if char == ".":
                continue
            if char == "7":
                # Gauche
                if index_char > 0:
                   if lines[index_line][index_char-1] in ["F", "L", "-", "S"]:
                       neighbors.append(f"{index_line}:{index_char-1}:{lines[index_line][index_char-1]}")
                # Bas
                if index_line < len(lines)-1:
                   if lines[index_line+1][index_char] in ["J", "L", "|", "S"]:
                       neighbors.append(f"{index_line+1}:{index_char}:{lines[index_line+1][index_char]}")
            elif char == "J":
                # Gauche
                if index_char > 0:
                   if lines[index_line][index_char-1] in ["F", "L", "-", "S"]:
                       neighbors.append(f"{index_line}:{index_char-1}:{lines[index_line][index_char-1]}")
                # Haut
                if index_line > 0:
                   if lines[index_line-1][index_char] in ["F", "7", "|", "S"]:
                       neighbors.append(f"{index_line-1}:{index_char}:{lines[index_line-1][index_char]}")
            elif char == "F":
                # Droite
                if index_char < len(line)-1:
                   if lines[index_line][index_char+1] in ["J", "7", "-", "S"]:
                       neighbors.append(f"{index_line}:{index_char+1}:{lines[index_line][index_char+1]}")
                # Bas
                if index_line < len(lines)-1:
                   if lines[index_line+1][index_char] in ["J", "L", "|", "S"]:
                       neighbors.append(f"{index_line+1}:{index_char}:{lines[index_line+1][index_char]}")
            elif char == "L":
                # Droite
                if index_char < len(line)-1:
                   if lines[index_line][index_char+1] in ["J", "7", "-", "S"]:
                       neighbors.append(f"{index_line}:{index_char+1}:{lines[index_line][index_char+1]}")
                # Haut
                if index_line > 0:
                   if lines[index_line-1][index_char] in ["F", "7", "|", "S"]:
                       neighbors.append(f"{index_line-1}:{index_char}:{lines[index_line-1][index_char]}")
            elif char == "|":
                # Haut
                if index_line > 0:
                   if lines[index_line-1][index_char] in ["F", "7", "|", "S"]:
                       neighbors.append(f"{index_line-1}:{index_char}:{lines[index_line-1][index_char]}")
                # Bas
                if index_line < len(lines)-1:
                   if lines[index_line+1][index_char] in ["J", "L", "|", "S"]:
                       neighbors.append(f"{index_line+1}:{index_char}:{lines[index_line+1][index_char]}")
            elif char == "-":
                # Droite
                if index_char < len(line)-1:
                   if lines[index_line][index_char+1] in ["J", "7", "-", "S"]:
                       neighbors.append(f"{index_line}:{index_char+1}:{lines[index_line][index_char+1]}")
                # Gauche
                if index_char > 0:
                   if lines[index_line][index_char-1] in ["F", "L", "-", "S"]:
                       neighbors.append(f"{index_line}:{index_char-1}:{lines[index_line][index_char-1]}")
            nodes[f"{index_line}:{index_char}:{lines[index_line][index_char]}"] = neighbors
    curr_node = None
    
    for key, value in nodes.items():
        if "S" in key:
            curr_node = key
            break

    for key, value in nodes.items():
        for node in value:
            if "S" in node:
                nodes[curr_node].append(key)

    seen = set()
    seen.add(curr_node)
    len_path = 0
    while True:
        neighbors = nodes[curr_node]
        if neighbors[0] not in seen:
            curr_node = neighbors[0]
            len_path += 1
            seen.add(neighbors[0])
        elif neighbors[1] not in seen:
            curr_node = neighbors[1]
            len_path += 1
            seen.add(neighbors[1])
        else:
            break
    
    print(math.ceil(len_path / 2)) # 6897
main()
