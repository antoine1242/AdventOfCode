import copy

def count_neighbors(grid_4d, i, j, k, m):
    neighbors = 0

    for i_ in range(i - 1, i + 2):
        for j_ in range(j - 1, j + 2):
            for k_ in range(k - 1, k + 2):
                for m_ in range(m - 1, m + 2):
                    if i_ >= 0 and i_ < len(grid_4d) and j_ >= 0 and j_ < len(grid_4d[0]) and k_ >= 0 and k_ < len(grid_4d[0][0]) and m_ >= 0 and m_ < len(grid_4d[0][0][0]):
                        if not (i_ == i and j_ == j and k_ == k and m_ == m):
                            if grid_4d[i_][j_][k_][m_] == "#":
                                neighbors += 1

    return neighbors

def problem2():
    with open("input2.txt") as f:
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

    grid_4d = []
    grid_4d.append(grid_3d)

    for cycle in range(6+1):
        grid_4d.append([[["." for x in range(len(grid_3d[0][0]))] for y in range(len(grid_3d[0]))] for z in range(len(grid_3d))])
        grid_4d.insert(0, [[["." for x in range(len(grid_3d[0][0]))] for y in range(len(grid_3d[0]))] for z in range(len(grid_3d))])

    for cycle in range(6):
        old_grid4d = copy.deepcopy(grid_4d)

        for i in range(len(grid_4d)):
            for j in range(len(grid_4d[0])):
                for k in range(len(grid_4d[0][0])):
                    for m in range(len(grid_4d[0][0][0])):
                        neighbors = count_neighbors(old_grid4d, i, j, k, m)

                        if old_grid4d[i][j][k][m] == "#":
                            if neighbors < 2 or neighbors > 3:
                                grid_4d[i][j][k][m] = "."
                        else:
                            if neighbors == 3:
                                grid_4d[i][j][k][m] = "#"
        x = 0

    actives = 0

    for i in range(len(grid_4d)):
        for j in range(len(grid_4d[0])):
            for k in range(len(grid_4d[0][0])):
                for m in range(len(grid_4d[0][0][0])):
                    if grid_4d[i][j][k][m] == "#":
                        actives += 1

    return actives

print(problem2())

#