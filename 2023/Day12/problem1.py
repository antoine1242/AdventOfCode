from aocd.models import Puzzle
import parse

def check_if_arragement(springs, spring_numbers):
    i = 0
    num = 0
    while i < len(springs):
        if springs[i] == ".":
            i += 1
            continue
            
        elif springs[i] == "#":
            if sum([x == "#" for x in springs[i:i+spring_numbers[num]]]) == spring_numbers[num]:
                i += spring_numbers[num]
                if i == len(springs):
                    num += 1
                    continue
                if springs[i] == "#":
                    return 0
                else:
                    num += 1
            else:
                return 0
                
        if num == len(spring_numbers):
            if sum([x == "#" for x in springs[i:]]) == 0:
                return 1
            else:
                return 0
        
        i += 1
    
    if num == len(spring_numbers):
        return 1
    
    return 0

def count_arragements(i, springs, spring_numbers):
    if sum([x == "?" for x in springs]) == 0:
        is_arragement = check_if_arragement(springs, spring_numbers)
        
        return is_arragement 
    
    arragements = 0

    while i < len(springs):
        if springs[i] in [".", "#"]:
            i += 1
            continue

        elif springs[i] == "?":
            arragements += count_arragements(i, springs[:i] + "#" + springs[i+1:], spring_numbers)
            arragements += count_arragements(i, springs[:i] + "." + springs[i+1:], spring_numbers)

            return arragements
    
    return arragements
            
def main(test=False):
    if test:
        with open("Day12/input.txt") as f:
            lines = f.read().split("\n")
    else:
        lines = Puzzle(year=2023, day=12).input_data.split("\n")

    total_arragements = 0

    for line in lines:
        springs = line.split(" ")[0]
        spring_numbers = [int(x) for x in line.split(" ")[1].split(",")]
        total_arragements += count_arragements(0, springs, spring_numbers)

    print(total_arragements)

main(test=True)
#main() # 7195
