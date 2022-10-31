"""
Since, everything is going in real-time, we don't have control over characters,
instead our characters will choose their own fight.
This time each character gets it own structure and defined parameters, so as you
can see our code is getting better and certainly we are going to make is awesome
as we progress with future modules.
"""


# import the stuff we require
from typing import Final
from random import randint

# -------------------------------------------------------------------------
# TYPE ALIAS:
# ===========
# Each time typing type as dict[str, str | int] is so boring, so we instead
# create a type alias and make our lives simpler.
# -------------------------------------------------------------------------

Character = dict[str, str | int]

# SuperHeros
IRONMAN: Final[Character] = {"name": "Ironman", "attack_power": 250, "life": 1000}
BLACKWIDOW: Final[Character] = {"name": "Blackwidow", "attack_power": 180, "life": 800}
SPIDERMAN: Final[Character] = {"name": "Spiderman", "attack_power": 190, "life": 700}
HULK: Final[Character] = {"name": "Hulk", "attack_power": 300, "life": 1100}

# Super Villans

THANOS: Final[Character] = {"name": "Thanos", "attack_power": 400, "life": 1500}
REDSKULL: Final[Character] = {"name": "Redskull", "attack_power": 300, "life": 800}
PROXIMA: Final[Character] = {"name": "Proxima", "attack_power": 320, "life": 800}

# All super Heros
superheros: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
villains: list[Character] = [THANOS, REDSKULL, PROXIMA]

# Helper variables
choice = 0
attack_num = 0

hero_life = 0
villain_life = 0

# declare helper messages
WIN_MSG: Final[str] = "You successfully saved Zortan!!! "
LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!!"

# Attack

for attack in range(3):
    # Each iteration get a new hero and villian
    hero_index = randint(0, 3)
    villain_index = randint(0, 2)
    # helper variables
    current_superhero = superheros[hero_index]
    current_villain = villains[villain_index]
    # Life
    hero_life += current_superhero["life"]
    villain_life += current_villain["life"]
    print(
        f"Attack: {attack + 1} => {current_superhero['name']} is going to fight with {current_villain['name']}."
    )

    # attack
    hero_life -= current_villain["attack_power"]
    villain_life -= current_superhero["attack_power"]

# print a separating line
print("=" * 70)

# win or lose

if hero_life >= villain_life:
    print(WIN_MSG)
else:
    print(LOST_MSG)
