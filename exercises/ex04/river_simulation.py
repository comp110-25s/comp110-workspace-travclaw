"""Runs a simulation on the river"""

__author__: str = "730554286"

from exercises.EX04.river import River

my_river: River = River(num_fish=10, num_bears=2)
my_river.view_river()
my_river.one_river_week()
