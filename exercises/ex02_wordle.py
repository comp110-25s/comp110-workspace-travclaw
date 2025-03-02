"""Exercise to recreate wordle using concepts from class."""

__author__: str = "730554286"


def contains_char(any_length: str, single_char: str) -> bool:
    """Checks if a single character is included in an any length string."""
    assert len(single_char) == 1, f"len('{single_char}') is not 1"
    char_index: int = 0
    while char_index < len(any_length):
        if any_length[char_index] == single_char:
            return True
        else:
            char_index = char_index + 1
    return False


def emojified(guess_str: str, secret_str: str) -> str:
    """Checks if the letters of the guessed str match that of the secret str."""
    assert len(guess_str) == len(secret_str), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    char_index: int = 0
    emoji_str: str = ""
    while char_index < len(guess_str):
        if guess_str[char_index] == secret_str[char_index]:
            emoji_str = emoji_str + GREEN_BOX
        else:
            if contains_char(secret_str, guess_str[char_index]):
                emoji_str = emoji_str + YELLOW_BOX
            else:
                emoji_str = emoji_str + WHITE_BOX
        char_index = char_index + 1
    return emoji_str


def input_guess(exp_length: int) -> str:
    """Asks for a word with a certain length."""
    guess_ask = input(f"Enter a {exp_length} character word:")
    while exp_length != len(guess_ask):
        guess_ask = input(f"That wasn't {exp_length} chars! Try again:")
    return guess_ask


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    rounds: int = 6
    round: int = 1
    while round <= rounds:
        attempt = input_guess(len(secret))
        print(f"===Turn {round}/{rounds}===")
        print(emojified(attempt, secret))
        if attempt == secret:
            return print(f"You won in {round}/{rounds} turns!")
        round = round + 1
    if round > rounds:
        return print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
