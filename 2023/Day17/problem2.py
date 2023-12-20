from aocd.models import Puzzle
from collections import deque
import copy
import time

class State():
    def __init__(self, i, j, heat_loss, direction, steps):
        self.i = i
        self.j = j
        self.heat_loss = heat_loss
        self.direction = direction
        self.steps = steps

    def __str__(self):
        return f"({self.i}, {self.j}, {self.direction}, {self.steps})"

DAY = 17

def sorting_key(state):
    return state.heat_loss

def main(test=False):
    if test:
        with open(f"Day{DAY}/input.txt") as f:
            ls = f.read()
    else:
        ls = Puzzle(year=2023, day=DAY).input_data

    ls = [list(x) for x in ls.split("\n")]

    grid = []
    heat_loss_grid = []

    for l in ls: 
        grid.append([int(y) for y in l])
    
    # min_heat_losses = []

    # min_heat_loss = 0
    # for i in range(len(grid)):
    #     min_heat_loss += grid[i][i]
    #     if i < len(grid)-1:
    #         min_heat_loss += grid[i][i+1]
    # min_heat_losses.append(min_heat_loss)

    # min_heat_loss = 0
    # for i in range(len(grid)):
    #     min_heat_loss += grid[i][i]
    #     if i < len(grid)-1:
    #         min_heat_loss += grid[i+1][i]
    # min_heat_losses.append(min_heat_loss)

    # min_heat_loss = 0
    # for i in range(0, len(grid), 2):
    #     min_heat_loss += grid[i][i]
    #     if i < len(grid)-1:
    #         min_heat_loss += grid[i][i+1]
    #     if i < len(grid)-2:
    #         min_heat_loss += grid[i][i+2]
    #         min_heat_loss += grid[i+1][i+2]
    # min_heat_losses.append(min_heat_loss)

    # min_heat_loss = 0
    # for i in range(0, len(grid), 2):
    #     min_heat_loss += grid[i][i]
    #     if i < len(grid)-1:
    #         min_heat_loss += grid[i+1][i]
    #     if i < len(grid)-2:
    #         min_heat_loss += grid[i+2][i]
    #         min_heat_loss += grid[i+2][i+1]
    # min_heat_losses.append(min_heat_loss)

    # min_heat_loss = min(min_heat_losses)
    # print(min_heat_loss)

    min_heat_loss = 1500
    for l in ls: 
        heat_loss_grid.append([min_heat_loss for y in l])

    seen = {}

    queue = deque([State(0, 0, 0, None, 10)])

    # counter = 0
    while len(queue) > 0:
        # periodically search neighbors' heat loss
        # if counter % 1 == 0 and heat_loss_grid[-1][-1] >= 1337:
        #     heat_loss_grid_copy = copy.deepcopy(heat_loss_grid)
        #     for i in range(len(heat_loss_grid)):
        #         for j in range(len(heat_loss_grid[0])):
        #             if i > 0:
        #                 up = heat_loss_grid[i-1][j]
        #             else:
        #                 up = 9999999999
        #             if i < len(heat_loss_grid) - 1:
        #                 down = heat_loss_grid[i+1][j]
        #             else:
        #                 down = 9999999999
        #             if j > 0:
        #                 right = heat_loss_grid[i][j-1]
        #             else:
        #                 right = 9999999999
        #             if j < len(heat_loss_grid[0]) - 1:
        #                 left = heat_loss_grid[i][j+1]
        #             else:
        #                 left = 9999999999
        #             augment = min(heat_loss_grid[i][j]*2, 9)
        #             heat_loss_grid_copy[i][j] = min([up+augment, down+augment, right+augment, left+augment, heat_loss_grid[i][j]])
        #     heat_loss_grid = heat_loss_grid_copy
        #     #counter = 0

        # counter += 1

        queue = deque(sorted(queue, key=sorting_key))
        state = queue.popleft()
        curr_heat_loss = state.heat_loss + grid[state.i][state.j]
        if state.i < 0 or state.i > len(grid) or state.j < 0 or state.j > len(grid[0]):
            continue
        if state.i == len(grid)-1 and state.j == len(grid[0])-1 and state.steps >= 4 and state.steps <= 10:
            min_heat_loss = min(curr_heat_loss, min_heat_loss)
            print(min_heat_loss)
            continue
        if str(state) in seen and seen[str(state)] <= curr_heat_loss:
            continue
        else:
            seen[str(state)] = curr_heat_loss

        if curr_heat_loss > (heat_loss_grid[state.i][state.j]) + 9: # 18?
            continue
        else:
            heat_loss_grid[state.i][state.j] = curr_heat_loss
        
        if curr_heat_loss + ((len(grid)-1 - state.i)+(len(grid[0])-1 - state.j)) >= min_heat_loss:
            continue


        # choose lowest neighbor first
        neighbors = []

        if state.i > 0:
            neighbors.append(["U", grid[state.i-1][state.j]])
        if state.j > 0:
            neighbors.append(["L", grid[state.i][state.j-1]])
        if state.i < len(grid) - 1:
            neighbors.append(["D", grid[state.i+1][state.j]])
        if state.j < len(grid[0]) - 1:
            neighbors.append(["R", grid[state.i][state.j+1]])

        # Find lowest neighbor
        neighbors.sort(key=lambda x: x[1])

        for neighbor in neighbors:
            if neighbor[0] == "R":
                #  go right
                if (not ((state.direction == "R" and state.steps == 10) or (state.direction != "R" and state.steps < 4) or state.direction == "L")) and state.j < len(grid[0]) - 1:
                    curr_steps = state.steps + 1 if state.direction == "R" else 1
                    queue.append(State(state.i, state.j+1, curr_heat_loss, "R", curr_steps))
            elif neighbor[0] == "D":
                # go down
                if (not ((state.direction == "D" and state.steps == 10) or (state.direction != "D" and state.steps < 4) or state.direction == "U")) and state.i < len(grid) - 1:
                    curr_steps = state.steps + 1 if state.direction == "D" else 1
                    queue.append(State(state.i+1, state.j, curr_heat_loss, "D", curr_steps))
            elif neighbor[0] == "L":
                # go left
                if (not ((state.direction == "L" and state.steps == 10) or (state.direction != "L" and state.steps < 4) or state.direction == "R")) and state.j > 0:
                    curr_steps = state.steps + 1 if state.direction == "L" else 1
                    queue.append(State(state.i, state.j-1, curr_heat_loss, "L", curr_steps))
            elif neighbor[0] == "U":
                # go up
                if (not ((state.direction == "U" and state.steps == 10) or (state.direction != "U" and state.steps < 4) or state.direction == "D")) and state.i > 0:
                    curr_steps = state.steps + 1 if state.direction == "U" else 1
                    queue.append(State(state.i-1, state.j, curr_heat_loss, "U", curr_steps))

    print(min_heat_loss - grid[0][0])

start_time = time.time()
#main(test=True)
#print(f"Time: {time.time() - start_time} s")
main() # 788
print(f"Time: {time.time() - start_time} s")