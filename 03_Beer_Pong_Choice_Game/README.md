# 🍻 Beer Pong Bar Adventure

### Project Description
A text-based interactive adventure game designed to demonstrate **logic control flow** in Python. The script simulates a branching narrative where the user must navigate through a series of decisions to achieve a specific goal ("Finding your friends").

### 🕹️ The Scenario
You are navigating a crowded bar environment. Your mission is to bypass distractions and obstacles (like getting lost in the bathroom or being kicked out by the manager) to locate your group at the correct table.

### 🧠 Key Technical Concepts
* **Nested Conditionals:** implementation of deep `if/elif/else` structures to create a decision tree with multiple outcomes.
* **Input Sanitization:** Application of string methods `.lower()` and `.upper()` to normalize user input, making the program robust against case-sensitivity errors (e.g., handling "Left", "left", or "LEFT").
* **UX/UI Elements:** Usage of `os.system('cls')` to clear the terminal for a clean interface and ASCII art integration for visual engagement.
* **Error Handling:** "Catch-all" logic in `else` blocks to handle invalid user inputs gracefully.

### 🚀 How to Run
1. Execute the script in your terminal.
2. Follow the on-screen prompts.
3. Choose wisely! Only one specific path leads to victory (Table B).