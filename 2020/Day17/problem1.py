import copy

def count_neighbors(grid_3d, i, j, k):
    neighbors = 0

    for i_ in range(i - 1, i + 2):
        for j_ in range(j - 1, j + 2):
            for k_ in range(k - 1, k + 2):
                if i_ >= 0 and i_ < len(grid_3d) and j_ >= 0 and j_ < len(grid_3d[0]) and k_ >= 0 and k_ < len(grid_3d[0][0]):
                    if not (i_ == i and j_ == j and k_ == k):
                        if grid_3d[i_][j_][k_] == "#":
                            neighbors += 1
    return neighbors

def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [list(x.strip()) for x in content]

    grid_3d = []

    for cycle in range(6):
        for index, line in enumerate(lines):
            lines[index] = ["."] + line + ["."]
        lines.append(["." for x in range(len(lines[0]))])
        lines.insert(0, ["." for x in range(len(lines[0]))])

    grid_3d.append(lines)

    for cycle in range(6):
        grid_3d.append([["." for x in range(len(lines))] for y in range(len(lines))])
        grid_3d.insert(0, [["." for x in range(len(lines))] for y in range(len(lines))])

    for cycle in range(6):
        old_grid3d = copy.deepcopy(grid_3d)

        for i in range(len(grid_3d)):
            for j in range(len(grid_3d[0])):
                for k in range(len(grid_3d[0][0])):
                    neighbors = count_neighbors(old_grid3d, i, j, k)

                    if old_grid3d[i][j][k] == "#":
                        if neighbors < 2 or neighbors > 3:
                            grid_3d[i][j][k] = "."
                    else:
                        if neighbors == 3:
                            grid_3d[i][j][k] = "#"

    actives = 0

    for i in range(len(grid_3d)):
        for j in range(len(grid_3d[0])):
            for k in range(len(grid_3d[0][0])):
                if grid_3d[i][j][k] == "#":
                    actives += 1

    return actives

print(problem1())
