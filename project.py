import random

print("Guess The Number!")


random_number = random.randint(1, 100)

while True:
    number = int(input("Enter your guess here: "))
    
    if number == random_number:
        print("You got it right!")
        break
    elif number < random_number:
        print("Higher")
    elif number > random_number:
        print("Lower")
