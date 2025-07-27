# 👾 Alien Invasion (Pygame Project)

A beginner-friendly 2D space shooter game built with **Python** and **Pygame**, following the "Python Crash Course" by Eric Matthes.  
This project is part of my preparation for **Google Summer of Code 2026**.

---

## 🚀 Current Features

- **Game Window Initialized**: 1200x700 screen created using Pygame.
- **Ship Class Added**:
  - Loads a custom spaceship image.
  - Positions the ship at the bottom-center of the screen.
  - Renders the ship using the `blitme()` method.
- **Bullet Firing System**: (NEW!)
  - Press spacebar to shoot bullets upward.
  - Bullets are drawn on screen and move continuously.
  - Uses `pygame.sprite.Sprite` for efficient handling.

---

## 🧠 What I’m Learning

- Object-Oriented Programming in Python  
- Game development basics with `pygame`  
- Version control using **Git** and **GitHub**  
- Professional Git workflows (branching, PRs, commits)

---

## 🔜 Upcoming Features

- Alien fleet generation  
- Bullet-alien collision detection  
- Scoring system & levels  
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

## 📁 Project Structure (so far)
alien-invasion/
├── images/
│ └── ship.bmp
├── alien_invasion.py
├── ship.py
├── bullet.py # NEW
├── settings.py
└── README.md

---

## 🙋‍♂️ About Me

I’m **Sahil**, a passionate learner and aspiring contributor for **Google Summer of Code 2026**.  
This project is part of my self-taught journey in mastering open-source development.

---

## 🌟 Star this repo if you like my progress!
[![GitHub stars](https://img.shields.io/github/stars/CodeWithSahil-alt/alien-invasion?style=social)](https://github.com/CodeWithSahil-alt/alien-invasion)