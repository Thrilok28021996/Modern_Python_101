def divider(x: int, y: int) -> None:
    try:
        # code
        num = x / y
    except ZeroDivisionError:  # catch specific error
        # do something with errr
        print("can't divide by zero! use some other number.")

    except TypeError:
        print("Both X and Y needs to be numbers.")

    except Exception as e:
        print(f"oops, something went worng: {e}")

    else:
        print("Else: is executed only when try succeeds ")
        print("printing number...")
        print(num)

    finally:
        print("finally: Always executes irrespective of succeeds or Exception")


# divider(3, 0)
# divider(3, "a")
divider(3, 4)
