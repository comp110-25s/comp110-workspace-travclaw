"""Practice with dictionary functions"""

__author__: str = "730554286"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """inverts the keys and values of the dictionary"""
    inverted: dict[str, str] = {}
    for key in dictionary:
        value: str = dictionary[key]
        inverted[value] = key
    return inverted


def count(list: list[str]) -> dict[str, int]:
    """returns a dictionary with the value being the number of times the key appeared in the list"""
    dictionary: dict[str, int] = {}
    for string in list:
        if string in dictionary:
            dictionary[string] += 1
        else:
            dictionary[string] = 1
    return dictionary


def favorite_color(dictionary: dict[str, str]) -> str:
    """returns the most popular color in the dictionary"""
    colors: list[str] = []
    for name in dictionary:
        color = dictionary[name]
        colors.append(color)
    color_count: dict[str, int] = count(colors)
    fav_color: str = ""
    max: int = 0
    for color in color_count:
        if max < color_count[color]:
            max = color_count[color]
            fav_color = color
    return fav_color


def bin_len(list: list[str]) -> dict[int, set[str]]:
    """sets the length of strings as the keys and assigns the strings to their corresponding length as the values"""
    dictionary: dict[int, set[str]] = {}
    for string in list:
        length: int = len(string)
        if length in dictionary:
            dictionary[length].add(string)
        else:
            dictionary[length] = {string}
    return dictionary
