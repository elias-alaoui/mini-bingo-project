# src/main.py
from game.bingo_card import complete_card, print_complete_card
from game.number_draw import check_card


def main() -> None:
    # 1) Build and show the card
    card = complete_card()
    print_complete_card(card)

    # 2) (Optional for Sprint 1 demo) Draw a few numbers and show live updates
    #    You can comment this out if Sprint 1 strictly ends at allocation/display.
    for _n, _seen in check_card(card, turns=5, delay_seconds=0.0, echo=True, seed=42):
        pass


if __name__ == "__main__":
    main()
