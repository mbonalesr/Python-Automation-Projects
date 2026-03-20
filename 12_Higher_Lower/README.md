# Higher-Lower Game 📈📉

A Python implementation of the classic "Higher or Lower" internet game. Test your pop culture and social media knowledge by guessing who has more Instagram followers! This project was **pre-planned using a logical flowchart** before coding began to ensure a robust logic structure.

## 📝 Description

This is a terminal-based game where the player is presented with two random public figures, brands, or celebrities. The goal is to guess which of the two has a higher number of followers on Instagram. 

If the player guesses correctly, their score increases by 1, and the second profile becomes the first profile for the next round. The game continues until the player makes a wrong guess.

## 🧠 Logic Flowchart

Before writing any line of code, the program's logic was entirely mapped out using this flowchart to ensure a bug-free and efficient game loop:

![Game Logic Flowchart](./higher_lower_flowchart.png)

## ✨ Features

* **Modular Codebase:** The project is divided into logical files (`main.py` for logic, `game_data.py` for the database, and `art.py` for ASCII UI) for better readability and maintenance.
* **Dynamic Data Loading:** Uses the `random` module to fetch competitors from a custom dictionary containing 50+ real-world profiles.
* **Continuous Gameplay Loop:** Implements a `while` loop that keeps the game running and updating the score seamlessly.
* **Clear UI:** Clears the terminal screen automatically after every round using `os.system('cls')` to keep the console neat and readable.

## 🚀 How to Run

1. Make sure you have Python installed on your system.
2. Clone this repository or download the project folder.
3. Open your terminal and navigate to the folder containing the game.
4. Run the following command:
   ```bash
   python main.py