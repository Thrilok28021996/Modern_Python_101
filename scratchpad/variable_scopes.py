"""

Variable Scopes
-------------------

Scopes can be 'Global or Local'
"""

num = 10


def print_global_num():
    # Global Declaration not required as there is no operation
    # on the variable
    print(f"GLobal NUmber is:{num}")


def print_num():
    num = 20  # fuction or local scope
    print(f"Local Num is {num}")


def inc_num():
    # Explicit Global Declaration
    global num
    num += 2


def inc_local():
    new_num = num + 10
    print(new_num)


print_global_num()
print_num()
inc_num()
inc_local()
print(num)
