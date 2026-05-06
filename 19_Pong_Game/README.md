# Classic Pong Game 🏓

A Python implementation of the classic arcade game Pong, built using Object-Oriented Programming (OOP) and the `turtle` graphics library. 

## 🚀 Features
* **OOP Architecture:** Codebase separated into distinct, manageable classes (`Ball`, `Paddle`, `Scoreboard`).
* **Dynamic Speed:** The ball accelerates by 10% after every successful paddle hit, increasing difficulty.
* **Collision Detection:** Accurate boundary and paddle collision mechanics.
* **Live Score Tracking:** Automatic score updating and reset upon missing the ball.

## 🛠️ Prerequisites
* Python 3.x
* `turtle` module (comes pre-installed with standard Python library)

## 🎮 How to Play
1. Clone this repository to your local machine.
2. Run `main.py` from your terminal or IDE.
3. The game starts immediately.

**Controls:**
* **Left Player:** `W` (Up) / `S` (Down)
* **Right Player:** `Up Arrow` / `Down Arrow`

## 🧠 What I Learned
This project was built to strengthen my understanding of Object-Oriented Programming, state management, and class inheritance in Python.

## UML Diagram
```mermaid
classDiagram
    class Turtle

    class main {
        +bool game_on
    }
    
    class Paddle {
        +tuple position
        +go_up()
        +go_down()
    }
    
    class Scoreboard {
        +int left_score
        +int right_score
        +update_score()
        +left_point()
        +right_point()
    }
    
    class Ball {
        +move_and_bounce_y()
        +bounce_x()
        +reset_position()
    }

    Turtle <|-- Paddle
    Turtle <|-- Ball
    Turtle <|-- Scoreboard

    main ..> Ball
    main ..> Paddle
    main ..> Scoreboard