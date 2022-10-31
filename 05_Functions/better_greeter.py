"""
Info
-----
Useful pattern for testing
"""


def greeter(name: str) -> str:
    """
    Greeting message
    """
    return f"Zola {name}"


def main() -> None:
    friends: list[str] = ["Cece", "Roko", "Chiko", "Niko", "Ziko"]
    for friend in friends:
        if "Chiko" in greeter(friend):
            print(f"{friend} is cute")
        else:
            print(greeter(friend))


main()
