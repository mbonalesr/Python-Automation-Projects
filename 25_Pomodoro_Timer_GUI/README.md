# Mau's Pomodoro App 🍅

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-lightgrey?style=for-the-badge)

A minimal, productivity-boosting Pomodoro timer built entirely with Python and the Tkinter GUI library. This application helps you manage your study or work sessions using the classic Pomodoro Technique, automatically alternating between focus blocks and breaks.

## Features
* **Automated Cycles:** Automatically switches between Work, Short Break, and Long Break phases.
* **Dynamic UI:** The interface changes titles and colors depending on the current phase to keep you visually cued.
* **Visual Tracking:** Earn a checkmark (✔) for every completed work session.
* **Full Reset:** A reset button that instantly halts the timer, clears your progress, and returns the application to its initial state.

## The Pomodoro Logic Applied
1. **Work Session:** 25 minutes (Adjustable in constants).
2. **Short Break:** 5 minutes.
3. Every 4th Work Session triggers a **Long Break** (20 minutes).

## Prerequisites
* Python 3.x installed on your machine.
* Tkinter (Usually comes pre-installed with standard Python distributions).

## Installation and Setup
1. Clone this repository to your local machine.
2. Ensure you have the `tomato.png` image file in the same directory as your main Python script.
3. Run the script from your terminal:
   ```bash
   python main.py