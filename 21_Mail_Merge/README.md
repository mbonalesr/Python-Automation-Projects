# Automated Mail Merge ✉️🚀
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![TXT](https://img.shields.io/badge/TXT-File-4A4A4A?style=flat)

A fast and efficient Python automation script that takes a template letter and a list of invitees, merging them to generate individualized text files ready for sending.

This project was developed to master file handling, directory navigation via relative paths, and string manipulation techniques in Python without relying on external libraries.

## 🚀 Features
* **Batch Automation:** Instantly generates dozens of personalized .txt files in a fraction of a second, saving hours of manual copy-pasting.

* **Automatic Data Cleaning:** Sanitizes raw input data on the fly by removing unwanted blank lines or spaces (using .strip()) and ensuring proper name capitalization (using .title()).

* **Safe Memory Management:** Utilizes Python's with open() context managers to ensure files are safely processed and automatically closed after operations to prevent memory leaks.

## 🏗️ Architecture & Logic
The script relies on built-in Python methods to read, process, and write data efficiently across different nested directories:

* **Data Extraction (.read() vs .readlines()):** Extracts the master template as a single continuous string, while parsing the list of names as an iterable list, making it easy to loop through each person.

* **String Manipulation (.replace()):** Searches the master letter for the specific [name] placeholder and dynamically swaps it with the sanitized string of the current iteration.

* **Dynamic Pathing:** Navigates cleanly through the project's folder structure (Input/Names/, Input/Letters/, and Output/ReadyToSend/), ensuring that all newly generated invitations are neatly organized in their designated output directory.