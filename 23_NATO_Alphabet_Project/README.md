# NATO Phonetic Alphabet Translator 🔤✈️

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=flat&logo=pandas)

A clean, command-line Python application that translates any user-provided word into its corresponding NATO phonetic alphabet sequence. The program incorporates advanced exception handling to ensure a crash-free and smooth user experience.

This project was developed to solidify core Python concepts, specifically data extraction with the pandas library, Dictionary/List Comprehensions, and Exception Handling (`try/except/else`).

## 🎮 Features
* **Efficient Data Processing:** Reads and processes CSV data automatically using the pandas library.
* **Robust Error Handling:** Utilizes `try / except / else` blocks to actively catch `KeyError` exceptions when a user inputs numbers, spaces, or special characters, preventing the program from crashing.
* **Recursive Prompting:** If an invalid input is detected, the program elegantly triggers its own function recursively (`generate_phonetic()`) to prompt the user again without breaking the flow.
* **Optimized Memory Usage:** Loads the CSV file and builds the translation dictionary only once at startup, rather than on every user input.

## 🏗️ Architecture & Logic
The project relies on advanced Python concepts to handle data parsing and translation efficiently:

* **Dictionary Comprehension & iterrows():** Converts the `nato_phonetic_alphabet.csv` file into a clean Python dictionary format (e.g., `{'A': 'Alfa', 'B': 'Bravo'}`) by iterating through the Pandas DataFrame rows.
* **Exception-Driven Logic (EAFP):** Instead of using complex `if` statements to filter input beforehand, it attempts a List Comprehension directly. If an unmapped character is found, the `except KeyError` block cleanly catches the issue and handles the mistake.