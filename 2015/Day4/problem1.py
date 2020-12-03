import hashlib 

def main():
    puzzle_input = "ckczppom"

    i = 0

    while True:
        if hashlib.md5((puzzle_input + str(i)).encode()).hexdigest()[:5] == "00000":
            print(i)
            return i
        
        i += 1


main()