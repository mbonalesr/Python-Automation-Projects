# 🔐 Secure Password Generator

### Project Description
A security tool designed to generate strong, randomized passwords based on user specifications. Unlike simple generators, this script creates a completely shuffled mix of characters to maximize entropy and security.

### Key Features
* **Customizable Complexity:** Users define the exact count of letters, numbers, and symbols.
* **Randomization Engine:** Uses `random.choice()` for selection and `random.shuffle()` to prevent predictable patterns.
* **Optimization:** Implements efficient list-to-string conversion using `.join()`.

### Usage
Run the script, input the desired number of each character type, and copy the generated password.