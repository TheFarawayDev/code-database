import random

def roll_die():
  return random.randint(1, 6)

def play_pig():
  player_score = 0
  turn = 1

  while player_score < 100:
    print(f"\nTurn {turn}")
    print(f"Your Current Score is: {player_score}")

    round_score = 0
    while True:
      print(f"This round you have: {round_score}")
      action = input("Would you like to roll or bank? ").lower()

      if action == "roll":
        roll = roll_die()
        print(f"\nYou rolled a {roll}.")

        if roll == 1:
          print("You rolled a 1! You get a zero for this round!")
          round_score = 0
          break
        else:
          round_score += roll
      elif action == "bank":
        player_score += round_score
        break
      else:
        print("Invalid input. Please enter 'roll' or 'bank'.")

    turn += 1

  print(f"\nCongratulation! You won on {turn - 1} turns!")

play_pig()