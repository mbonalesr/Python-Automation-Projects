# 🔐 Caesar Cipher - Python Encryption Project

A console-based Python program that encrypts and decrypts messages using the classic Caesar Cipher technique. 

## 🧠 Technical Concepts Applied
* **Mathematical Logic (Modulo Operator):** Implemented `(index + shift) % 26` to elegantly wrap around the alphabet list, allowing for infinite shift numbers without throwing an `IndexError`.
* **Functions with Inputs:** Passed arguments (`original_text`, `shift_amount`, `direction`) to a core processing function.
* **Edge Case Handling:** Designed the algorithm to detect and preserve numbers, spaces, and special symbols without attempting to shift them.
* **State Management:** Used a boolean flag (`should_continue`) to wrap the program in a `while` loop, allowing the user to encode/decode multiple messages in a single session.

## 🎮 Features
* **Encode / Decode:** Choose to encrypt a secret message or crack an existing one.
* **Robust Shift:** Handles any integer shift, no matter how large.
* **Data Integrity:** Keeps your punctuation and spacing exactly as you typed it.

## 🛠️ How to run
Simply execute the `main.py` file in your terminal:
```bash
python main.py