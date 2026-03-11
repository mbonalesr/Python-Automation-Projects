# 🎯 Number Guessing Game

A console-based game built with Python where the player must guess a randomly generated secret number between 1 and 100, managing a life system based on the selected difficulty.

## 🛠️ Technologies & Concepts Applied
- **Python 3**
- **Libraries:** `random` (number generation), `os` (console clearing).
- **Scope Management:** Proper handling of global constants and local variables.
- **Functions & Returns:** Modularization of the core game logic to prevent memory leaks.
- **Game Loops:** `while` loops controlled by boolean flags (`game_over`).
- **DRY Principle (Don't Repeat Yourself):** Code refactoring for efficiency and readability.

## 🧠 Logic Flow & Architecture
To build this game, the problem was broken down into the following logical steps:
1. **Initialization:** Generate a random secret number (1-100) and define global constants for lives (`EASY_LIVES = 10`, `HARD_LIVES = 5`).
2. **Difficulty Setup:** A `choosing_difficulty()` function that evaluates the user's input and returns the starting number of lives.
3. **Evaluation Engine:** A core `check_answer()` function with a single responsibility: compare the user's guess against the secret number, print hints ("Too high" / "Too low"), and return the updated life count.
4. **Game Loop:** A `while not game_over:` loop that drives the game by:
   - Requesting the user's guess.
   - Updating the global life counter by catching the `return` value from the evaluation engine.
   - Checking for win/loss conditions to break the loop.

## 🎮 How to Play
1. Run the `main.py` file in your terminal.
2. Choose your difficulty by typing `easy` (10 attempts) or `hard` (5 attempts).
3. Enter integers to try and guess the secret number.
4. Follow the on-screen hints ("Too high" or "Too low") to adjust your next guess.