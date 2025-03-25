"""Testing the dictionary functions"""

__author__: str = "730554286"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_use() -> None:
    """test use case for the invert function"""
    assert invert({"1": "2", "3": "4", "5": "6"}) == {"2": "1", "4": "3", "6": "5"}


def test_invert_use2() -> None:
    """test use case for the invert function"""
    assert invert({"Travis": "Clawson"}) == {"Clawson": "Travis"}


def test_invert_edge() -> None:
    """test edge case for the invert function"""
    assert invert({}) == {}


def test_favorite_color_use() -> None:
    """test use case for the favorite_color function"""
    assert (
        favorite_color({"John": "green", "Jack": "yellow", "Matt": "green"}) == "green"
    )


def test_favorite_color_use2() -> None:
    """test use case for the favorite_color function"""
    assert favorite_color({"Jerry": "blue", "Mike": "blue", "Peyton": "blue"}) == "blue"


def test_favorite_color_edge() -> None:
    """test edge case for the favorite_color function"""
    assert favorite_color({}) == ""


def test_count_use() -> None:
    """test use case for the count function"""
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_count_use2() -> None:
    """test use case for the count function"""
    assert count(["a", "a", "a", "b", "c"]) == {"a": 3, "b": 1, "c": 1}


def test_count_edge() -> None:
    """test edge case for the count function"""
    assert count([]) == {}


def test_bin_len_use() -> None:
    """test use case for the bin_len function"""
    assert bin_len(["football", "basketball", "baseball"]) == {
        8: {"football", "baseball"},
        10: {"basketball"},
    }


def test_bin_len_use2() -> None:
    """test use case for the bin_len function"""
    assert bin_len(["a", "b", "ab", "c", "bc", "abc"]) == {
        1: {"a", "b", "c"},
        2: {"ab", "bc"},
        3: {"abc"},
    }


def test_bin_len_edge() -> None:
    """test edge case for the bin_len function"""
    assert bin_len([]) == {}
