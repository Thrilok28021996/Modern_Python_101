"""
First Bug
---------

Understand behaviour in programming is called as 'Bug'

Python is a dynamically typed language so it's easy to introduce a bug
"""


box = "balloons"
print(f"Box contains {box}")

box = 10
print(f"Box contains {box}")


# ----------------------------------------------------------------------------------
# Introducing the Type Hinting - Optimal Static Type Checking in Python Using 'Mypy'
# ----------------------------------------------------------------------------------

food: str = "Milk"
print(f"Louis is going to drink {food}")

food = "Eggs"
print(f"Louis is going to drink {food}")

food = False
print(f"Louis is going to drink {food}")
