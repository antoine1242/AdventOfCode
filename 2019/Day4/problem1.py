def has_neighbors(number):
    ints = [int(d) for d in str(number)]

    for i in range(len(ints)-1):
        if ints[i] == ints[i+1]:
            return True
    
    return False

def is_increasing(number):
    ints = [int(d) for d in str(number)]

    for i in range(len(ints)-1):
        if ints[i+1] < ints[i]:
            return False
    
    return True

total = 0

for i in range(172930,683083):
    if has_neighbors(i) and is_increasing(i):
        total += 1

print(total)

