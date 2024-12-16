# Flappy Bird Game

## Overview
This project is a **Flappy Bird clone** implemented in Python using the **Pygame library**. The game features smooth gameplay, dynamic obstacles, real-time scoring, and a game-over screen with restart functionality. It is a fun demonstration of Python programming and game development concepts.

---

## Features

### Gameplay Mechanics
- **Bird Movement**: The bird moves automatically and falls due to gravity.
  - Press **SPACE** to make the bird jump.
- **Dynamic Obstacles**:
  - Randomly generated pipes move across the screen with a vertical gap.
  - New pipes appear when old ones move off the screen.
- **Score Tracking**: The score increases when the bird passes through pipes.
- **Game Over**:
  - Collision with pipes or screen boundaries ends the game.
  - Press **SPACE** to restart after a game-over screen.

### Visual and Audio Elements
- **Bird and Pipe Graphics**: Custom images for the bird and pipes.
- **Score Display**: The current score is displayed in real-time.

---

## Prerequisites
- **Python 3.8 or above**
- **Pygame library**

Install Pygame using pip:
```bash
pip install pygame
```

---

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/roeeBuchler/FlappyBird.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd FlappyBird
   ```

3. **Add required game assets**:
   Ensure the following assets are in the project directory:
   - `bird.png` (bird graphic)
   - `pipe_down.png` (downward pipe)

4. **Run the game**:
   ```bash
   python main.py
   ```

---

## Gameplay Instructions
- Press **SPACE** to make the bird jump.
- Avoid colliding with the pipes or the edges of the screen.
- Keep passing through the pipes to increase your score.
- When the game ends, press **SPACE** to restart.

---

## File Structure
```
FlappyBird/
│-- main.py             # Main game logic
│-- bird.png            # Bird sprite
│-- pipe_down.png       # Downward-facing pipe graphic
│-- pipe_up.png         # Upward-facing pipe graphic
│-- README.md           # Project documentation
```

---

## Skills Demonstrated
- **Python Programming**: Object-oriented design for modular game components.
- **Game Development**: Real-time collision detection, scoring, and smooth gameplay mechanics.
- **Pygame**: Handling graphics, events, and game loops effectively.
- **Problem Solving**: Implementing dynamic obstacles and responsive controls.

---

## Future Enhancements
- Add sound effects for jumps and collisions.
- Implement multiple difficulty levels with increasing pipe speed.
- Add animations for enhanced visuals.
- Include a high-score leaderboard.

---

![image](https://github.com/user-attachments/assets/7641e1c9-698d-4b72-afed-d3e6116df10b)


**Project by Roee Buchler**
