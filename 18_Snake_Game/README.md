# Classic Snake Game 🐍

A Python recreation of the classic arcade Snake game, built entirely using Object-Oriented Programming (OOP) principles and the `turtle` graphics library.

## 🚀 Features

* **Object-Oriented Architecture:** The game logic is strictly divided into distinct classes (`Snake`, `Food`, `Scoreboard`) for maintainability and clean code.
* **Dynamic Score Tracking:** Real-time scoreboard that tracks current points and displays a "GAME OVER" sequence upon collision.
* **Collision Detection:** Precise mathematical distance tracking to detect when the snake consumes food, hits the screen boundaries, or collides with its own tail.

## 📁 Project Structure

* `main.py`: The game engine. Handles screen setup, event listening (keyboard inputs), and the main game loop.
* `snake.py`: Contains the `Snake` class. Manages the creation of segments, movement logic, and directional controls.
* `food.py`: Contains the `Food` class (inherits from Turtle). Handles random coordinate generation for food placement.
* `scoreboard.py`: Contains the `Scoreboard` class (inherits from Turtle). Manages score updates and text rendering on the screen.

## 🎮 How to Play

1. Run the `main.py` file to start the game.
2. Use the **Arrow Keys** (Up, Down, Left, Right) to navigate the snake.
3. Eat the blue food dots to grow your tail and increase your score.
4. Don't hit the walls or your own tail!

```mermaid
classDiagram
    class Turtle
    
    class Food {
        +refresh()
    }
    
    class Scoreboard {
        +int score
        +refresh_score()
        +game_over()
    }
    
    class Snake {
        +list segments
        +Turtle head
        +generate_snake()
        +extend()
        +add_segment()
        +movement()
        +go_up()
        +go_down()
        +go_left()
        +go_right()
    }

    Turtle <|-- Food
    Turtle <|-- Scoreboard