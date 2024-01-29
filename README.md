# Hangman Game

## Description

This Python program is an implementation of the classic word-guessing game, Hangman. It features a simple console-based interface where the player guesses letters to form a word. The game uses a list of pre-defined words and represents the hangman stages graphically as the player makes incorrect guesses. The program is divided into several components, each handling a different aspect of the game.

## Requirements

- Python 3.x
- Two additional Python files: hangman_words.py and hangman_art.py
  - hangman_words.py should contain a list of words (word_list) from which the program will randomly select one for the game.
  - hangman_art.py should contain two variables: stages (a list of strings representing different stages of the hangman) and logo (a string representing the game's logo).

## Features

- Random word selection from a provided list.
- Console-based user interaction for guessing letters.
- Dynamic display of the player's progress in guessing the word.
- Graphical representation of the hangman as the player makes incorrect guesses.
- Game-over conditions for both winning (guessing the word) and losing (using up all lives).

## How to Play

- Run the Python program.
- The Hangman game logo and an initial word (hidden with underscores) will be displayed.
- Guess letters one at a time by typing them into the console.
- The game will reveal guessed letters in the word and display the hangman stages for incorrect guesses.
- The game ends when either the word is fully guessed (win) or the hangman is completely drawn (loss).

## Implementation Details

- The `clear()` function: Clears the console screen to refresh the game's display after each guess. It works differently depending on the operating system.
- Game Initialization Variables: Set up the initial state of the game, including selecting a random word, initializing game conditions, and displaying the game logo.
- Main Game Loop: Handles the logic for guessing letters, updating the display, and checking win/loss conditions.

## How to Run

- Ensure you have Python 3.x installed.
- Place the hangman_words.py and hangman_art.py files in the same directory as this script.
- Run the script using a Python interpreter.

## Notes

- This game is console-based and does not feature a graphical user interface.
- Customization of the word list and hangman stages can be done in the respective `hangman_words.py` and `hangman_art.py files`.

Please ensure that the hangman_words.py and hangman_art.py files are correctly set up and available in the same directory as this script for the program to function properly.