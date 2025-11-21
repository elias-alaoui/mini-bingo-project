# src/game/input_handler.py
"""
Handles all player input and basic validation for the Bingo game.

Responsible for:
- Reading user responses (Y/N, Line, Bingo)
- Validating inputs and handling invalid cases gracefully
- Returning standardized results to be processed by the game logic
"""

from __future__ import annotations
from typing import Literal, Optional


VALID_YES_NO = {"Y", "N"}
VALID_CLAIMS = {"L", "B", "N"}  # L = Line, B = Bingo, N = No claim


def ask_yes_no(prompt: str = "Do you have this number? (Y/N): ") -> Literal["Y", "N"]:
    """
    Ask the user whether they have the drawn number.
    Accepts only Y or N (case-insensitive).
    Keeps asking until a valid input is received.

    Returns:
        "Y" if player has the number
        "N" if player does not have the number
    """
    while True:
        response = input(prompt).strip().upper()
        if response in VALID_YES_NO:
            return response
        print(" Invalid input. Please type 'Y' for yes or 'N' for no.")


def ask_claim(prompt: str = "Do you want to claim a Line or Bingo? (L/B/N): ") -> Literal["L", "B", "N"]:
    """
    Ask the user whether they want to claim a Line, Bingo, or None.
    Accepts L, B, or N (case-insensitive).
    Keeps asking until a valid input is received.

    Returns:
        "L" if claiming a line
        "B" if claiming bingo
        "N" if no claim
    """
    while True:
        response = input(prompt).strip().upper()
        if response in VALID_CLAIMS:
            return response
        print(" Invalid input. Please type 'L' for line, 'B' for bingo, or 'N' for no claim.")


def handle_player_turn(drawn_number: int) -> tuple[bool, Optional[str]]:
    """
    Task: Manage the player’s full input sequence for one drawn number.

    Args:
        drawn_number: The number recently called.

    Returns:
        (has_number, claim)
        - has_number: True if player confirmed having the number (Y)
        - claim: "L" (line), "B" (bingo), or None
    """
    print(f"\n Number drawn: {drawn_number}")

    # Ask if player has the number
    response = ask_yes_no()
    has_number = response == "Y"

    # If yes, ask if they want to claim a line or bingo
    claim = None
    if has_number:
        claim_response = ask_claim()
        if claim_response in ("L", "B"):
            claim = claim_response

    return has_number, claim


def validate_claim(is_correct_claim: bool) -> int:
    """
    Task: Handle scoring adjustments for wrong or correct claims.
    (To be integrated with the point system.)

    Args:
        is_correct_claim: Whether the claim (Line/Bingo) is valid.

    Returns:
        Penalty or reward points adjustment.
        Negative for wrong claims, 0 if no claim, positive for correct.
    """
    if is_correct_claim:
        print("Claim accepted!")
        return 0
    else:
        print("Wrong claim! -3 points penalty applied.")
        return -3


if __name__ == "__main__":
    # Simple standalone test
    print("Testing input handler...")
    has_number, claim = handle_player_turn(42)
    print(f"has_number={has_number}, claim={claim}")


