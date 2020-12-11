def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    numbers = [int(x.strip()) for x in content]

    built_in = max(numbers) + 3
    
    numbers.append(0)    
    numbers.append(built_in)

    numbers.sort()

    bounce_one = 0
    bounce_three = 0

    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] == 1:
            bounce_one += 1   
        elif numbers[i+1] - numbers[i] == 3:
            bounce_three += 1   

    return bounce_one * bounce_three

print(problem1())
