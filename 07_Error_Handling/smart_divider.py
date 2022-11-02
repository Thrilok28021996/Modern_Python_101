def smart_divider(x: int, y: int) -> None:
    try:
        # code
        num = x / y
        print(num)
    except ZeroDivisionError:  # catch specific error
        # do something with errr
        print("can't divide by zero! use some other number")


smart_divider(4, 0)
