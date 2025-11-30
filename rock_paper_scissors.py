
# 0 to represent "Rock", a 1 to represent "Paper", or a 2 to represent "Scissors."

import random

play_again = "yes"
#lower() means that it will turn capitalized letter into lower cases
while play_again.lower() == "yes":
    Computer = random.randint(0, 2)
    print("0 means Rock, 1 means Paper, and 2 means Scissors")
    player = int(input("Enter your number 0-2 here:  "))

#Computer wins
    if player == 0 and Computer == 1:
        player = "Rock"
        Computer = "Paper"
        winner = "Computer"
        print("The winner is the", winner ,"!")
        print("Player chose", player ,"2and Computer chose", Computer)
    elif player == 1 and Computer == 2:
        player = "Paper"
        Computer = "Scissors"
        winner = "Computer"
        print("The winner is the", winner ,"!")
        print("Player chose", player ,"and Computer chose", Computer)
    elif player == 2 and Computer == 0:
        player = "Scissors"
        Computer = "Rock"
        winner = "Computer"
        print("The winner is the", winner ,"!") 
        print("Player chose", player ,"and Computer chose", Computer)

    #Player wins
    elif Computer == 0 and player == 1:
        Computer = "Rock"
        player = "paper"
        winner = "Player"
        print("The winner is the", winner ,"!")
        print("Player chose", player ,"and Computer chose", Computer)
    elif Computer == 1 and player == 2:
        Computer = "Paper"
        player = "Scissors"
        winner = "Player"
        print("The winner is the", winner ,"!")
        print("Player chose", player ,"and Computer chose", Computer)
    elif Computer == 2 and player == 0:
        Computer = "Scissors"
        player = "Rock"
        winner = "Player"
        print("The winner is the", winner ,"!")
        print("Player chose", player ,"and Computer chose", Computer)

    elif player == 0 and Computer == 0:
        print("Tie!")
        print("Both chose Rock!")
    elif player == 1 and Computer == 1:
        print("Tie!")
        print("Both chose Paper!")
    elif player == 2 and Computer == 2:
        print("Tie!")
        print("Both chose Scissors!")

    play_again = input("Do you want to play again?  ")
print("Thanks for playing!")