"""
Louis wants to open a pizza shop and needs
to write a program for accepting orders.

Tip -
-----
Always Visualize First, Then Start Coding.
"""

# ------------------------------------
# Variable Declaration
# ------------------------------------


customer: str = "Cece"
pizza_base: str = "Thin"
pizza_size: int = 12
topping: str = "Olives"
extra_cheese: bool = True
price: float = 8.99

# -------------------------------
# Alternative 1 - Using print function
# ----------------------------------


print(f"Recieved order from: {customer}")
print(f"Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}")
print(f"Is extra_cheese required: {extra_cheese}")
print(f"Bill Amount: {price}")


# --------------------------------------
# Alternative 2 - Using formatted string
# --------------------------------------

order_details: str = f"""
Recieved order from: {customer}
Pizza Base: {pizza_base}, Size:{pizza_size} inches, Topping: {topping}
Is extra cheese required: {extra_cheese}
Bill Amount: {price}
"""

print(order_details)


# -------------------------------------------------
# Alternative 3 - Using formatted string in 'print'
# -------------------------------------------------

print(
    f"""
Recieved order from: {customer}
Pizza Base: {pizza_base}, Size:{pizza_size} inches, Topping: {topping}
Is extra cheese required: {extra_cheese}
Bill Amount: {price}
"""
)
