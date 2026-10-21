# Checkers AI

A game of Checkers in Python and Pygame where you play against a computer opponent that searches the game tree with **Minimax**.

![A mid-game position: red pieces against the Minimax-controlled white pieces](docs/images/screenshot.png)

## Play in the browser

**[Play it live](https://shreyask06.github.io/checkerAiPy/)**: the same `main.py` compiled to WebAssembly with [pygbag](https://github.com/pygame-web/pygbag) and deployed by GitHub Actions on every push to `main` (the first load downloads the Python runtime, so give it a few seconds, then click the page to start).

## Run it locally

Requires Python 3.9+.

```bash
pip install pygame
python main.py
```

You play red with the mouse: click a piece to see its valid moves highlighted, then click a destination. The computer plays white and answers immediately.

## How the AI works

- **Search:** Minimax to a fixed depth of 3 plies. The computer expands every legal move for both sides, including multi-jump sequences, and picks the line with the best evaluation.
- **Evaluation:** `white pieces - red pieces + 0.5 x (white kings - red kings)`, so a king counts as worth half a piece more than a regular piece.
- **Rules:** diagonal moves, captures with multi-jumps, promotion to kings, and win detection after every move.

## Project structure

```
main.py                     Pygame loop: input, AI turn, win messages
CheckersAI/
  board.py                  Board state, move generation (including jumps), evaluation
  game.py                   Turn handling, piece selection, move application
  piece.py, constants.py    Piece drawing, colours, board dimensions
  crown.png                 King marker
  minimax/algorithm.py      Minimax search and move enumeration
```

## Roadmap

- Alpha-beta pruning, which would allow a deeper default search at the same speed.
- A richer evaluation function (back-row control, centre control, mobility).
- Selectable difficulty and unit tests for move generation and jump rules.

## Tech stack

Python, Pygame.
