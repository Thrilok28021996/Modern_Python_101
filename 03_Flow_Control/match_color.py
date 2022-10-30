"""match operator is a new operator in pytohn 3.10.5"""


fav_color: str = input("Enter your favourite color:")
fav_color = fav_color.lower()

print(fav_color)

match fav_color:
    case "black":
        print(" Has black color")
    case "red":
        print("Has red car")
    case "yellow":
        print("Has yellow shirt")
    case "green":
        print("Has green hat")

    case _:
        print(f"Has nothing in {fav_color} color")
