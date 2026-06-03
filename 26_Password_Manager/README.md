# 🔐 Mau's Password Manager
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/Tkinter-31A8FF?style=for-the-badge)
![JSON](https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white)

A sleek and secure desktop application built with Python that helps you generate, store, and manage your passwords locally. 

## 🚀 Features

* **Secure Password Generation:** Automatically creates strong, random passwords using a mix of letters, numbers, and symbols.
* **Local Storage:** Saves your credentials (website, email, and password) securely in a local `data.json` file.
* **Smart Search:** Quickly retrieve your saved passwords by searching for the website name.
* **Clipboard Integration:** Automatically copies newly generated passwords to your clipboard for instant use.
* **Error Handling:** Built-in safeguards to prevent empty entries and gracefully manage missing data files.

## 🛠️ Technologies Used

* **Python 3:** Core programming language.
* **Tkinter:** Built-in Python library for creating the Graphical User Interface (GUI).
* **JSON:** Used for structuring, reading, and updating the local database.
* **Pyperclip:** Cross-platform Python module for clipboard operations.

## 💻 How to Use

1. Clone this repository or download the source code.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pyperclip