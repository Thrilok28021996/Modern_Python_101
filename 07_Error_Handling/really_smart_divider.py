def rsmart_divider(x: int, y: int) -> None:
    try:
        # code
        num = x / y
        print(num)
    except ZeroDivisionError:  # catch specific error
        # do something with errr
        print("can't divide by zero! use some other number.")

    except TypeError:
        print("Both X and Y needs to be numbers.")

    except Exception as e:
        print(f"oops, something went worng: {e}")


rsmart_divider(3, 0)
rsmart_divider(3, "a")
rsmart_divider(3, 4)
