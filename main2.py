import random

print("Welcome to the guessing game")

while True:
    luckynumber = random.randint(1 , 100)
    attempts = 0

    while True:
        guess = int(input("guess a number between 1 to 100 : "))
        attempts += 1

        if guess < luckynumber:
            print("your number is too small")

        elif guess > luckynumber:
            print("your number is too big")

        else:
            print("BINGOOOO")
            break

    print(f"Congrats , you guessed the right number and it took you {attempts} attempts ")

    playagain = input("Do you want to play again ? (yes/no) ")
    if playagain != 'yes':
        print("Thank you for playing , goodbye!")
        break
