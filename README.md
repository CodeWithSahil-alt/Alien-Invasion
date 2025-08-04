# 👾 Alien Invasion (Pygame Project)

A beginner-friendly 2D space shooter game built with **Python** and **Pygame**, following the "*Python Crash Course*" by *Eric Matthes*.  
This project is part of my preparation for **Google Summer of Code 2026**.

---

## 🚀 Current Features

### ✅ Game Window Initialized
- 1200x755 screen created using `pygame.display.set_mode()`
- Game loop running with proper event handling (`QUIT`)

### ✅ Ship Class Added
  - Loads a custom spaceship image.
  - Positions the ship at the bottom-center of the screen.
  - Renders the ship using the `blitme()` method.
  - Structured in a separate `Ship` class
  
### ✅ Bullet Firing System
  - Press spacebar to shoot bullets upward.
  - Bullets are drawn on screen and move continuously.
  - Uses `pygame.sprite.Sprite` for efficient handling.
  - Implemented using a `Bullet` class

### ✅ Alien Fleet Generation (NEW!)
- Created `Alien` class using `pygame.sprite.Sprite`
- Calculated number of aliens per row dynamically
- Aliens drawn in a fleet at the top of the screen
- Foundation laid for future logic (movement, collision, scoring)

---

## 🧠 What I’m Learning

- Object-Oriented Programming in Python  
- Game development basics with `pygame`  
- Version control using **Git** and **GitHub**  
- Professional Git workflows (branching, PRs, commits)

---

## 🔜 Upcoming Features
 
- Add alien fleet movement (horizontal + drop down)
- Bullet-alien collision detection
- Scoring system & levels
- Add game over condition 
- Sound effects and animations  

---

## ⚙️ How to Run

1. Install [Python](https://www.python.org/) and [Pygame](https://www.pygame.org/):
    ```bash
    pip install pygame
    ```

2. Clone this repo:
    ```bash
    git clone https://github.com/CodeWithSahil-alt/alien-invasion.git
    cd alien-invasion
    ```

3. Run the game:
    ```bash
    python alien_invasion.py
    ```

---

## 🎮 Controls

- **Left / Right Arrows** — Move ship horizontally
- **Spacebar** — Fire bullets
- **X / Close** — Quit the game

---


## 📁 Project Structure (so far)
alien-invasion/  
├── images/  
│ └── ship.bmp  
├── alien_invasion.py  
├── ship.py  
├── alien.py # NEW  
├── settings.py  
└── README.md

---

### 🤝 Contribution
This is a solo learning project for now. If you're reading this and want to give feedback or suggestions — feel free!

---

### 📚 Credits

- [Python Crash Course by Eric Matthes](https://nostarch.com/pythoncrashcourse2e)
- [Pygame Documentation](https://www.pygame.org/docs/)

---

## 🙋‍♂️ About Me

I’m **Sahil**, a passionate learner and aspiring contributor for **Google Summer of Code 2026**.  
This project is part of my self-taught journey in mastering open-source development.

---

## 🌟 Star this repo if you like my progress!
[![GitHub stars](https://img.shields.io/github/stars/CodeWithSahil-alt/alien-invasion?style=social)](https://github.com/CodeWithSahil-alt/alien-invasion)