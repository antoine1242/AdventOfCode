def has_unique_neighbor(number):
    ints = [int(d) for d in str(number)]

    i = 0

    while i < len(ints)-2:
        if ints[i] == ints[i+1]:
            if ints[i] == ints[i+2]:
                curr = ints[i]
                i += 3
                while(i < len(ints) and ints[i] == curr):
                    i += 1
                i -= 1
            else:
                return True
        if (ints[len(ints)-2] == ints[len(ints)-1]) and (ints[len(ints)-3] != ints[len(ints)-2]):
            return True

        i += 1
    return False

def is_increasing(number):
    ints = [int(d) for d in str(number)]

    for i in range(len(ints)-1):
        if ints[i+1] < ints[i]:
            return False
    
    return True

total = 0

for i in range(172930,683083):
    if has_unique_neighbor(i) and is_increasing(i):
        total += 1

print(total)

