from src.game.number_draw import NumberDrawer

def test_draw_no_repetition():
    d = NumberDrawer(seed=123)
    seen = set()
    for _ in range(90):
        n = d.draw_next()
        assert n not in seen
        seen.add(n)
    assert d.draw_next() is None
