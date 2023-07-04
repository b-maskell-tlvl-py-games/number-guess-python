import random


def run_game():
  number_guesses = 0
  target_num = random.randint(1,99)

  while True:
    number_guesses += 1
    player_guess = int( input("Enter Guess (1-99): "))

    if player_guess == target_num:
      print(f"Well Done {player_guess} was Correct! - number of guesses was {number_guesses}")
      break
    elif player_guess > target_num:
      print("Guess too high")
    else:
      print("Guess too low")



# MAIN IDEOM - only run code below if called as script
if __name__ == '__main__':
  
  while True:
    run_game()

    play_again = input("Do You Want To Play Again (y/n): ")
    if play_again == "n":
      break

