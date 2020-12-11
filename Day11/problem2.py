import copy

def check_direction(seats, i_, j_, dx, dy):
    i = i_ + dx
    j = j_ + dy

    while (0 <= i < len(seats)) and (0 <= j < len(seats[0])):
        if seats[i][j] == "L":
            return 0
        elif seats[i][j] == "#":
            return 1

        i += dx
        j += dy

    return 0

def count_surrounding_occupied(seats, i_, j_):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                count += check_direction(seats, i_, j_, i, j)

    return count

def problem1():
    with open("input2.txt") as f:
        content = f.readlines()
    seats_curr = [list(x.strip()) for x in content]

    while True:
        seats = copy.deepcopy(seats_curr)

        for i in range(len(seats)):
            for j in range(len(seats[0])):
                occupied_seats = count_surrounding_occupied(seats_curr, i, j)
                if seats[i][j] == "#":
                    if occupied_seats >= 5:
                        seats[i][j] = "L"
                elif seats[i][j] == "L":
                    if occupied_seats == 0:
                        seats[i][j] = "#"

        if seats == seats_curr:
            break

        else:
            seats_curr = seats

    return sum(x.count("#") for x in seats)


print(problem1())
