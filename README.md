# Mini Bingo Game

A simple, terminal-based Bingo game built with Scrum: small, focused sprints, clear acceptance criteria, and a clean, testable codebase.  
This README covers the project vision, rules, backlog, Sprint 1 scope, structure, and how to run/tests.

---

## Overview & Vision
Our goal is to build a **simple, fair, and accessible** Bingo game you can play in the terminal. It should be easy to use, support multiple players (bots included), offer continuous play with clear feedback, and scale with future sprints.

---

## Core Rules (MVP)
- **Card:** 3×5 matrix (3 rows, 5 columns) with **15 numbers**.
- **Number range:** **1–90** (inclusive).
- **Draws:** Numbers are drawn **randomly without repetition**.
- **Claiming wins:** The **player manually claims** `line` or `bingo`.
- **Points:** The game uses a points system (starting points, entry cost, rewards, penalties).
- **Game-mode:** Choose the game-mode which best suits the difficulty you are seeking (easy, medium or hard).

**Points system (project-level rule):**
- Start with **20** points.  
- **–2** points to enter each round.  
- **+10%** of the point pool for a **line**; **+50%** for **bingo**.  
- **–1** for an incorrect number input.  
- **–3** for a false `line`/`bingo` claim.

---

## Product Backlog (Summary)
1. Allocate a 3×5 Bingo card to the player.  
2. Draw numbers randomly without repetition and display turn-by-turn.  
3. Allow inputs per turn within a time window (`Y/N` to mark; then `L`/`B`/`N`).  
4. Handle invalid inputs gracefully.  
5. Display clear win notifications (line/bingo + rewards + current points).  
6. Implement the points system (start, bets, wins/losses, penalties).  
7. Provide a clear instructions screen.  
8. Add multiplayer (bots) with difficulty presets.  
9. Offer different game modes (e.g., fast/long; matrix sizes).

(Full details live in `docs/`.)

---

## User Stories
- As a developer I want to make the game unambiguous, allowing the user to easily navigate the (T)UI and play with minimum friction/confusion, without getting stuck, so that each user has a standardized, fun time.  
- As an elderly person I want to see clear instructions so that I can understand how to play and enjoy the game easily.  
- As a player, I want to play a simple, stimulating game with small and big wins where I manage my credits, so that I feel the risk/reward feeling and have fun without thinking too much.  
- As a player I want to manually claim wins (line or bingo) so that I feel more engaged with the game.  
- As a player I want to have a clear notification (pop-up message) so that I know when I win (either a line or bingo).  
- As a player, I want to have a quick-start option so that I can immediately begin playing without going through many menus.  
- As a player with limited tech knowledge, I want a simple layout with big, readable buttons so that I can navigate the game without confusion.  
- As a player I want to choose the number of players I play against simultaneously so that I can adjust the level of competition and difficulty. 

---

## Acceptance Criteria (Project-Level)
- **Bingo Card Validity:** Each player receives a 3×5 card with **15 unique** numbers within **1–90**, clearly displayed.  
- **Number Calling:** Numbers are drawn randomly **one by one** without repetition and shown to the player.  
- **Marking & Tracking:** When a drawn number is on the player’s card, the card can be marked (manually in early sprints) and remains visible.  
- **Win Detection:** The game accepts a player’s **manual win claim** (`line` or `bingo`) and responds with a clear notification and the appropriate point update.

---

## Sprint 1
**Goal:** *Have the player be allocated a valid bingo card where 15 random numbers are placed without repetition and the card is displayed.*

**Sprint Backlog**
- Generate an empty **3×5** bingo card.  
- Generate **15 unique random** numbers (**1–90**).  
- Randomly allocate the numbers to the card slots.  
- Display the completed card in the terminal.

**Definition of Done**
- Card is generated as a **3×5** grid filled with **15 unique** numbers in **1–90**.  
- Numbers are **randomly distributed** (not sequential).  
- The card is **clearly displayed** in the terminal (readable alignment/spacing).  
- Multiple runs consistently produce valid cards (dimensions, uniqueness, range).  
- Code has tests for grid creation, uniqueness, range, and basic rendering.  
- Code runs without errors, is reviewed, and is committed to the repository with updated docs.

**Duration:** 1 week

---

## Project Structure
```
mini_bingo_game/
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   └── settings.yaml
│   └── game/
│       ├── __init__.py
│       ├── bingo_card.py
│       ├── number_draw.py
│       ├── player.py
│       └── input_handler.py
│
├── tests/
│   ├── __init__.py
│   ├── test_bingo_card.py
│   ├── test_number_draw.py
│   ├── test_player.py
│   └── test_input_handler.py
│
└── docs/
    ├── index.md
    └── gameplay_instructions.md
```

---

## Getting Started

### Prerequisites
- **Python 3.10+**
- Recommended: a virtual environment (`venv`)

### Setup
```bash
git clone https://github.com/elias-alaoui/mini-bingo-project.git
cd mini-bingo-project

python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

### Run (Sprint 1)
```bash
python -m src.main
```
This generates and prints a randomized **3×5** Bingo card to the terminal.

### Tests
```bash
pytest
```

---

## Configuration
Basic game settings live in `src/config/settings.yaml`. Example:
```yaml
board:
  rows: 3
  cols: 5
  number_range: [1, 90]

points:
  start: 20
  round_entry: 2
  line_reward: 0.10
  bingo_reward: 0.50
  wrong_input_penalty: -1
  wrong_claim_penalty: -3

modes:
  easy_bots: 4
  medium_bots: 9
  hard_bots: 19
```

---

## Tech Stack
- **Python** (terminal-based app)
- **Pytest** for tests
- **YAML** for configuration

---

## Team
**Group 1:** Amir Natan, Elias Alaoui, Marc Montull, Kilian Llopis, Fiore De Vito, Gerard Figueras

---

## License
This project is licensed under the **MIT License** — see `LICENSE` for details.
