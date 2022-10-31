"""
Info:
-----
Our functions do only one thing at a time,
this is called as 'Single Responsibilty principle' and 
important aspect of programming.
"""

from typing import Final

MAX_FLYING_WEIGHT: Final[float] = 15


def calc_weight(weight: float) -> float:
    """
    calculates the weight
    ----------------------

    Look how the functions just transforms data,
    from float to float.
    """
    return (weight + 32) / 8


def can_fly(weight: float) -> bool:
    """
    Returns if you can fly

    we convert float values to boolean values!!!
    """
    return weight <= MAX_FLYING_WEIGHT


def flying_friends(friends: dict[str, float]) -> None:
    """
    Displays Flying and Non Flying Friends

    Note:
    -----
    No data transforation here.
    we are printing the output to console, the function
    doesn't return anything.
    """
    for name, earth_weight in friends.items():
        z_weight = calc_weight(earth_weight)
        if can_fly(z_weight):
            print(f"{name} :{z_weight} kgs can fly")
        else:
            print(f"{name} :{z_weight} kgs cannot fly")


def main() -> None:
    friends: dict[str, float] = {
        "Cece": 54,
        "Roko": 88,
        "Chiko": 50,
        "Niko": 102,
        "Ziko": 90,
    }

    flying_friends(friends)


main()
