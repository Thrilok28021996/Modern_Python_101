"""
Dictionary:
------------

Dictonary makes it easy to have key-value pairs.

Info:
------
Lookups are very fast!!!
"""
marks: dict[str, int] = {
    "Maths": 80,
    "Science": 82,
    "History": 78,
    "English": 35,
    "Python": 98,
    "Physics": 63,
}

print(f" Marks: {marks}")

# -------------------------
# Checkout all the subjects
# -------------------------

for subject in marks.keys():
    print(subject)

# ------------------------------
# Checkout all the marks(values)
# -------------------------------

for score in marks.values():
    print(score)

# ---------------------------------------------------
# Checkout all the subjects and marks( keys - values)
# ----------------------------------------------------

for subject, score in marks.items():
    print(f"{subject}: {score} / 100")


# ------------------------------------------------------
# check out the Passes of the subjects , passing mark 50
# -------------------------------------------------------

for subject, score in marks.items():
    if score >= 50:
        print(f"{subject} PASS")
    else:
        print(f"{subject} FAIL!!!")


# ------------------------------
# Change the english marks to 70
# -------------------------------

marks["English"] = 70
print(f"Scored {marks['English']} in English")

# ------------------------------
# Add Geography and scored 78
# -------------------------------

marks["Geography"] = 78

# ------------------------------------------------------------
# Again check out the Passes of the subjects , passing mark 50
# ------------------------------------------------------------

for subject, score in marks.items():
    if score >= 50:
        print(f"{subject} PASS")
    else:
        print(f"{subject} FAIL!!!")

# --------------------------
# check the score of Python
# --------------------------

# --------------------------
# Alternative # 1
# --------------------------

python_score = marks["Python"]
print(f"Scored {python_score} in Python")

# --------------------------
# Alternative # 2
# --------------------------

python_score = marks.get("Python")
print(f"Scored {python_score} in Python")

# --------------------------
# check the score of Java
# --------------------------
# ----------------------------------
# Alternative # 1 throws Keys error
# ----------------------------------
# java_score = marks["Java"]
# print(f"Scored {java_score} in Java")


# ------------------------------------
# Alternative # 2 - preferred Approach
# -------------------------------------

java_score = marks.get("Java")
if java_score is None:
    print("Did Not study Java")
else:
    print(f"Scored {java_score} in Java")

# ------------------------------------
# Deleting an element from dictionary
# -------------------------------------

del marks["English"]

print(f"marks:{marks}")

pizza = {
    10: "small",
    8.99: "price",
    ("cheese", "olives"): "toppings",
    True: "available",
}

print(pizza[10])
print(pizza[8.99])
print(pizza[("cheese", "olives")])
print(pizza[True])
