"""
VOC DTP
------------
Visualize
Outline
Code
Debug
Test
Polish
"""


# import the stuff we require
from typing import Final

# declare our constants
IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

# declare other variables
thanos_life = 1500
choice = 0
attack_num = 0

# declare helper messages
WIN_MSG: Final[str] = "You successfully saved Zortan!!! "
LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!!"
MSG = """
---------------------------------------------------------------------
Zortan is under attack, choose the pairs no. that will attack Thanos
1) Ironman & Black Widow
2) Black Widow & Spiderman
3) Spiderman & Hulk
4) Hulk & Ironman
---------------------------------------------------------------------
"""

# Start game
while True:

    # First check, should we play the game?
    if thanos_life <= 0 and attack_num <= 3:
        print(WIN_MSG)
        break
    elif attack_num >= 3:
        print(LOST_MSG)
        break

    # Only if we can play, then ask for user input
    print(MSG)
    choice = int(input("Enter your pair no >>> "))

    if choice == 1:
        print("Ironman & Black Widow are attacking Thanos....")
        thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 2:
        print("Black Widow & Spiderman are attacking Thanos....")
        thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
        attack_num += 1
    elif choice == 3:
        print("Spiderman & Hulk are attacking Thanos....")
        thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
        attack_num += 1
    elif choice == 4:
        print("Hulk & Ironman are attacking Thanos....")
        thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER
        attack_num += 1
