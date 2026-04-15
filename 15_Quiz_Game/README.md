# 🐍 Object-Oriented Quiz Game

A terminal-based trivia game built from the ground up to practice Python's Object-Oriented Programming (OOP) principles. The project is an essential milestone in the 100 Days of Code course.

## 🚀 Overview

This quiz game fetches a question database and presents them to the user in a terminal interface. The code is structured into separate, interoperable classes, ensuring clean code, easier maintainability, and scalability. It handles user inputs (True/False) with validation to prevent logical errors.

## ✨ Features

- **Object-Oriented Architecture:** Clear separation of concerns between data, class models, and game logic.
- **Robust Input Validation:** The game only accepts `True` or `False` (case-insensitive). Invalid inputs prompt the user to try again, preventing runtime crashes.
- **Score Tracking:** Displays the current score after each question and a final score summary.
- **Clean Interface:** Clears the terminal screen before the quiz for a focused experience.
- **Extensible:** The question database can easily be expanded or replaced with external sources.

## 📐 Architecture & Logic Documentation

To ensure maintainability and a clear understanding of the system, this project includes visual documentation:
- **UML Class Diagram:** Maps the attributes, methods, and the 1-to-many association between the `QuizBrain` controller and the `Question` data models.
- **Logic Flowchart:** Details the execution path, including the initialization loop and the main `while` game loop.

## 📂 Project Structure

- `main.py`: The entry point of the game. It controls the game loop and orchestrates interaction between all components.
- `quiz_brain.py`: Contains the `QuizBrain` class, which manages the quiz logic, score keeping, and answer checking.
- `question_model.py`: Defines the `Question` class, which acts as a structured model for a single trivia question.
- `data.py`: A database of trivia questions and their correct answers.

## 🛠️ How to Run

1.  Make sure you have Python 3 installed.
2.  Clone this repository to your local machine.
3.  Navigate to the project directory in your terminal.
4.  Run the main game file:
    ```bash
    python main.py
    ```

## 🎮 Game Flow

1.  The program reads the data and initializes the `QuizBrain` with a list of `Question` objects.
2.  The terminal screen is cleared, and the quiz logo is displayed.
3.  Questions are presented one by one. The user types `True` or `False` for their answer.
4.  If correct, the score increases. The current score and the correct answer are shown.
5.  The loop continues until `still_has_questions()` returns False.
6.  A final score summary is displayed before exiting.

## 🎓 Inspiration

This project was built as a component of Angela Yu's "100 Days of Code: The Complete Python Pro Bootcamp".

## 📜 License

[MIT](https://choosealicense.com/licenses/mit/)