"""
Functions
---------
Write a program to greet everyone

"""


def greeter(name: str) -> None:
    """
    Greets
    """
    print(f"Zola {name}")


def main() -> None:
    friends: list[str] = ["Cece", "Roko", "Chiko", "Niko", "Ziko"]
    for friend in friends:
        greeter(friend)


main()
