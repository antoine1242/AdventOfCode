import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.readlines()

    moons = []

    for entry in entries:
        entry = entry.strip("\n")
        moons.append(read_moon_input(entry))

    cycles_length = []
    seen_pos = {}

    j = 0
    i = 0
    while True:
        curr_moons = make_step(moons)
        curr_dir_pos = str(curr_moons[0][0+j]) + "," + str(curr_moons[0][3+j]) + ":" + \
            str(curr_moons[1][0+j]) + "," + str(curr_moons[1][3+j]) + ":" + \
            str(curr_moons[2][0+j]) + "," + str(curr_moons[2][3+j]) + ":" + \
            str(curr_moons[3][0+j]) + "," + str(curr_moons[3][3+j])

        if curr_dir_pos in seen_pos:
            j += 1
            cycles_length.append(i)
            if j == 3:
                break
            seen_pos = {}
            i = 0
            continue
        seen_pos[curr_dir_pos] = 1

        i += 1
    print(cycles_length)
    #print(compute_lcm(cycles_length[0], compute_lcm(cycles_length[1], cycles_length[2])))

def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

def make_step(moons):
    # Change velocities
    for i in range(len(moons)):
        curr_moon = moons[i]
        curr_x = curr_moon[0]
        curr_y = curr_moon[1]
        curr_z = curr_moon[2]
        
        for j in range(i+1, len(moons)):
            second_moon = moons[j]
            second_x = second_moon[0]
            second_y = second_moon[1]
            second_z = second_moon[2]

            if curr_x > second_x:
                curr_moon[3] -= 1
                second_moon[3] += 1
            elif curr_x < second_x:
                curr_moon[3] += 1
                second_moon[3] -= 1

            if curr_y > second_y:
                curr_moon[4] -= 1
                second_moon[4] += 1
            elif curr_y < second_y:
                curr_moon[4] += 1
                second_moon[4] -= 1

            if curr_z > second_z:
                curr_moon[5] -= 1
                second_moon[5] += 1
            elif curr_z < second_z:
                curr_moon[5] += 1
                second_moon[5] -= 1
    
    for moon in moons:
        moon[0] += moon[3]
        moon[1] += moon[4]
        moon[2] += moon[5]

    return [moons[0], moons[1], moons[2], moons[3]]

def read_moon_input(entry):
    coordinates_raw = entry.split(" ")
    x = int(coordinates_raw[0][3:-1])
    y = int(coordinates_raw[1][2:-1])
    z = int(coordinates_raw[2][2:-1])

    return [x, y, z, 0, 0, 0]

main()