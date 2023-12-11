import copy

def main():
    with open("Day10/input.txt") as f:
        lines = f.read().split("\n")

    mask = [[0 for j in range(len(lines[0]))] for i in range(len(lines))]

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

    removed = True
    while removed:
        removed = False
        # Remove parts not in loop
        nodes_to_remove = []
        for key, value in nodes.items():
            if len(value) < 2:
                nodes_to_remove.append(key)
                removed = True

        for node_to_remove in nodes_to_remove:
            nodes.pop(node_to_remove)

            for key, value in nodes.items():
                if node_to_remove in value:
                    value.remove(node_to_remove)

    lines_ = [list(line) for line in lines]

    # left - right
    for index_line, line in enumerate(lines_):
        if index_line == 0 or index_line == len(lines_) - 1:
            continue

        in_loop = False
        last_char = ""
        # From left
        for index_char, char in enumerate(line):
            if f"{index_line}:{index_char}:{lines[index_line][index_char]}" in nodes:
                if last_char == "":
                    if char != ".":
                        last_char = char
                        in_loop = not in_loop
                
                elif last_char == "|" or last_char == "S":
                    in_loop = not in_loop
                    if char == "|" or last_char == "S":
                        last_char = ""
                    else:
                        last_char = char

                elif last_char == "F":
                    if char == "-": 
                        continue
                    elif char == "J":
                        last_char = ""
                    elif char == "7":
                        in_loop = not in_loop
                        last_char = ""

                elif last_char == "L":
                    if char == "-": 
                        continue
                    elif char == "7":
                        last_char = ""
                    elif char == "J":
                        in_loop = not in_loop
                        last_char = ""
            else:
                if in_loop:
                    mask[index_line][index_char] = 1

    print(sum([sum(x) for x in mask]))
    
main() # Should be 367

