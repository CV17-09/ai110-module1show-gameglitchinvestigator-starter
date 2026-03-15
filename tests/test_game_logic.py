"""
Tests for `check_guess` in `logic_utils.py`.

# NOTE: `check_guess` was moved from `app.py` into `logic_utils.py` and the
# hint-direction bug was fixed — the function now returns the logical outcomes
# "Win", "Too High", or "Too Low" for the comparisons below.
"""

from logic_utils import check_guess


def test_winning_guess():
    # secret == guess -> should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # guess > secret -> "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # guess < secret -> "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
