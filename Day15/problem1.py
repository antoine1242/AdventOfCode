def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]


    numbers = lines[0].split(",")

    numbers_dic = {}
    spoken_number = 0
    i = 0
    is_new = True

    while i < 2020:
        if i < len(numbers) :
            spoken_number = int(numbers[i])
            old_value = 0
            numbers_dic[spoken_number] = i
            i += 1
            continue

        if is_new:
            spoken_number = 0
            old_value = numbers_dic[spoken_number]
            is_new = spoken_number not in numbers_dic
            numbers_dic[spoken_number] = i

        else:
            spoken_number = (i - 1) - old_value
            is_new = spoken_number not in numbers_dic
            if not is_new:
                old_value = numbers_dic[spoken_number]

            numbers_dic[spoken_number] = i



        i += 1


    return spoken_number


print(problem1())

#504