"""File to define Bear class."""

__author__: str = "730554286"


class Bear:
    """Bears living by the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Ages the bears and makes them more hungry."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Simulates the bear eating x amount of fish."""
        self.hunger_score += num_fish
        return None
