"""
CLIENT:
-------
This module can be logically thought as a 'client' as it consumes our API 'game'.
"""

from game import Game, Player


def main() -> None:
    """Game Begins Here."""

    p1 = Player("Louis", "Zappa")
    p2 = Player("Chiko", "Neutron")

    game1 = Game(p1)
    print(game1)
    print(game1.state)

    game1.attack().win_or_loose()
    print(game1.state)

    print("-" * 20 + " player 2 starts the game " + "-" * 20)

    game2 = Game(player=p2).attack().win_or_loose()
    print(game2)


main()
