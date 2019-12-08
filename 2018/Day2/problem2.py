def main():
    with open("input.txt") as f:
        content = f.readlines()
        words = [x.strip() for x in content]

    len_word = len(words[0])

    for i in range(len(words) - 1):
        for j in range(i+1, len(words)):
            differing_letters = 0
            index = 0

            for k in range(len_word):
                if words[i][k] != words[j][k]:
                    differing_letters += 1
                    if differing_letters == 1:
                        index = k
            if differing_letters == 1:
                return words[i][:index] + words[j][index + 1:]
print(main())