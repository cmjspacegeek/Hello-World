import random
def main():
    while True:
        try:
            Level = int(input("Level: "))
            if Level < 1:
                pass
            num = random.randint(1, Level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess > num:
                        print("Too large!")
                    elif guess < num:
                        print("Too small!")
                    elif guess == num:
                        print("Just right")
                        quit()
                except ValueError:
                    pass
        except ValueError:
            pass

main()