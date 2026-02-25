# 🔨 Secret Auction - Python Console Project

A terminal-based blind auction program. It allows multiple users to place bids secretly by clearing the console after each turn, ensuring privacy. Once all bids are in, it calculates and announces the highest bidder.

## 🧠 Technical Concepts Applied
* **Dictionaries (Key-Value Pairs):** Used to store and link each bidder's name (key) with their respective bid amount (value).
* **Dictionary Iteration:** Utilized the `.items()` method in a `for` loop to scan through all entries and mathematically determine the maximum bid.
* **Control Flow & State Management:** Implemented a `while` loop that keeps the auction running until the user explicitly types 'no'.
* **Console Manipulation:** Used `os.system('cls')` to clear the terminal screen between users, practically solving the "secret" aspect of the blind auction.

## 🎮 Features
* **Blind Bidding:** The screen wipes clean after every bid so the next person can't see previous offers.
* **Dynamic Winner Calculation:** Automatically evaluates all stored bids at the end to declare the winner.
* **Input Validation:** Gracefully ends the auction if an invalid command is typed when asked for more bidders.

## 🛠️ How to run
Simply execute the `main.py` file in your terminal:
```bash
python main.py