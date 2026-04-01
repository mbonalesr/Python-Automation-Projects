# ☕ Coffee Machine Simulator - Python Console Program

A fully functional, text-based Virtual Coffee Machine built in Python. It handles inventory management, processes user payments (using Mexican Pesos), calculates exact change, and dynamically evaluates complex dictionary structures to fulfill user orders.

![Coffee Machine Flowchart](./diagram.png) 
*(Note: Replace `./diagram.png` with the actual path to your flowchart image)*

## 🧠 Technical Concepts Applied
* **Dictionary Navigation & Cross-referencing:** Implemented an advanced data evaluation system to compare two separate dictionaries simultaneously. The program uses a dynamic key (`ingredient`) to cross-reference the machine's current `resources` against the specific `MENU` requirements for the chosen drink.
* **Global vs. Local Scope:** Successfully managed state across the application by using the `global` keyword to update the machine's total `profit` inside the transaction function, without causing scope conflicts.
* **Continuous State Management:** Wrapped the core logic in a continuous `while` loop controlled by a boolean flag (`machine_operating`), ensuring the machine runs indefinitely for multiple users until a maintenance command is issued.
* **Modular Architecture:** Kept the main executable script clean by separating concerns. The ASCII art is stored in `art.py`, and the machine's starting inventory and menu dictionaries are isolated in `machine_data.py`.

## 🎮 Features
* **Smart Inventory Validation:** Before accepting any money, the machine checks if it has enough water, milk, and coffee to fulfill the specific order. If a resource is missing, it alerts the user and cancels the transaction.
* **Dynamic Coin Processor:** Asks the user to insert specific Mexican coins ($10, $5, $2, $1 MXN). It calculates the total, compares it to the drink's cost, and either returns the exact change or issues a full refund if the funds are insufficient.
* **Hidden Admin Commands:** Includes secret developer commands for maintenance. Typing `report` prints a formatted string of the current resource levels and total profit, while typing `off` safely terminates the program loop.
* **Real-time Resource Depletion:** Once a transaction is successful, the machine dynamically subtracts the exact ingredient amounts used from its global inventory.
