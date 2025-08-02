import random

def loop_for_input(random_number, guess_number):
    while True:
        if int(guess_number) == random_number:
            print("You guessed it!")
            break
        elif int(guess_number) > random_number:
            print("Too high! Guess a lower number")
            guess_number = input("Enter a number between 1 and 100: ")
        else:
            print("Too low! Guess a higher number")
            guess_number = input("Enter a number between 1 and 100: ")

def main():
    random_number = random.randint(1, 100)
    
    guess_number = int(input("Enter a number between 1 and 100: "))
    
    loop_for_input(random_number, guess_number)
    


if __name__ == "__main__":
    main()