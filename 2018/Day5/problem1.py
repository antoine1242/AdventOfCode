def main():
    with open("input.txt") as f:
        polymer = f.readline().rstrip("\n")

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

    print(len(polymer))

main()