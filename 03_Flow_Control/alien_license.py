age: int = 13
planet: str = "Earth"

# --------------------------------------
# And / Or statement
# --------------------------------------


if age < 16 and planet == "Earth":
    print("You are NOT eligible for license on Earth")
elif age > 16 and planet == "Earth":
    print("You can apply for license on Earth")
elif age < 16 or planet == "Zortan":
    print("You can apply for a zortan license")


# ----------------------------
# zortan
# ---------------------------

planet = "Earth"

if age < 16 or planet == "Zortan":
    print("You can apply for a zortan license")
elif age < 16 and planet == "Earth":
    print("You are NOT eligible for license on Earth")
elif age > 16 and planet == "Earth":
    print("You can apply for license on Earth")
