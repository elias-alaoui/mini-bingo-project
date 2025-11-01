# src/game/bingo_card.py
from __future__ import annotations

import random
from typing import List, Sequence

# --- Core constants (can be later loaded from config/settings.yaml) ---
BOARD_ROWS = 3
BOARD_COLS = 5
NUMBER_RANGE = (1, 90)  # inclusive
CARD_SIZE = BOARD_ROWS * BOARD_COLS  # 15


def generate_empty() -> List[List[int | None]]:
    """
    Task (Marc): Generate an empty 3x5 bingo card that will be seen by the user in the terminal.

    Returns a BOARD_ROWS x BOARD_COLS matrix filled with None to represent empty slots.
    """
    return [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]


def random_generated() -> List[int]:
    """
    Task (Elias): Generate 15 random unique numbers within the valid range (1–90).

    Returns:
        A list of 15 unique integers sampled without replacement from NUMBER_RANGE.
    """
    low, high = NUMBER_RANGE
    population = range(low, high + 1)
    return random.sample(population, CARD_SIZE)


def complete_card() -> List[List[int]]:
    """
    Task (Gerard): Allocate the numbers from random_generated() into the empty bingo card slots.

    Returns:
        A BOARD_ROWS x BOARD_COLS matrix filled with 15 unique random numbers.
    """
    empty = generate_empty()
    numbers = random_generated()
    random.shuffle(numbers)  # random insertion order across the grid

    idx = 0
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            empty[r][c] = numbers[idx]
            idx += 1
    # type: ignore[return-value]
    return empty  # now it's List[List[int]]


def _format_row(values: Sequence[int | None]) -> str:
    """Helper: render one table row with proper spacing and borders."""
    # Width 2 or 3 depending on range; 1–90 fits width=2, add padding for readability
    cells = []
    for v in values:
        if v is None:
            cells.append("  ")
        else:
            cells.append(f"{v:2d}")
    return " │ " + " │ ".join(cells) + " │"


def print_complete_card(card: List[List[int | None]]) -> None:
    """
    Task (Marc): Display the completed bingo card to the user in a clear, readable way,
    printed as a table in the terminal.

    Args:
        card: A 3x5 matrix with ints (or None before being fully allocated).
    """
    top = "┌" + ("──┬" * (BOARD_COLS - 1)) + "──┐"
    mid = "├" + ("──┼" * (BOARD_COLS - 1)) + "──┤"
    bot = "└" + ("──┴" * (BOARD_COLS - 1)) + "──┘"

    print("\nYour Bingo Card (3×5):")
    print(top)
    for r, row in enumerate(card):
        print(_format_row(row))
        if r < BOARD_ROWS - 1:
            print(mid)
    print(bot)
