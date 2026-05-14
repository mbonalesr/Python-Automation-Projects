# U.S. States Educational Game 🗺️📍

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Turtle](https://img.shields.io/badge/GUI-Turtle-green?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=flat&logo=pandas)

An interactive, graphical desktop game built in Python that tests your knowledge of United States geography. The objective is to name all 50 states. When a user guesses correctly, the state's name is dynamically written on a blank map at its exact geographical coordinates.

This project was developed to combine graphical user interfaces (GUI) using the turtle module with powerful data manipulation using the pandas library.

## 🚀 Features
* **Interactive GUI:** Utilizes turtle.Screen() and custom .gif images to create a visually engaging, clickable game environment with text input popups.

* **Smart Input Handling:** Automatically formats user input using .title() to ensure case-insensitive matching (e.g., typing "texas", "TEXAS", or "Texas" are all accepted).

* **Live Progress Tracking:** The popup dialog box dynamically updates the user's score (e.g., "15/50 States Correct") while the game loop runs.

* **Study Mode Export:** If the user types "Exit", the game immediately halts and generates a states_to_learn.csv file containing only the states they missed, perfect for later studying.

## 🏗️ Architecture & Logic
The codebase efficiently bridges the gap between raw CSV data and visual screen coordinates:

* **Data Extraction & Filtering:** Reads the 50_states.csv file using pandas. It extracts the specific row for a correctly guessed state (data[data.state == answer_state]) and uses the .item() method to pull the pure integer values for the X and Y coordinates, avoiding label conflicts.

* **Coordinate Mapping:** A hidden turtle object is programmatically dispatched to the exact (x, y) coordinates retrieved from the dataset to stamp the state's name on the map.

* **List Comprehensions:** Upon exiting, a single-line Python list comprehension ([state for state in states if state not in guessed_states]) efficiently compares the master list of states against the user's guesses to isolate the missing ones.

* **Automated Data Export:** Converts the newly generated list of missing states back into a Pandas DataFrame and exports it directly to a CSV file.