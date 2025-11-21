# src/main.py
"""
Mini Bingo Game — full version (NO timeouts)

Implements:
- 3x5 card per player
- number drawing 1-90 without repetition
- user input each round (no time limit)
- line / bingo claims with rewards
- penalties for wrong Y/N and false claims
- multiplayer with bots (easy/medium/hard)
- instructions screen

Run:
    python -m src.main
"""

from __future__ import annotations

import os
from typing import Dict, List, Optional, Set

from game.bingo_card import complete_card, print_complete_card, BOARD_ROWS, BOARD_COLS
from game.number_draw import NumberDrawer
from game.player import Player

# ---------------- Settings loading ---------------- #
DEFAULT_SETTINGS = {
    "starting_points_per_player": 100,
    "line_percent": 0.10,
    "bingo_percent": 0.50,
    "bots_easy": 4,
    "bots_medium": 9,
    "bots_hard": 19,
}


def load_settings() -> Dict[str, float | int]:
    """Load YAML settings if PyYAML is installed; otherwise fallback to defaults."""
    settings = DEFAULT_SETTINGS.copy()
    try:
        import yaml  # type: ignore
        path = os.path.join(os.path.dirname(__file__), "config", "settings.yaml")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            settings["starting_points_per_player"] = data.get("game", {}).get(
                "starting_points_per_player",
                settings["starting_points_per_player"],
            )
            settings["line_percent"] = data.get("rewards", {}).get(
                "line_percent",
                settings["line_percent"],
            )
            settings["bingo_percent"] = data.get("rewards", {}).get(
                "bingo_percent",
                settings["bingo_percent"],
            )
            modes = data.get("modes", {})
            settings["bots_easy"] = modes.get("easy", {}).get("bots", settings["bots_easy"])
            settings["bots_medium"] = modes.get("medium", {}).get("bots", settings["bots_medium"])
            settings["bots_hard"] = modes.get("hard", {}).get("bots", settings["bots_hard"])
    except ImportError:
        pass
    except Exception as e:
        print(f" Settings load failed: {e}. Using defaults.")
    return settings


SETTINGS = load_settings()


# ---------------- Rendering helpers ---------------- #
def print_marked_card(card: List[List[int]], marked: Set[int]) -> None:
    """Show player's card with marked numbers bracketed, properly aligned."""
    top = "┌" + ("────┬" * (BOARD_COLS - 1)) + "────┐"
    mid = "├" + ("────┼" * (BOARD_COLS - 1)) + "────┤"
    bot = "└" + ("────┴" * (BOARD_COLS - 1)) + "────┘"

    def row_fmt(values: List[str]) -> str:
        return "│" + "│".join(values) + "│"

    print(top)
    for r in range(BOARD_ROWS):
        row: List[str] = []
        for c in range(BOARD_COLS):
            v = card[r][c]
            if v in marked:
                row.append(f"[{v:2d}]")  
            else:
                row.append(f" {v:2d} ")  
        print(row_fmt(row))
        if r < BOARD_ROWS - 1:
            print(mid)
    print(bot)


# ---------------- Instructions screen ---------------- #
def print_instructions() -> None:
    print("""
==================== MINI BINGO ====================

Goal:
  Mark numbers on your 3×5 card as they are drawn.
  You can win by completing:
    • A LINE  (any full horizontal row)
    • BINGO   (the entire card)

Commands per round:
  1) "Do you have this number? (Y/N)"
       Y = yes, it's on your card and you want to mark it
       N = no

  2) If you said Y, you'll be asked:
       "Claim Line or Bingo? (L/B/N)"
       L = claim a line
       B = claim bingo
       N = no claim

Points:
  • Everyone starts with starting points.
  • Total point pool = sum of starting points of all players.
  Rewards:
    • Line  → +10% of pool
    • Bingo → +50% of pool
  Penalties:
    • Wrong Y/N answer → -1 point
    • False Line/Bingo claim → -3 points

Multiplayer Modes:
  Easy   → You + 4 bots   (5 players total)
  Medium → You + 9 bots   (10 players total)
  Hard   → You + 19 bots  (20 players total)

=====================================================
""")


# ---------------- Setup / Mode selection ---------------- #
def choose_mode() -> int:
    prompt = (
        "\nChoose difficulty:\n"
        "  1) Easy   (vs 4 bots)\n"
        "  2) Medium (vs 9 bots)\n"
        "  3) Hard   (vs 19 bots)\n"
        "Enter 1/2/3: "
    )
    while True:
        ans = input(prompt).strip()
        if ans in ("1", "2", "3"):
            return int(ans)
        print(" Invalid choice. Type 1, 2, or 3.")


def create_players(mode: int) -> List[Player]:
    bots_count = {
        1: int(SETTINGS["bots_easy"]),
        2: int(SETTINGS["bots_medium"]),
        3: int(SETTINGS["bots_hard"]),
    }[mode]

    starting_points = int(SETTINGS["starting_points_per_player"])

    players: List[Player] = []
    human_card = complete_card()
    human = Player(name="You", card=human_card, is_bot=False, points=starting_points)
    players.append(human)

    for i in range(bots_count):
        bot_card = complete_card()
        bot = Player(name=f"Bot-{i+1}", card=bot_card, is_bot=True, points=starting_points)
        players.append(bot)

    return players


# ---------------- Core game loop ---------------- #
def play_game(seed: Optional[int] = None) -> None:
    print_instructions()
    mode = choose_mode()
    players = create_players(mode)

    human = players[0]
    pool_total = sum(p.points for p in players)

    print_complete_card(human.card)
    print(f"\nPlayers in this match: {len(players)} (You + {len(players)-1} bots)")
    print(f"Starting points each: {SETTINGS['starting_points_per_player']}")
    print(f"Total point pool: {pool_total}\n")

    drawer = NumberDrawer(seed=seed)

    turn = 1
    bingo_winner: Optional[Player] = None

    try:
        while True:
            drawn = drawer.draw_next()
            if drawn is None:
                print("\nNo more numbers left. Game over.")
                break

            print(f"\n========== TURN {turn} ==========")
            print(f" Number drawn: {drawn}")

            # --- Bots play ---
            for bot in players[1:]:
                has_num, claim = bot.bot_play_turn(drawn)
                if claim == "L" and not bot.has_line:
                    reward = bot.award_line(pool_total)
                    print(f" {bot.name} claims a LINE! +{reward} points. (Total: {bot.points})")
                if claim == "B" and not bot.has_bingo:
                    reward = bot.award_bingo(pool_total)
                    print(f" {bot.name} claims BINGO! +{reward} points. (Total: {bot.points})")
                    bingo_winner = bot

            if bingo_winner:
                break

            # --- Human turn ---
            print("\nYour card right now:")
            print_marked_card(human.card, human.marked)

            try:
                ans = input(f"\nDo you have {drawn}? (Y/N): ")
            except EOFError:
                ans = "N"

            ans = ans.strip().upper()
            if ans not in ("Y", "N"):
                print(" Invalid input. Treated as 'N' and -1 point penalty.")
                human.penalize_wrong_number()
                ans = "N"

            actually_on_card = human.has_number(drawn)

            if ans == "Y":
                if actually_on_card:
                    human.mark_number(drawn)
                    print(" Marked!")
                else:
                    print(" That number is NOT on your card. -1 point.")
                    human.penalize_wrong_number()
            else:  # ans == "N"
                if actually_on_card:
                    print(" It WAS on your card. Missed it! -1 point.")
                    human.penalize_wrong_number()

            claim: Optional[str] = None
            if ans == "Y":
                try:
                    c = input("Claim Line/Bingo? (L/B/N): ")
                except EOFError:
                    c = "N"

                c = c.strip().upper()
                if c not in ("L", "B", "N"):
                    print(" Invalid claim input. No claim.")
                    c = "N"
                if c in ("L", "B"):
                    claim = c

            # Validate claim
            if claim == "L":
                if (not human.has_line) and human.check_line():
                    reward = human.award_line(pool_total)
                    print(f" LINE COMPLETE! You gain +{reward} points.")
                else:
                    print(" False Line claim. -3 points.")
                    human.penalize_false_claim()

            if claim == "B":
                if (not human.has_bingo) and human.check_bingo():
                    reward = human.award_bingo(pool_total)
                    print(f" BINGO!!! You gain +{reward} points.")
                    bingo_winner = human
                else:
                    print(" False Bingo claim. -3 points.")
                    human.penalize_false_claim()

            print(f"\nYour points: {human.points}")
            turn += 1

            if bingo_winner:
                break

    except KeyboardInterrupt:
        print("\n\n Game interrupted by user.")

    # ---------------- End game summary ---------------- #
    print("\n================== GAME OVER ==================")
    if bingo_winner:
        print(f"Winner: {bingo_winner.name} ")
    else:
        print("No Bingo was achieved.")

    print("\nFinal points:")
    for p in players:
        tag = "(You)" if not p.is_bot else "(Bot)"
        print(f"  - {p.name:6s} {tag:5s} → {p.points} pts")
    print("===============================================")


if __name__ == "__main__":
    play_game(seed=None)

