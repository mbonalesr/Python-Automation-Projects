# Flashy - CAE Vocabulary Flashcards 🇬🇧

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)

## 📝 Description
Flashy is a Python-based GUI desktop application designed to help users study and memorize Advanced English (C1/CAE) vocabulary efficiently. It uses the flashcard methodology, presenting a word on the front and revealing its definition on the back after a brief delay. 

The application features a smart progression system that saves your learning history, ensuring you only review the words you haven't mastered yet.

## ✨ Features
* **Automated Flipping:** Cards automatically flip after 3 seconds to reveal the definition.
* **Smart Progress Tracking:** Words marked as "known" (✅) are removed from the active deck and saved locally using Pandas.
* **Persistent State:** The app remembers your progress between sessions. If closed, it resumes exactly where you left off.
* **Clean UI:** Built with Tkinter Canvas for a smooth, distraction-free studying experience.

## 🛠️ Prerequisites
* Python 3.x
* Pandas library (`pip install pandas`)

## 🚀 How to Use
1. Run the `main.py` file.
2. Read the C1 vocabulary word on the screen.
3. Wait 3 seconds for the card to flip and reveal the English definition.
4. Click the ✅ button if you knew the word (it won't appear again).
5. Click the ❌ button if you didn't know it (it remains in the deck for future review).

## 🎓 Acknowledgements
This project was developed as part of a personalized learning journey to master Python GUI development and prepare for the **Certificate in Advanced English (CAE)**.