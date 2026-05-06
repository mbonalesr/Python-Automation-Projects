# Turtle Crossing Game 🐢🚗

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![OOP](https://img.shields.io/badge/Architecture-OOP-success)

A classic arcade-style crossing game built entirely in Python using the built-in `turtle` module. The objective is simple: guide your turtle safely across a busy multi-lane highway without getting run over. Every time you successfully cross, the traffic speed increases!

This project was developed to solidify concepts of Object-Oriented Programming (OOP), state management, and collision detection in a visual environment.

## 🎮 Features
* **Object-Oriented Architecture:** Clean separation of concerns using Python classes.
* **Dynamic Difficulty:** Traffic speed automatically increases as the player reaches higher levels.
* **Collision Detection:** Accurate distance tracking between the player and moving obstacles.
* **Procedural Generation:** Cars are spawned at random intervals and positions using probability logic.

## 🏗️ Architecture & UML Diagram
The project relies on OOP principles, specifically using Inheritance from Python's built-in `Turtle` class for entities that require rendering on the screen.

```mermaid
classDiagram
    class Turtle {
        <<Library Module>>
        +shape()
        +penup()
        +setposition()
    }

    Turtle <|-- Player
    Turtle <|-- Scoreboard

    class Scoreboard {
        -tuple FONT
        +int level
        +update_level()
        +game_over()
    }

    class Player {
        -tuple STARTING_POSITION
        -int MOVE_DISTANCE
        -int FINISH_LINE_Y
        +go_up()
        +is_at_finish_line()
        +return_to_start()
    }

    class CarManager {
        -list COLORS
        -int STARTING_MOVE_DISTANCE
        -int MOVE_INCREMENT
        +list all_cars
        +int car_speed
        +create_car()
        +move_cars()
        +more_speed()
    }

    class GameManager {
        <<main.py>>
    }
    
    GameManager ..> Player : controls
    GameManager ..> CarManager : manages
    GameManager ..> Scoreboard : updates