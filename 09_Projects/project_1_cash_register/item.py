class Item:
    """SImple Item for cash Register."""

    def __init__(self, id: int, name: str, price: float, measurement_unit: str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.measurement_unit = measurement_unit  # EG. -> Kg or ml

    def __repr__(self) -> str:
        return '<class "Item">'

    def __str__(self) -> None:
        return f"{self.id}, {self.name}: ${self.price} / {self.measurement_unit}"
