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

from typing import Final

# Declaring Constraints

IRONMAN_ATTACK_POWER: Final[int] = 250
BLACK_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanos_life: int = 1500
choice = 0
attack_num = 0

# Declare helper message

MSG = """
--------------------------------------------
Chooose the pairs no. that will attack Thanos
1) Ironman and Blackwidow
2) Black widow and spider man
3) spider man and Hulk
4) Hulk and Iron man
---------------------------------------------
"""

While True:

	# win / loose
	if thanos_life <= 0 and attack_num <=3:
		# win
		break
	elif attack_num >= 3:
		# loose
		break
	print(MSG)
	choice = int(input("Enter the Pair no >>>"))


	if choice == 1:
	    print("Iron man and Black widow are attacting the thanos")
	elif choice == 2:
	    print("Black widow and spider man are attacting the thanos")
	elif choice == 3:
	    print("spider man and Hulk are attacting the thanos")
	elif choice == 4:
	    print("Hulk and Iron man are attacting the thanos")
