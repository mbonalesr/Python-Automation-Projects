# 🔤 Hangman Game - Python Console Project

A classic text-based Hangman game built with Python. The player has 6 lives to guess a randomly chosen word letter by letter before the stickman is fully drawn.

## 🧠 Technical Concepts Applied
* **Lists & Strings:** Iterating through words and updating the hidden placeholders.
* **While & For Loops:** Maintaining the main game loop (`while not end_of_game`) and checking letters inside the word.
* **Conditionals:** Checking if a guess is correct, incorrect, or already guessed.
* **Modularization:** Splitting the code into separate files (`main.py`, `hangman_art.py`, and `hangman_words.py`) for cleaner architecture and readability.

## 🎮 Features
* Random word selection from a custom dictionary.
* ASCII Art integration that updates dynamically based on the player's remaining lives.
* Input validation: Warns the user if they enter a letter they have already guessed without penalizing them.

## 🛠️ How to run
Simply execute the `main.py` file in your terminal:
```bash
python main.py