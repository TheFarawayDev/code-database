import random

def roll_die():
    return random.randint(1, 6)

def computer_turn(computer_score):
    round_score = 0
    print("\nThe computer's turn.")
    while round_score <= 15:
        roll = roll_die()
        print(f"The computer rolled a {roll}")
        if roll == 1:
            print("The computer rolled a 1. End of turn.\n")
            return 0
        else:
            round_score += roll
            print(f"This round the computer has: {round_score}")
            if round_score <= 15:
                print("The computer chooses to roll again.\n")
        #No if statement needed, the bank statement is always printed after the loop.
    print("The computer chooses to bank.\n")
    return round_score

def player_turn(player_score):
    round_score = 0
    while True:
        print(f"This round you have: {round_score}")
        action = input("Would you like to roll or bank? ").lower()
        if action == "roll":
            roll = roll_die()
            print(f"\nYou rolled a {roll}.")
            if roll == 1:
                print("You rolled a 1! You get a zero for this round!")
                return 0
            else:
                round_score += roll
        elif action == "bank":
            return round_score
        else:
            print("Invalid input. Please enter 'roll' or 'bank'.")

def play_pig_computer():
    player_score = 0
    computer_score = 0
    turn = 1

    while player_score < 100 and computer_score < 100:
        print(f"\nTurn {turn}")
        print(f"Your Current Score is: {player_score}")
        print(f"Computer Current Score is: {computer_score}")

        player_score += player_turn(player_score)
        if player_score >= 100:
            break
        computer_score += computer_turn(computer_score)
        if computer_score >= 100:
            break
        turn += 1

    print("\nGame Over!")
    if player_score >= 100 and computer_score >= 100:
        if player_score > computer_score:
            print("You won!")
        else:
            print("The Computer won!")
    elif player_score >= 100:
        print("You won!")
    else:
        print("The Computer won!")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")
    print(f"Game ended on turn: {turn}")

play_pig_computer()