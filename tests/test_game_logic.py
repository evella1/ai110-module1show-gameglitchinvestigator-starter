from logic_utils import check_guess, get_range_for_difficulty

#FIX: Added tests to check the correctness of the check_guess function and get_range_for_difficulty function using agent

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, the guess is too high
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, the guess is too low
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug: incorrect go higher/go lower hint (opposite to the actual) ---

def test_too_high_hint_tells_player_to_go_lower():
    # Guess is above the secret, so the player must aim LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_tells_player_to_go_higher():
    # Guess is below the secret, so the player must aim HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)
