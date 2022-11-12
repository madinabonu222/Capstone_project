#Number Guessing Game Objectives
# Include an ASCII art logo.
from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check_answer (guess,answer,turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")
    print(input("Do you want to play again? Type 'yes' or 'no'"))

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def set_difficulty ():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL

# Allow the player to submit a guess for a number between 1 and 100.
def game():
  print(logo)

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100);
  # If they got the answer correct, show the actual answer to the player.
  

  

# Track the number of turns remaining.
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

  #Let the user guess a number.
    guess = int(input("Make a guess: "))
  
# If they run out of turns, provide feedback to the player. 
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guess, you lose.")
      print(f"You lose, the answer was {answer}")
      return
    elif guess != answer:
      print("Guess again")

while True:
  game() 

  
  
  

