# src/main.py
# src/main.py
"""
Mini Bingo Game — main entrypoint

Wires together:
- game/bingo_card.py   → generate_empty, random_generated, complete_card, print_complete_card
- game/number_draw.py  → check_card (draw numbers without repetition + visual snapshot)
- game/input_handler.py→ ask_yes_no, ask_claim, handle_player_turn

Run:
    python -m src.main
"""

from __future__ import annotations

from typing import List, Set

from game.bingo_card import complete_card, print_complete_card, BOARD_ROWS, BOARD_COLS
from game.number_draw import check_card
from game.input_handler import handle_player_turn


# ---------- Helpers for validating user claims ---------- #
def _is_line_complete(card: List[List[int]], drawn: Set[int]) -> bool:
    """Return True if any FULL row in the 3x5 card is completely drawn."""
    for r in range(BOARD_ROWS):
        if all(card[r][c] in drawn for c in range(BOARD_COLS)):
            return True
    return False


def _is_bingo_complete(card: List[List[int]], drawn: Set[int]) -> bool:
    """Return True if the entire 3x5 card is completely drawn (full card)."""
    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLS):
            if card[r][c] not in drawn:
                return False
    return True


def _validate_user_inputs(card: List[List[int]], drawn: Set[int], last_drawn: int, has_number: bool, claim: str | None) -> None:
    """
    Provide feedback about the player's inputs vs. reality.
    (No points applied here—this is just messaging. Hook your points system here later.)
    """
    # Check the Y/N confirmation against the actual card membership of the drawn number
    actually_on_card = any(last_drawn in row for row in card)

    if has_number and not actually_on_card:
        print("⚠️ You answered 'Y' but that number is NOT on your card. (Would be -1 point.)")
    elif not has_number and actually_on_card:
        print("⚠️ You answered 'N' but that number IS on your card. (Would be -1 point.)")

    # If a claim was made, verify
    if claim == "L":
        if _is_line_complete(card, drawn):
            print("✅ Line claim is VALID! (Would award 10% of point pool.)")
        else:
            print("❌ Line claim is NOT valid. (Would be -3 points.)")
    elif claim == "B":
        if _is_bingo_complete(card, drawn):
            print("🏆 Bingo claim is VALID! (Would award 50% of point pool.)")
        else:
            print("❌ Bingo claim is NOT valid. (Would be -3 points.)")


# ---------- Main flows ---------- #
def sprint1_demo_only() -> None:
    """
    Sprint 1 scope only:
      - Build and display the completed 3x5 card.
    """
    card = complete_card()
    print_complete_card(card)


def interactive_demo(turns: int = 8, seed: int | None = 42) -> None:
    """
    Extended demo (beyond Sprint 1):
      - Build and display the card.
      - Draw 'turns' numbers without repetition, show live updates.
      - Prompt the user each turn (Y/N, optional L/B claim).
      - Validate the player's input vs. actual card/drawn state and print feedback.
    """
    card = complete_card()
    print_complete_card(card)

    print("\nStarting the draw…\n(Answer with Y/N, and optionally claim L (line) or B (bingo) when asked.)")

    # Draw numbers turn-by-turn. check_card prints the card snapshot each turn when echo=True.
    for drawn_number, drawn_set in check_card(card, turns=turns, delay_seconds=0.0, seed=seed, echo=True):
        # Ask player for inputs on this number
        has_number, claim = handle_player_turn(drawn_number)

        # Validate the user's responses against the true state
        _validate_user_inputs(card, drawn_set, drawn_number, has_number, claim)

        # If bingo is complete, we can stop the demo early
        if _is_bingo_complete(card, drawn_set):
            print("🎉 Full card completed. Ending demo.")
            break


if __name__ == "__main__":
    # Choose ONE of the flows below depending on what you want to demonstrate:

    # 1) Strict Sprint 1: just allocate and display the card.
    # sprint1_demo_only()

    # 2) Extended interactive demo (uses input handler + live drawing).
    interactive_demo(turns=8, seed=42)


