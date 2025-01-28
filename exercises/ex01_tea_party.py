"""Exercise to write a program that plans a tea party by using the number of guests to calculate tea bags, treats, and cost of the tea party"""

__author__: str = "730554286"


def main_planner(guests: int) -> None:
    """Bring the tea_bags, treats, and cost functions together to plan the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculate amount of teabags needed given amount of people attending"""
    return people * 2


def treats(people: int) -> int:
    """Calculate amount of treats needed based on number of teas guests expect to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost of tea party given the number of teabags and treats needed"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
