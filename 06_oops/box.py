from __future__ import annotations


class Box:
    def __init__(self, side_a: int, side_b: int) -> None:
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self) -> int:
        return self.side_a * self.side_b

    def __repr__(self) -> None:
        return '<class "Box">'

    def __str__(self) -> None:
        return f"Box ==> side A: {self.side_a}, Side B: {self.side_b}"

    def __contains__(self, num: object) -> bool:
        """Use 'in' operator."""
        if not isinstance(num, int):
            raise NotImplementedError
        return num in [self.side_a, self.side_b]

    def __eq__(self, other: object) -> bool:
        """check if boxes are equal."""
        if not isinstance(other, Box):
            raise NotImplemented
        return self.side_a == other.side_a and self.side_b == other.side_b

    def __lt__(self, other: object) -> bool:
        """check if other box is smaller."""
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area < other.area

    def __le__(self, other: object) -> bool:
        """check if other box is smaller."""
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area <= other.area

    def __add__(self, other: object) -> int:
        """Add two boxes."""
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area + other.area

    def __sub__(self, other: object) -> int:
        """Subtract two boxes."""
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area - other.area

    def __mul__(self, other: object) -> int:
        """Multiply two boxes."""
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area * other.area

    def __truediv__(self, other: object) -> float:
        """Divide two boxes."""
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area / other.area

    def __floordiv__(self, other: object) -> float:
        """Divide two boxes."""
        if not isinstance(other, Box):
            raise NotImplemented
        return self.area // other.area


b1 = Box(3, 4)
b2 = Box(2, 5)

# print(b1)
# print(b2)

# print(b1 < b2)
# print(b1 > b2)
# print(b1 <= b2)
# print(b1 >= b2)
# print(b1 == b2)

print(b1 - b2)
print(b1 + b2)
print(b1 * b2)
print(b1 / b2)
print(b1 // b2)

# print(4 in b1)
# print(6 in b1)
# print("a" in b1)
