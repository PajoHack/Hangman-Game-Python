# Import the random module to use its functions
import random

# Define a list of words
word_list = ["aardvark", "baboon", "camel"]

# Randomly select one word from the word_list
chosen_word = random.choice(word_list)

# Testin code
print(f"Pssst, the solution is {chosen_word}.")

# Initialize an empty list to hold the display characters
display = []
word_length = len(chosen_word)

# Loop through the number of letters in the chosen word
for _ in range(word_length):
  # Add an underscore to the display list for each letter in the chosen word
  display += "_"

# Print the display list
print(display)

end_of_game = False

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

  print(display)
  
  if "_" not in display:
    end_of_game = True
    print("You Win!")

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):
    letter = chosen_word[position]
    
    if letter == guess:
      display[position] = letter

  print(display)
  
  if "_" not in display:
    end_of_game = True
    print("You Win!")
