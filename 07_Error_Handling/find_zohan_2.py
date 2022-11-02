def find_zohan(name: str) -> None:
    friends = ["Cece", "Roko", "Chiko", "Niko", "Zohan", "Mario"]

    if name not in friends:
        raise ValueError(f"{name} is not found")
    else:
        print(f"Found {name}")


find_zohan("Zohan")
find_zohan("sara")


"""
find out more about exceptions 
Go to this link : "https://docs.python.org/3/library/exceptions.html#exception-hierarchy"

"""
