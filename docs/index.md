# Mini Bingo Game — Documentation

Welcome to the Mini Bingo Game docs. This space contains the vision, backlog, user stories, sprint plan, and gameplay instructions for the project.

---

## Project Overview
- **Goal:** Build a simple, fair, accessible terminal-based Bingo game.
- **Style:** Iterative Scrum approach with small, focused sprints.
- **MVP Scope:** Allocate a 3×5 Bingo card, draw non-repeating numbers, allow manual line/bingo claims, and manage points.

---

## Quick Links
- [Vision Statement](../README.md)
- [Product Backlog](../README.md)
- [User Stories](../README.md)
- [Sprint Plan](../README.md)
- [Gameplay Instructions](../README.md)

---

## Core Rules (Summary)
- **Card:** 3×5 grid, 15 numbers total.
- **Number Range:** 1–90 inclusive.
- **Draws:** Random, no repetition.
- **Claims:** Player types `line` or `bingo` to claim wins.
- **Points:** Start 20; -2 to enter; +10% pool for line; +50% pool for bingo; -1 bad number; -3 false claim.
- **Players:** Choose number of bot opponents (modes coming later).

---

## Sprint 1 Focus
- Generate a valid 3×5 card with 15 unique numbers in range.
- Randomize placement and display clearly in the terminal.
- Add tests for dimensions, uniqueness, range, and rendering.

