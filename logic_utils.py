def get_range_for_difficulty(difficulty: str):
    """
    Return the inclusive number range for the selected difficulty.

    Args:
        difficulty: The difficulty label chosen by the player.

    Returns:
        A tuple containing the lower and upper bounds for the game range.

    Raises:
        NotImplementedError: This function still needs to be refactored
            from app.py into logic_utils.py.
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse raw user input into an integer guess.

    Args:
        raw: The raw text entered by the player.

    Returns:
        A tuple of:
            - ok: True if parsing succeeded, otherwise False
            - guess_int: The parsed integer if valid, otherwise None
            - error_message: An error message if parsing failed, otherwise None
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare a guess to the secret number.

    Args:
        guess: The player's guess.
        secret: The secret number to compare against.

    Returns:
        A string representing the result of the guess:
        "Win", "Too High", or "Too Low".
    """
    if guess == secret:
        return "Win"

    try:
        if guess > secret:
            return "Too High"
        return "Too Low"
    except TypeError:
        guess_str = str(guess)
        secret_str = str(secret)

        if guess_str == secret_str:
            return "Win"
        if guess_str > secret_str:
            return "Too High"
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update the player's score based on the guess outcome.

    Args:
        current_score: The score before applying the update.
        outcome: The result of the guess.
        attempt_number: The current attempt number.

    Returns:
        The updated score as an integer.

    Raises:
        NotImplementedError: This function still needs to be refactored
            from app.py into logic_utils.py.
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")