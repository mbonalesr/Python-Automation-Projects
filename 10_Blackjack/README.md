# 🃏 Blackjack Capstone Project - Python Console Game

A fully playable, text-based Blackjack (21) game built entirely in Python. It pits the user against the PC (dealer) following traditional casino rules, including dynamic Ace calculation and strict dealer drawing logic.

## 🧠 Technical Concepts Applied
* **Lists and Randomization:** Simulated an infinite deck of cards using a list of integers `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]` where 10 represents face cards and 11 represents the Ace. The `deal_card()` function randomly selects from this pool.
* **Advanced Control Flow (The Ace Logic):** Programmed a mathematical condition to dynamically convert an Ace from an 11 to a 1 if the current hand score exceeds 21 (`if score > 21 and 11 in cards:`).
* **PC Dealer AI:** Implemented the classic casino rule where the dealer must continue to draw cards while their score is under 17 (`while pc_score < 17:`) and stand on 17 or above.
* **Scope & Encapsulation:** Wrapped the core game logic inside a main `blackjack_game()` function. This safely resets the local variables (`user_cards`, `pc_cards`) for every new round, completely avoiding memory leaks from previous games.
* **State Management (Boolean Flags):** Used a `game_over` boolean flag to gracefully handle the user's turn (asking to hit or stand) until a win, bust, or pass condition is met.

## 🎮 Features
* **Dynamic Scoring:** Real-time score calculation and validation for Blackjacks and busts.
* **Custom ASCII Art:** Modularized graphics stored in a separate `art.py` file to display customized banners for the main logo, wins, losses, and draws (`Push!`).
* **Infinite Replayability:** A persistent game loop wraps the entire application, allowing the user to play as many consecutive rounds as they want simply by typing 'y' or 'n'. The console screen wipes clean `os.system('cls')` between matches for a clean UI.

## 🛠️ How to run
Simply execute the `main.py` file in your terminal:
```bash
python main.py