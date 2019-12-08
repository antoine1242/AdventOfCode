from collections import Counter

def main():
    with open("input.txt") as f:
        content = f.readlines()
        entries = [x.strip() for x in content]

    entries_list = []

    for entry in entries:
        time, action, guard_number = read_entry(entry)

        entries_list.append((time, action, guard_number))

    entries_list.sort()

    curr_guard = -1
    curr_state = ""
    guards_dict = {}
    min_fell_asleep = 0

    for entry in entries_list:
        minute = int(entry[0][-2:])
        action = entry[1]
        guard_number = entry[2]

        if action == "G":
            curr_guard = guard_number
            curr_state = "G"
        elif action == "W":
            curr_state = "W"
        else:
            min_fell_asleep = minute
            curr_state = "F"

        if curr_guard != -1 and curr_state == "W":
            if curr_guard not in guards_dict:
                guards_dict[curr_guard] = []

            for i in range(min_fell_asleep, minute):
                guards_dict[curr_guard].append(i)
                

    max_times = 0
    minute_most_slept = 0
    curr_guard_num = 0

    for guard_number, hours in guards_dict.items():
        data = Counter(hours)
        curr_minute_most_slept = data.most_common(1)[0][0]
        times_slept = data.most_common(1)[0][1]

        if times_slept > max_times:
            max_times = times_slept
            minute_most_slept = curr_minute_most_slept
            curr_guard_num = guard_number

    print("minute_most_slept", minute_most_slept)
    print("curr_guard_num", curr_guard_num)
    print(int(curr_guard_num) * int(minute_most_slept))

def read_entry(entry):
    parts = entry.split(" ")

    time = parts[0][6:8] + parts[0][9:11] + parts[1][0:2] + parts[1][3:5]
    
    action = ""
    guard_number = -1

    if len(parts) == 4:
        if parts[2] == "falls":
            action = "F"
        else:
            action = "W"

    else:
        action = "G"
        guard_number = int(parts[3][1:])

    return time, action, guard_number

main()