def main():
    with open("input.txt") as f:
        content = f.readlines()
        claims = [x.strip() for x in content]

    grid = inititialize_grid()

    for claim in claims:
        claim_number, start_point, size = read_claim(claim)

        for i in range(start_point[0], start_point[0] + size[0]):
            for j in range(start_point[1], start_point[1] + size[1]):
                if i<1000 and j<1000:
                    if grid[i][j] != ".":
                        grid[i][j] = "X"
                    else:
                        grid[i][j] = str(claim_number)

    for claim in claims:
        claim_number, start_point, size = read_claim(claim)

        is_overlapping = False

        for i in range(start_point[0], start_point[0] + size[0]):
            for j in range(start_point[1], start_point[1] + size[1]):
                if i<1000 and j<1000:
                    if grid[i][j] != str(claim_number):
                        is_overlapping = True
                else:
                    is_overlapping = True
            if is_overlapping:
                break
            
        if not is_overlapping:
            return claim_number

def inititialize_grid():
    grid = []
    for i in range(1000):
        grid.append([])
        for j in range(1000):
            grid[i].append(".")

    return grid

def read_claim(claim):
    parts = claim.split(" ")
    claim_number = int(parts[0][1:])

    start_array = parts[2].split(",")
    start_point = (int(start_array[0]) + 1, int(start_array[1][:-1]) + 1)
    size_array = parts[3].split("x")
    size = (int(size_array[0]), int(size_array[1]))

    return claim_number, start_point, size

print(main())