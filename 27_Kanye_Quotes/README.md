# Kanye Quotes App 🎤💬

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)
![API](https://img.shields.io/badge/API-Requests-brightgreen?style=for-the-badge)

## 📝 Description
The Kanye Quotes App is a lightweight Python graphical user interface (GUI) application that fetches and displays random, iconic quotes from Kanye West in real-time. 

Every time the user clicks on the interactive button, the app makes a live network request to a public API, parses the incoming data, and seamlessly updates the UI with a new quote.

## ✨ Features
* **Real-Time API Integration:** Uses the `requests` library to connect to the external `api.kanye.rest` endpoint.
* **JSON Parsing:** Efficiently handles and extracts specific data fields from the server's JSON response.
* **Error Handling:** Implements HTTP status code checking to ensure reliable connections.
* **Interactive UI:** Built with Tkinter Canvas, featuring an engaging graphical layout and custom image buttons.

## 🛠️ Prerequisites
* Python 3.x
* `requests` library (`pip install requests`)
* `background.png` and `kanye.png` image files in the same directory as the script.

## 🚀 How to Use
1. Clone or download the repository to your local machine.
2. Ensure you have an active internet connection to reach the API.
3. Run the `main.py` file.
4. Click on Kanye's face to fetch and display a brand new quote!

## 🎓 Acknowledgements
This project was developed as part of a personalized learning journey to master interacting with web APIs, handling GET requests, and integrating external data into Python GUI applications.