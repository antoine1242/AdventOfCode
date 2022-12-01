import copy

directions = ["E", "S", "W", "N"]

def move_ship(curr_dir, curr_x, curr_y, command, number):
    if command == "E":
        curr_x += number
    elif command == "N":
        curr_y += number
    elif command == "S":
        curr_y -= number
    elif command == "W":
        curr_x -= number

    elif command == "R":
        index = directions.index(curr_dir)
        index += number // 90
        curr_dir = directions[index % 4]

    elif command == "L":
        index = directions.index(curr_dir)
        index -= number // 90
        curr_dir = directions[index % 4]

    elif command == "F":
        if curr_dir == "E":
            curr_x += number
        elif curr_dir == "W":
            curr_x -= number
        elif curr_dir == "N":
            curr_y += number
        elif curr_dir == "S":
            curr_y -= number

    return curr_dir, curr_x, curr_y

def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]

    curr_dir = "E"
    curr_x = 0
    curr_y = 0

    for line in lines:
        command = line[0]
        number = int(line[1:])

        curr_dir, curr_x, curr_y = move_ship(curr_dir, curr_x, curr_y, command, number)


    return abs(curr_x) + abs(curr_y)
    
print(problem1())
