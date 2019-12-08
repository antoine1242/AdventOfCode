import copy

def main():
    with open("input.txt") as f:
        initial_polymer = f.readline().rstrip("\n")

    # Go through once to reduce the size of the Polymer that will be checked for each letter
    change = True

    while(change):
        change = False

        curr_polymer = []

        i = 0

        while i < len(initial_polymer):
            if i == len(initial_polymer) - 1:
                curr_polymer.append(initial_polymer[i])
                i += 1

            elif abs(ord(initial_polymer[i]) - ord(initial_polymer[i+1])) == 32:
                change = True
                i += 2

            else:
                curr_polymer.append(initial_polymer[i])
                i += 1

        initial_polymer = "".join(curr_polymer)

    # Check for all chars
    chars_to_check = []

    for i in range(65, 91):
        chars_to_check.append(chr(i) + chr(i+32))

    min_length = len(initial_polymer)

    for char in chars_to_check:
        polymer = copy.deepcopy(initial_polymer)
        polymer = polymer.replace(char[0], "").replace(char[1], "")

        change = True

        while(change):
            change = False

            curr_polymer = []

            i = 0

            while i < len(polymer):
                if i == len(polymer) - 1:
                    curr_polymer.append(polymer[i])
                    i += 1

                elif abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
                    change = True
                    i += 2

                else:
                    curr_polymer.append(polymer[i])
                    i += 1

            polymer = "".join(curr_polymer)

        if len(polymer) < min_length:
            min_length = len(polymer)

    print(min_length)

main()