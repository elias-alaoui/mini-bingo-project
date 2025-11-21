# src/game/player.py
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Set, Tuple
import random

from .bingo_card import BOARD_ROWS, BOARD_COLS


@dataclass
class Player:
    name: str
    card: List[List[int]]
    is_bot: bool = False
    points: int = 0

    marked: Set[int] = field(default_factory=set)
    has_line: bool = False
    has_bingo: bool = False

    def card_numbers(self) -> Set[int]:
        return {self.card[r][c] for r in range(BOARD_ROWS) for c in range(BOARD_COLS)}

    def has_number(self, n: int) -> bool:
        return n in self.card_numbers()

    def mark_number(self, n: int) -> bool:
        """Mark number if on card. Returns True if marked."""
        if self.has_number(n):
            self.marked.add(n)
            return True
        return False

    def check_line(self) -> bool:
        """True if any full row is marked."""
        for r in range(BOARD_ROWS):
            if all(self.card[r][c] in self.marked for c in range(BOARD_COLS)):
                return True
        return False

    def check_bingo(self) -> bool:
        """True if full card is marked."""
        for r in range(BOARD_ROWS):
            for c in range(BOARD_COLS):
                if self.card[r][c] not in self.marked:
                    return False
        return True

    # ---------- Bot behavior ----------
    def bot_play_turn(self, drawn_number: int) -> Tuple[bool, str | None]:
        """
        Bots are honest:
        - If they have the number, they mark it.
        - They claim L/B as soon as they achieve it.
        Returns (has_number, claim).
        """
        has_num = self.mark_number(drawn_number)
        claim = None

        if has_num:
            if (not self.has_bingo) and self.check_bingo():
                claim = "B"
            elif (not self.has_line) and self.check_line():
                claim = "L"
            else:
                claim = None

        return has_num, claim

    # ---------- Points ----------
    def add_points(self, delta: int) -> None:
        self.points += delta

    def penalize_wrong_number(self) -> None:
        self.points -= 1

    def penalize_false_claim(self) -> None:
        self.points -= 3

    def award_line(self, pool_total: int) -> int:
        reward = int(pool_total * 0.10)
        self.points += reward
        self.has_line = True
        return reward

    def award_bingo(self, pool_total: int) -> int:
        reward = int(pool_total * 0.50)
        self.points += reward
        self.has_bingo = True
        return reward
