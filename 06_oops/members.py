"""
Class can have class variables as well as instance variables.

Class variables are shared across all instances while instance
variable are only limited to that particular instance.
"""


class Box:

    # Class Varible/ Member
    box_type = "Packaging Carton"
    color = "Brown"

    def __init__(self, side_a: int, side_b: int) -> None:
        # instances variables/Members
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self) -> None:
        return '<class "Box">'

    def __str__(self) -> None:
        return f"Side A: {self.side_a}, Side B: {self.side_b}"


b1 = Box(3, 4)
print(b1)
print(b1.box_type)
print(b1.color)
