from aocd.models import Puzzle
import copy

DAY = 16

def main(test=False):
    if test:
        with open(f"Day{DAY}/input.txt") as f:
            ls = f.read()
    else:
        ls = Puzzle(year=2023, day=DAY).input_data

    ls = ls.split("\n")

    grid = [list(line) for line in ls]

    start_states = []

    for i in range(len(grid)):
        start_states.append([i, 0, "R"])
        start_states.append([i, len(grid[0])-1, "L"])
    for j in range(len(grid[0])):
        start_states.append([0, j, "D"])
        start_states.append([len(grid)-1, j, "U"])

    running = True

    max_energized = 0
 
    for start_state in start_states:
        grid = [list(line) for line in ls]
        energized = {}
        states_seen = {}
        states = [start_state]

        while running:
            if len(states) == 0:
                break
            new_states = []
            for state in states:
                if str(state) not in states_seen:
                    states_seen[str(state)] = True
                    coordinates = [state[0], state[1]]
                    direction = state[2]
                    if str(coordinates) not in energized:
                        energized[str(coordinates)] = True

                    i = coordinates[0]
                    j = coordinates[1]
                    curr_space = grid[i][j]

                    if curr_space == ".":
                        if direction == "R":
                            if j + 1 < len(grid[0]):
                                new_states.append([i, j+1, direction])
                        elif direction == "L":
                            if j - 1 >= 0:
                                new_states.append([i, j-1, direction])
                        elif direction == "D":
                            if i + 1 < len(grid):
                                new_states.append([i+1, j, direction])
                        elif direction == "U":
                            if i - 1 >= 0:
                                new_states.append([i-1, j, direction])

                    elif curr_space == "|":
                        if direction == "R" or direction == "L":
                            if i + 1 < len(grid):
                                new_states.append([i+1, j, "D"])
                            if i - 1 >= 0:
                                new_states.append([i-1, j, "U"])
                        elif direction == "D":
                            if i + 1 < len(grid):
                                new_states.append([i+1, j, direction])
                        elif direction == "U":
                            if i - 1 >= 0:
                                new_states.append([i-1, j, direction])

                    elif curr_space == "-":
                        if direction == "R":
                            if j + 1 < len(grid[0]):
                                new_states.append([i, j+1, direction])
                        elif direction == "L":
                            if j - 1 >= 0:
                                new_states.append([i, j-1, direction])
                        elif direction == "U" or direction == "D":
                            if j - 1 >= 0:
                                new_states.append([i, j-1, "L"])
                            if j + 1 < len(grid[0]):
                                new_states.append([i, j+1, "R"])
                    
                    elif curr_space == "\\":
                        if direction == "R":
                            if i + 1 < len(grid):
                                new_states.append([i+1, j, "D"])
                        elif direction == "L":
                            if i - 1 >= 0:
                                new_states.append([i-1, j, "U"])
                        elif direction == "U":
                            if j - 1 >= 0:
                                new_states.append([i, j-1, "L"])
                        elif direction == "D":
                            if j + 1 < len(grid[0]):
                                new_states.append([i, j+1, "R"])

                    elif curr_space == "/":
                        if direction == "L":
                            if i + 1 < len(grid):
                                new_states.append([i+1, j, "D"])
                        elif direction == "R":
                            if i - 1 >= 0:
                                new_states.append([i-1, j, "U"])
                        elif direction == "D":
                            if j - 1 >= 0:
                                new_states.append([i, j-1, "L"])
                        elif direction == "U":
                            if j + 1 < len(grid[0]):
                                new_states.append([i, j+1, "R"])
            states = copy.deepcopy(new_states)
                            
        max_energized = max(len(energized), max_energized)

    print(max_energized)

#main(test=True)
main() # 8163
