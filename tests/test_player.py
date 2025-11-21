from src.game.player import Player

def test_line_check():
    card = [
        [1,2,3,4,5],
        [10,11,12,13,14],
        [20,21,22,23,24],
    ]
    p = Player("P", card, points=0)
    for n in [1,2,3,4,5]:
        p.mark_number(n)
    assert p.check_line() is True
    assert p.check_bingo() is False

def test_bingo_check():
    card = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
    ]
    p = Player("P", card, points=0)
    for n in range(1,16):
        p.mark_number(n)
    assert p.check_bingo() is True
