import copy

def count_surrounding_occupied(seats, i_, j_):
    count = 0
    for i in range(i_-1, i_+2):
        for j in range(j_-1, j_+2):
            if not (i_ == i and j_ == j):
                if i >= 0 and i < len(seats) and j >= 0 and j < len(seats[0]):
                    if seats[i][j] == "#":
                        count += 1

    return count

def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    seats_curr = [list(x.strip()) for x in content]

    while True:
        seats = copy.deepcopy(seats_curr)

        for i in range(len(seats)):
            for j in range(len(seats[0])):
                occupied_seats = count_surrounding_occupied(seats_curr, i, j)
                if seats[i][j] == "#":
                    if occupied_seats >= 4:
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
