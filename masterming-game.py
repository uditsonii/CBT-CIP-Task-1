import random

def setNumber(player):
    while True:
        number = input(f"{player}, set your Multi-digit number: ")
        if number.isdigit():
            return number
        else:
            print("Invalid input. Please Enter a valid input")

def getGuess(player):
    while True:
        guess = input(f"{player}, Enter your guess: ")
        if guess.isdigit():
            return guess
        else:
            print("Invalid input. Please Enter a valid input")

def provideHint(secretNumber, guess):
    correctPositions = 0
    correctDigits = 0
    for i in range(len(secretNumber)):
        if guess[i] == secretNumber[i]:
            correctPositions +=1
        elif guess[i] in secretNumber:
            correctDigits +=1
    return correctPositions, correctDigits 

def playGame(player1, player2):
    secretNumber = setNumber(player1)
    attempts = 0
    while True:
        attempts +=1
        guess = getGuess(player2)
        if guess == secretNumber:
            print(f"Congratulations {player2}, you guess the number {secretNumber} in {attempts} attempts\n")
            return attempts
        else:
            correctPositions, correctDigits = provideHint(secretNumber, guess)
            print("Hint: ")
            print(f"Correct digits in the Correct Position: {correctPositions}")
            print(f"Correct digits in the Wrong Position: {correctDigits}")

def main():
    print("Welcome to the Mastermind Game")
    player1 = "Player1"
    player2 = "Player2"

    print(f"{player1}'s turn to set the number")
    player1Attempts = playGame(player1, player2)

    print(f"{player2}'s turn to set the number")
    player2Attempts = playGame(player2, player1)
 
    if player1Attempts < player2Attempts:
        print("Player 1 wins and is crowned Mastermind")
    elif player1Attempts > player2Attempts:
        print("Player 2 wins and is crowned Mastermind")  
    else:
        print("Tie! Both players are Mastermind")
    

main()