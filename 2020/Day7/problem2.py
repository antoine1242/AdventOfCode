def find_bags(colors_dic, curr_color, nums_relation):
    total = 1

    if curr_color in colors_dic:
        for color in colors_dic[curr_color]:
            for relation in nums_relation:
                if relation[0] == curr_color and relation[2] == color:
                    total += int(relation[1]) * find_bags(colors_dic, color, nums_relation)
                    break
    return total

def problem2():
    with open("input2.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]

    colors_dic = {}
    nums_relation = []

    for index, line in enumerate(lines):
        test = line.split("contain")

        curr_bag = test[0][:-6]

        num_colors = test[1].strip(".").split(",")

        for index, bag in enumerate(num_colors):
            num_color = bag.strip("s").strip("bag").strip().split(" ", 1)
            num_colors[index] = num_color

        for num_color in num_colors:
            if num_color[0] != "no":
                nums_relation.append((curr_bag, num_color[0], num_color[1]))
            if curr_bag in colors_dic:
                colors_dic[curr_bag].append(num_color[1])
            else:
                colors_dic[curr_bag] = [num_color[1]]

    total = find_bags(colors_dic, "shiny gold", nums_relation)

    return total - 1

print(problem2())
