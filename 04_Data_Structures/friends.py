"""
info:
-----

Lists are the mutable data structures, that means the data inside can be mutated.
Index always starts from 0.
"""

friends: list[str] = ["Cece", "Roko", "Chiko", "Niko"]
# List with the Index [ 0,		1,		2,		3]

print(f"friends: {friends}")

# --------------------------------------------
# Time to use greet friends using the for Loop
# --------------------------------------------

for friend in friends:
    print(f"zola {friend}!")


# --------------------------------------------
# Count the nuber of the friends
# --------------------------------------------

print(f" Friends Length: {len(friends)}")

# --------------------------------------------
# Remove a friend from the friends list
# --------------------------------------------


unfriend = friends.pop()
print(f"Unfriend: {unfriend}")
print(f"friends: {friends}")


# --------------------------------------------
# Add a friend from the friends list
# --------------------------------------------

friends.append("Ziko")
print(f"friends: {friends}")


# --------------------------------------------
# check out the third friend from the friends
# --------------------------------------------

print(friends[2])

# --------------------------------------------
# Remove a friend from the friends list
# --------------------------------------------

friends.remove("Roko")
print(f"friends: {friends}")


# -------------------------------------------------------
# Insert the friend to the friends list in the same place
# --------------------------------------------------------

friends.insert(1, "Roko")
print(f"friends: {friends}")

# --------------------------------------------
# Friend is in  friends list or not
# --------------------------------------------

if "Roko" in friends:
    print("yay roko is in friends list")
else:
    print("oh no, roko is not in friends list")


# --------------------------------------------
# Add and change the position of a friend in the friends list
# --------------------------------------------


friends.insert(0, "Niko")
print(f"friends: {friends}")


# --------------------------------------------
# sort the  friends list in Alphabetical order
# --------------------------------------------

friends.sort()
print(f"friends: {friends}")

# --------------------------------------------
# sort the  friends list in reverse Alphabetical order
# --------------------------------------------


friends.reverse()
print(f"friends: {friends}")


# --------------------------------------------
# Remove a friend from the friends list
# --------------------------------------------

unfriend = friends.pop()
print(f"Unfriend: {unfriend}")
print(f"friends: {friends}")
