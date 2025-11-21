from src.game import input_handler

def test_valid_sets_exist():
    assert "Y" in input_handler.VALID_YES_NO
    assert "L" in input_handler.VALID_CLAIMS
