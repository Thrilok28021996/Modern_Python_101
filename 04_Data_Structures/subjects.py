"""
Info:
-----
Tuple also start from index 0
"""

subjects: tuple[str, str, str] = ("Maths", "Science", "History")

# ------------------------Index No(0,		1,			2 	)

# ------------------------
# Count the subjects
# ------------------------

print(f"No.of subjects: {len(subjects)}")

# ----------------------------
# signup for all the subjects
# -----------------------------

for subject in subjects:
    print(f"signing up for: {subject}")


# --------------------------------------
# wants to  see which is second subject
# ---------------------------------------

print(subjects[1])


# -----------------------------------------
# Add 3 more subjects to the subjects tuple
# ------------------------------------------

add_subjects = ("English", "Python", "Physics")
total_subjects = subjects + add_subjects
print(f"All subjects:{total_subjects}")

# -----------------------------------------
# check the python is in subjects tuple
# ------------------------------------------

if "Python" in total_subjects:
    print("yay! Going to Learn Python")
else:
    print("Oh no! no python ")
