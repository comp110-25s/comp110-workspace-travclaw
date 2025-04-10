"""File to define Fish class."""

__author__: str = "730554286"


class Fish:
    """Fish in the river"""

    age: int

    def __init__(self):
        """Initializes the fish class"""
        self.age = 0
        return None

    def one_day(self):
        """Ages the fish"""
        self.age += 1
        return None
