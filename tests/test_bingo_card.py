from src.game.bingo_card import complete_card, BOARD_ROWS, BOARD_COLS, NUMBER_RANGE

def test_complete_card_dimensions():
    card = complete_card()
    assert len(card) == BOARD_ROWS
    assert all(len(row) == BOARD_COLS for row in card)

def test_complete_card_unique_numbers():
    card = complete_card()
    nums = [n for row in card for n in row]
    assert len(nums) == len(set(nums))

def test_complete_card_range():
    low, high = NUMBER_RANGE
    card = complete_card()
    for row in card:
        for n in row:
            assert low <= n <= high
