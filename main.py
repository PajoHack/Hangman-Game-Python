import random
import os
from hangman_words import word_list
from hangman_art import stages, logo

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

"""
Game Initialization Variables:
1. end_of_game: A boolean flag to control the game loop. It starts as False and turns True when the game ends.
2. word_list: A list of words from which one will be randomly selected as the 'chosen word' for the game.
3. chosen_word: A randomly selected word from word_list. This is the word the player tries to guess.
4. word_length: The length of chosen_word. Used to determine the number of guesses and iterations in the game loop.
5. lives: Keeps track of the users remaining lives.
"""
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(logo)

# Testin code
# print(f"Pssst, the solution is {chosen_word}.")

# Initialize an empty list to hold the display characters
display = []

# Loop through the number of letters in the chosen word
for _ in range(word_length):
  # Add an underscore to the display list for each letter in the chosen word
  display += "_"

# Print the display list
print(display)
"""
This while loop runs the main game logic until the end_of_game condition is met. 
The game continues under these conditions:
1. The player is repeatedly prompted to guess a letter, which is converted to lowercase.
2. The loop iterates over the length of the chosen word:
   a. If the guessed letter matches a letter in the chosen word, that letter is 
   revealed in the display list at the corresponding position.
3. If the guessed letter is not in the chosen word, the player loses one life.
   a. If the player's lives reach zero, the game ends, and the player loses.
4. After each guess, the current state of the display (showing correctly guessed 
letters and remaining blanks) is printed.
5. The game checks if there are any remaining underscores ('_') in the display list:
   a. If not, it means the player has guessed all the letters, the end_of_game is set to True, 
   and the player wins.
6. The current state of the hangman (based on the number of lives left) is printed after each guess.
"""
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  clear()
  
  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose!")
    
  print(f"{' '.join(display)}")
  
  if "_" not in display:
    end_of_game = True
    print("You Win!")
    
  print(stages[lives])
