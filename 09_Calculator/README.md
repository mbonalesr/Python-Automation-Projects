# 🧮 Python Calculator - Console Project

A fully functional, terminal-based calculator. It performs basic arithmetic operations and allows the user to chain multiple calculations together, using the previous result as the starting point for the next operation.

## 🧠 Technical Concepts Applied
* **Functions with Outputs:** Structured modular functions (`add`, `subtract`, `multiply`, `divide`) utilizing the `return` keyword to pass data back to the main program.
* **First-Class Functions:** Stored function references as values inside a Python Dictionary (`operations`). This allows the program to dynamically select and execute the correct mathematical operation based on the user's string input (e.g., `"+"`, `"-"`).
* **State Management (Chaining):** Implemented a `while` loop that successfully feeds the `answer` variable back into `num_1` if the user chooses to continue calculating.
* **Recursion (App Reset):** Handled the "new calculation" feature by clearing the console (`os.system('cls')`) and recursively calling the `calculator()` function to start a completely fresh session.
* **Docstrings:** Documented each mathematical function with explicit Python docstrings for professional readability.

## 🎮 Features
* **Continuous Operations:** Keep adding, subtracting, multiplying, or dividing from your current total without starting over.
* **Clean Slate:** Instantly wipe the screen and memory to start a brand new calculation.
* **Input Handling:** Detects invalid continue/reset choices and gracefully breaks the loop.

## 🛠️ How to run
Simply execute the `main.py` file in your terminal:
```bash
python main.py