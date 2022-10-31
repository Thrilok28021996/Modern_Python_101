"""
ENUM
-----

This is a very good data structure for creating choices or variaties
"""

from enum import Enum, auto


class PizzaSize(Enum):
    """Pizza Base Size Options"""

    SMALL = 0
    MEDIUM = 10
    LARGE = 12


choice = PizzaSize.MEDIUM

print(f"One order for {choice.value} inch pizza")


class Colors(Enum):
    """T- shirt Varietes"""

    RED = "red"
    BLUE = "blue"
    GREEN = "green"


print(f"One order for {Colors.GREEN.value} T-shirt")


class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANGER = auto()


print(Role.MANGER.value)
