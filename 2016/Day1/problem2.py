def main():
    with open("Day1/input.txt") as f:
        commands = f.readline()

    right_turn_dict = {"N": "E", "E": "S", "S": "W", "W": "N"}
    left_turn_dict = {"N": "W", "E": "N", "S": "E", "W": "S"}

    commands = commands.split(", ")

    curr_dir = "N"
    curr_pos = (0,0)

    positions = set()
    positions.add(curr_pos)

    for command in commands:
        if command[0] == "R":
            curr_dir = right_turn_dict[curr_dir]
        else:
            curr_dir = left_turn_dict[curr_dir]

        steps = int(command[1:])

        if curr_dir == "N":
            curr_pos = (curr_pos[0] + steps, curr_pos[1])
        if curr_dir == "E":
            curr_pos = (curr_pos[0], curr_pos[1] + steps)
        if curr_dir == "S":
            curr_pos = (curr_pos[0] - steps, curr_pos[1])
        if curr_dir == "W":
            curr_pos = (curr_pos[0], curr_pos[1] - steps)

        if curr_pos in positions:
            return curr_pos[0] + curr_pos[1]

        else:
            positions.add(curr_pos)

    return "No position was visited twice"

print(main())