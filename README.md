# 🚢 Terminal Battleship Simulator

A classic turn-based **Battleship game** playable in the terminal, built entirely with **Python**. This project was created as part of my coursework for **COMP112: Introduction to Programming** and served as one of my first explorations of logic, state tracking, and user input in a text-based game environment.

 **Completed**: December 3, 2022  
 **Course**: COMP112-01  
 **Author**: Kido Douglas

---

## 🌟 Highlights

-  **Player vs Computer** – Engage in a turn-based battle against a CPU opponent.
-  **Random Ship Placement** – Each game is unique with randomized ship layouts for both sides.
-  **Coordinate-Based Attacks** – Guess row and column to strike enemy ships.
-  **Win/Loss Conditions** – The game ends when all of one player’s ships are destroyed.
-  **Custom Grid Layout** – 9x9 playing field labeled A–I and 1–9.

---

## 📖 Overview

This terminal-based Battleship game simulates the classic board game in a 9x9 grid format. Players and the CPU each have hidden ships scattered across their boards. Each turn, both participants guess coordinates to "fire" at the opposing board.

### Game Features

- Ship types:
  - 4 single-tile ships
  - 3 double-tile ships (horizontal or vertical)
  - 2 triple-tile ships (horizontal or vertical)
- Input validation for coordinates
- Computer opponent makes random guesses
- Boards update after each round with:
  - `'x'` for hits
  - `'0'` for misses
- Printed ASCII boards show progress after each turn

---

## 🎮 How to Play

1. Run the script using Python:
   ```bash
   python battleship.py

## 📓 Reflection 

Though this was an introductory project, it lacks the complexities for it to be considered fully fledged.

### Plans for the future
- Adding difficulty levels for the cpu
- implementing a symbol Gui using pygame

