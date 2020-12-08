def find_bags(colors_dic, seen, curr_color):
    if curr_color in colors_dic:
        for color in colors_dic[curr_color]:
            if color not in seen:
                seen.add(color)
                find_bags(colors_dic, seen, color)

def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]

    colors_dic = {}

    for index, line in enumerate(lines):
        test = line.split("contain")

        curr_bag = test[0][:-6]
        colors = test[1].strip(".").split(",")

        for index, bag in enumerate(colors):
            colors[index] = bag[2:].strip("s").strip("bag").strip()

        for color in colors:
            if color in colors_dic:
                colors_dic[color].append(curr_bag)
            else:
                colors_dic[color] = [curr_bag]

    print(colors_dic)

    seen = set()

    find_bags(colors_dic, seen, "shiny gold")

    return len(seen)

print(problem1())
