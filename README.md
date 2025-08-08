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

### ✅ Alien Fleet Generation
- Created `Alien` class using `pygame.sprite.Sprite`
- Calculated number of aliens per row dynamically
- Aliens drawn in a fleet at the top of the screen
- Foundation laid for future logic (movement, collision, scoring)

### ✅ Alien Fleet Movement
- Aliens now move horizontally as a fleet
- When a fleet hits the screen edge, it drops down and reverses direction
- Controlled using `check_edges()` in each alien and centralized `fleet_direction` in `Settings`
- Prepares the game for bullet-alien collisions and end conditions

### ✅ Bullet-Alien Collision Detection
- Bullets now detect and destroy aliens on contact
- Uses `pygame.sprite.groupcollide()` to efficiently manage collisions
- Entire fleet regenerates after all aliens are destroyed
- Sets the stage for scoring, levels, and win conditions

### ✅ Game Over & Lives System (NEW!)
- Tracks remaining ships using `GameStats`
- Game ends when all ships are lost
- Ships repositioned after being hit, with a short pause before play resumes

---

## 🧠 What I’m Learning

- Object-Oriented Programming in Python  
- Game development basics with `pygame`  
- Version control using **Git** and **GitHub**  
- Professional Git workflows (branching, PRs, commits)

---

## 🔜 Upcoming Features

- Scoring system & levels
- Start/restart game functionality 
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
- **Q / Close** — Quit the game

---


## 📁 Project Structure (so far)
```
alien-invasion/
├── images/
│    ├──ship.bmp
│    └──alien.bmp
├── alien_invasion.py 
├── ship.py
├── alien.py
├── settings.py
├──game_stats.py 
└── README.md
```
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