from random import randint
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            rand_number = randint(1, level)
            guess = -1
            while guess != rand_number:
                try:
                    # print(guess)
                    # print(rand_number)
                    guess = int(input("Guess: "))
                    if guess > rand_number:
                        print("Too large!")
                    elif guess < rand_number:
                        print("Too small!")
                    elif guess == rand_number:
                        print("Just right!")
                        sys.exit()
                except ValueError:
                    pass
            break
        except ValueError:
            pass

main()
