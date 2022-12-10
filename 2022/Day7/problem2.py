import math
import copy

def main():
    with open("Day7/input.txt") as f:
        lines = f.read().split("\n")

    directories = {}
    curr_dir = "/"

    i = 0
    while i < len(lines):
        if lines[i].startswith("$ cd"):
            dir = lines[i].split(" ")[-1]

            if dir == "..":
                curr_dir = curr_dir.rsplit("/", 2)[0] + "/"

            elif dir != "/":
                curr_dir += dir + "/"
            
            i += 1
            
        elif lines[i].startswith("$ ls"):
            i += 1
            count = 0

            while i < len(lines) and not lines[i].startswith("$"):
                if lines[i].split(" ")[0] != "dir":
                    count += int(lines[i].split(" ")[0])

                i += 1

            directories[curr_dir] = count

            if curr_dir.count("/") > 1:
                tmp = curr_dir
                while tmp.count("/") > 1:
                    tmp = tmp.rsplit("/", 2)[0] + "/"
                    directories[tmp] += count

    max_size = 70000000
    root_size = directories["/"]

    remaining_size = max_size - root_size
    needed_space = 30000000 - remaining_size

    dirs_list = []

    for key, value in directories.items():
        if value >= needed_space:
            dirs_list.append(value)

    dirs_list.sort()
    print(dirs_list[0])  

main()