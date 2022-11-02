from item import Item


class InvoiceItem:
    """Line Item for cash register with purchase quantity & discount"""

    def __init__(self, item: Item, qty: int, discount: float = 0) -> None:
        self.item = item
        self.qty = qty
        self.discount = discount
        # private Member
        self._sub_total = (item.price * qty) - discount

    def __repr__(self) -> None:
        return '<class InvoiceItem">'

    def __str__(self) -> None:
        return (
            f"Item: {self.item}, Qty: {self.qty}, Discount: {self.discount},"
            f"sub Total: {self.get_sub_total():.2f}"
        )

    def get_sub_total(self) -> float:
        """Returns the sub-total."""

        return self._sub_total
