"""
Higher Order Functions
------------------------

Functions under the hood are just 'objects', they
can be passed to other functions and fucntions can also
return functions!

This data type is called as 'Callable', one which can be called or invoked.

Note:
------

Till now we have been sending data to our functions, but sending data every time
can be expensive, instead we can send function to data!
"""


from typing import Callable


def hello() -> None:
    """prints Hello world."""
    print("Hello world!")


# hello is just a regular object or class of type function

# print(hello)
# print(id(hello))
# print(type(hello))

# we can assign fucntion to variables

greet: Callable[[], None] = hello  # just assigns the object 'hello' to greet variable
# greet() # we can invoke/call the function using '()' at the end

# --------------------------------------------------------

"""
Create a universal greeter that can greet a person in multiple 
ways
"""


def zola(name: str) -> str:
    return f"zola, {name}"


def good_morning(name: str) -> str:
    return f"Good morning, {name}"


def goodbye(name: str) -> str:
    return f"Goodbye, {name}"


# Function accepting a function


def universal_greeter(name: str, greeter: Callable[[str], str]):
    """can greet in multiple ways"""

    msg = greeter(name)
    print(msg)


universal_greeter("octallium", zola)
universal_greeter("octallium", good_morning)
universal_greeter("octallium", goodbye)

# ------------------------------------------------------------

"""
Functions returning Functions
-----------------------------

"""

# Function returning a function


def add_by_5(num: int) -> Callable[[], int]:
    """Add by 5"""

    def by_5() -> int:
        return num + 5

    return by_5


sum = add_by_5(5)
print(sum())


def unique_adder(num1: int) -> Callable[[int], int]:
    """Adds two numbers and then subtracts by 1"""

    def adder(num2: int) -> int:
        return num1 + num2 - 1

    return adder


addr = unique_adder(5)
print(addr(5))


# ------------------------------------------------------

"""
Lambda:
-------

The way in which we declared functions are very verbose,
we cancondense them in a single statement.

Let's try to create a calculator from scratch
"""


add: Callable[[int, int], int] = lambda x, y: x + y
subtract: Callable[[int, int], int] = lambda x, y: x - y
multiply: Callable[[int, int], int] = lambda x, y: x * y


def calc(num1: int, num2: int, operation: Callable[[int, int], int]) -> int:
    """Performs the maths operation on the numbers"""
    return operation(num1, num2)


print(calc(4, 5, add))
print(calc(4, 5, subtract))
print(calc(4, 5, multiply))
