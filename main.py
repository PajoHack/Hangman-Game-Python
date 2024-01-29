import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

"""
Game Initialization Variables:
1. end_of_game: A boolean flag to control the game loop. It starts as False and turns True when the game ends.
2. word_list: A list of words from which one will be randomly selected as the 'chosen word' for the game.
3. chosen_word: A randomly selected word from word_list. This is the word the player tries to guess.
4. word_length: The length of chosen_word. Used to determine the number of guesses and iterations in the game loop.
5. lives: Keeps track of the users remaining lives.
"""
end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Testin code
print(f"Pssst, the solution is {chosen_word}.")

# Initialize an empty list to hold the display characters
display = []

# Loop through the number of letters in the chosen word
for _ in range(word_length):
  # Add an underscore to the display list for each letter in the chosen word
  display += "_"

# Print the display list
print(display)

"""
This while loop continues until the end_of_game condition is met. Within the loop:
1. The user is prompted to guess a letter, which is converted to lowercase.
2. The loop then iterates over the length of the chosen word. For each position in the word:
   a. It checks if the letter at that position matches the guessed letter.
   b. If there is a match, the corresponding position in the
   display list is updated with the guessed letter.
3. The updated display list is printed after each guess.
4. The loop checks if there are any remaining underscores ('_') in the display list.
   If not, it means the user has correctly guessed all the letters, 
   the end_of_game is set to True, and the user is notified of their win.
"""
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):
    letter = chosen_word[position]
    
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose!")
    
  print(f"{' '.join(display)}")
  
  if "_" not in display:
    end_of_game = True
    print("You Win!")
