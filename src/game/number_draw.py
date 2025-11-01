# src/game/number_draw.py
from __future__ import annotations

import random
import time
from typing import Generator, Iterable, List, Optional, Set, Tuple

from .bingo_card import NUMBER_RANGE, BOARD_ROWS, BOARD_COLS


class NumberDrawer:
    """
    Draw numbers one-by-one from the global pool without repetition.
    """

    def __init__(self, *, seed: Optional[int] = None) -> None:
        low, high = NUMBER_RANGE
        self._pool: List[int] = list(range(low, high + 1))
        if seed is not None:
            random.seed(seed)
        random.shuffle(self._pool)
        self._idx = 0
        self.drawn: Set[int] = set()

    def draw_next(self) -> Optional[int]:
        """Return the next number or None if exhausted."""
        if self._idx >= len(self._pool):
            return None
        n = self._pool[self._idx]
        self._idx += 1
        self.drawn.add(n)
        return n


def _marked_snapshot(card: List[List[int]], drawn: Set[int]) -> List[List[str]]:
    """
    Render a snapshot of the card where matched numbers are visibly marked.
    We mark hits by surrounding the number with brackets, e.g., [23].
    """
    snap: List[List[str]] = []
    for r in range(BOARD_ROWS):
        row: List[str] = []
        for c in range(BOARD_COLS):
            v = card[r][c]
            if v in drawn:
                row.append(f"[{v:2d}]")
            else:
                row.append(f" {v:2d} ")
        snap.append(row)
    return snap


def _print_snapshot(snapshot: List[List[str]]) -> None:
    top = "┌" + ("────┬" * (BOARD_COLS - 1)) + "────┐"
    mid = "├" + ("────┼" * (BOARD_COLS - 1)) + "────┤"
    bot = "└" + ("────┴" * (BOARD_COLS - 1)) + "────┘"

    def fmt_row(values: Iterable[str]) -> str:
        return " │ " + " │ ".join(values) + " │"

    print(top)
    for r, row in enumerate(snapshot):
        print(fmt_row(row))
        if r < BOARD_ROWS - 1:
            print(mid)
    print(bot)


def check_card(
    card: List[List[int]],
    *,
    turns: Optional[int] = None,
    delay_seconds: float = 0.0,
    seed: Optional[int] = None,
    echo: bool = True,
) -> Generator[Tuple[int, Set[int]], None, None]:
    """
    Task (Elias): Ensure numbers are drawn without repetition and visibly update each turn.

    Behavior:
      - Draws numbers one-by-one from the 1–90 pool with no repeats.
      - After each draw, yields (number_drawn, all_drawn_so_far).
      - If echo=True, prints an updated view of the card with matches marked.
      - `turns` limits the number of draws for demo/testing (None = draw until pool ends).

    Args:
        card: Completed 3x5 bingo card.
        turns: Optional cap on the number of draws to perform.
        delay_seconds: Optional sleep between draws (visual pacing).
        seed: Optional RNG seed to make draws deterministic for tests.
        echo: If True, prints the updated card after each draw.

    Yields:
        (drawn_number, drawn_set) after each draw.
    """
    drawer = NumberDrawer(seed=seed)
    max_draws = turns if turns is not None else len(drawer._pool)

    for _ in range(max_draws):
        n = drawer.draw_next()
        if n is None:
            break

        if echo:
            print(f"\nNumber drawn: {n}")
            snapshot = _marked_snapshot(card, drawer.drawn)
            _print_snapshot(snapshot)

        if delay_seconds > 0:
            time.sleep(delay_seconds)

        yield n, set(drawer.drawn)
