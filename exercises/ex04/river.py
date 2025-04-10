"""File to define River class."""

__author__: str = "730554286"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """The setting of the bears and fish."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes the fish older than 3 and bears older than 5."""
        living_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                living_fish.append(fish)
        self.fish = living_fish

        living_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                living_bears.append(bear)
        self.bears = living_bears
        return None

    def bears_eating(self):
        """If there are over 5 fish, a bear eats 3."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Removes the bears with hunger scores lower than 0."""
        living_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                living_bears.append(bear)
        self.bears = living_bears
        return None

    def repopulate_fish(self):
        """Produces 4 fish for every couple of fish."""
        new_fish: int = (len(self.fish) // 2) * 4
        for x in range(new_fish):
            new_fish2 = Fish()
            self.fish.append(new_fish2)
        return None

    def repopulate_bears(self):
        """Produces 1 bear for every couple of bears."""
        new_bears: int = len(self.bears) // 2
        for x in range(new_bears):
            new_bear = Bear()
            self.bears.append(new_bear)
        return None

    def view_river(self):
        """Gives the overview of the fish and bear population of a given day."""
        x: int = self.day
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Runs the one_river_day simulation 7 times to represent a week."""
        for x in range(7):
            self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Removes x amount of fish from the poulation."""
        for x in range(amount):
            self.fish.pop(0)
