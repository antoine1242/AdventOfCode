def main():
    with open("input.txt") as f:
        content = f.readlines()
        words = [x.strip() for x in content]

    total_2 = 0
    total_3 = 0

    for word in words:
        has_two, has_three = has_two_and_three(word)

        if has_two:
            total_2 += 1
        
        if has_three:
            total_3 +=1

    print(total_2 * total_3)
        
def has_two_and_three(word):
    letters_dict = {}

    for letter in word:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

    has_two = False
    has_three = False

    for key, value in letters_dict.items():
        if value == 2:
            has_two = True
        elif value == 3:
            has_three = True

    return has_two, has_three
main()