from aocd.models import Puzzle
import time

def count_arragements(springs, spring_numbers, prev_is_spring, seen):
    if springs + str(spring_numbers) + str(prev_is_spring) in seen:
        return seen[springs + str(spring_numbers) + str(prev_is_spring)]
    
    remaining_possible_springs = sum([x in ["?", "#"] for x in springs])
    remaining_springs = sum(spring_numbers)
    arragements = 0

    # S'il ne reste pas assez de spring possible
    if remaining_possible_springs < remaining_springs:
        seen[springs + str(spring_numbers) + str(prev_is_spring)] = 0
        return 0
    if remaining_springs == 0:
        if  sum([x in ["#"] for x in springs]) == 0:
            seen[springs + str(spring_numbers) + str(prev_is_spring)] = 1
            return 1
        else:
            seen[springs + str(spring_numbers) + str(prev_is_spring)] = 0
            return 0
    
    if prev_is_spring:
        if springs[0] == "#":
            seen[springs + str(spring_numbers) + str(prev_is_spring)] = 0
            return 0
        else:
            arragements += count_arragements(springs[1:], spring_numbers, False, seen)
    else:
        if springs[0] == ".":
            arragements += count_arragements(springs[1:], spring_numbers, False, seen) 
        else:
            if spring_numbers[0] == len(springs):
                seen[springs + str(spring_numbers) + str(prev_is_spring)] = 1
                return 1
            elif spring_numbers[0] > len(springs):
                seen[springs + str(spring_numbers) + str(prev_is_spring)] = 0
                return 0
            else:
                if sum([x in ["?", "#"] for x in springs[:spring_numbers[0]]]) == spring_numbers[0]:
                    arragements += count_arragements(springs[spring_numbers[0]:], spring_numbers[1:], True, seen)
                if springs[0] == "?":
                    arragements += count_arragements(springs[1:], spring_numbers, False, seen) 
    seen[springs + str(spring_numbers) + str(prev_is_spring)] = arragements
    return arragements
            
def main(test=False):
    if test:
        with open("Day12/input.txt") as f:
            lines = f.read().split("\n")
    else:
        lines = Puzzle(year=2023, day=12).input_data.split("\n")

    total_arragements = 0

    for line in lines:
        springs = base_springs = line.split(" ")[0]
        spring_numbers = [int(x) for x in line.split(" ")[1].split(",")]
        
        for i in range(4):
            springs += "?" + base_springs
        spring_numbers *= 5
        total_arragements += count_arragements(springs, spring_numbers, False, {})

    print(total_arragements)

start_time = time.time()
#main(test=True)
main() # 33992866292225
print("--- %s seconds ---" % (time.time() - start_time))
