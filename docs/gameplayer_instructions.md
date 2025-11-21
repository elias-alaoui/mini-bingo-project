# Mini Bingo — Gameplay Instructions

Welcome to the Mini Bingo game! This guide explains how to play, what commands to use, and how points work.

---

## 1. Objective

You are given a **3 × 5 Bingo card** (15 unique numbers between 1 and 90).

Numbers are drawn randomly, **one per turn**, without repetition.

You win by completing either:

###  Line
A **full horizontal row** of 5 numbers marked.

###  Bingo
The **entire card** (all 15 numbers) marked.

---

## 2. Game Flow (Turn-by-Turn)

Each round works like this:

1. **A number is drawn** (1–90).
2. You have **3 seconds** to respond.

### Step A — Do you have the number?
You will be asked:

**`Do you have this number? (Y/N):`**

- `Y` = Yes, the number is on your card → it will be marked
- `N` = No, the number is not on your card

If you enter something invalid or run out of time:
- The game treats it as `N`
- You may lose points if that was wrong.

### Step B — Claim a win (only if you answered Y)
If you respond `Y`, you will be asked:

**`Do you want to claim a Line or Bingo? (L/B/N):`**

- `L` = Claim a **Line**
- `B` = Claim **Bingo**
- `N` = No claim

If your claim is false, you lose points.

---

## 3. Points System

### Starting Points
Everyone begins each game with:

**100 points**

### Total Point Pool
At the start:

**Total Pool = sum of all players’ starting points**

Example:
- Easy mode → 5 players total
- Pool = 5 × 100 = **500 points**

---

### Rewards

| Win Type | Reward |
|---------|--------|
| **Line** | +10% of total pool |
| **Bingo** | +50% of total pool |

Example (pool = 500):

- Line reward = 10% → **+50 points**
- Bingo reward = 50% → **+250 points**

---

### Penalties (Anti-cheat)

| Mistake | Penalty |
|--------|---------|
| Wrong Y/N answer | **–1 point** |
| False Line/Bingo claim | **–3 points** |

Examples:
- You say `Y` but number isn’t on your card → –1
- You say `N` but number *was* on your card → –1
- You claim `L` but no row is complete → –3
- You claim `B` but card isn’t full → –3

---

## 4. Multiplayer Modes (Bots)

You always play with bots depending on difficulty:

| Mode | Bots | Total Players |
|------|------|---------------|
| **Easy** | 4 bots | 5 players |
| **Medium** | 9 bots | 10 players |
| **Hard** | 19 bots | 20 players |

Bots:
- Automatically mark their numbers.
- Claim Line/Bingo immediately when they actually achieve it.
- Do not cheat.

---

## 5. What You See On Screen

During the game you will see:

- The drawn number each turn.
- Your card with marked numbers displayed like:
  - `23` (unmarked)
  - `[23]` (marked)

---

## 6. Tips for Winning

- Look carefully before answering (Y/N).
- Claim only when you're sure.
- A wrong claim costs more than a missed number.
- Fast responses matter — you only get 3 seconds.

---

## 7. End of Game

The game ends when:

 Someone achieves **Bingo**, or  
 All numbers (1–90) are exhausted.

You’ll then see:
- The winner
- Final points for all players

---

## 8. Quick Command Cheat Sheet

| Prompt | Valid Inputs |
|-------|--------------|
| Do you have this number? | `Y` / `N` |
| Claim Line/Bingo? | `L` / `B` / `N` |

---

Enjoy the game and good luck! 
