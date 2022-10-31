"""
z_Weight = (Earth_weight + 32)/ 8
"""


def calc_weight(weight: float) -> float:
    return (weight + 32) / 8


print(f"You weight {calc_weight(60):.2f}kgs")
