class Item:
    discount = 0.5  # discount for all items

    def __init__(self, name: str, price: float, quantity: int = 1) -> None:
        # Data Validation
        assert price >= 0, f"Price of {price} should be greater than or equal to 0"
        assert quantity >= 0, f"Quantity of {quantity} should be greater than or equal to 0"
        # assign attributes to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"my class is {self.__class__.__name__}\n and the attributes are "
                f"{self.name}, {self.price}, {self.quantity}\n")

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"

    def calculate_total(self):
        return self.price * self.quantity

    def apply_count(self):
        return self.calculate_total() * self.discount


def main():
    item1 = Item(name="Iphone", price=1000, quantity=5)
    item2 = Item(name="Laptop", price=10, quantity=20)
    item3 = Item(name="Shoe", price=2, quantity=5)
    item4 = Item(name="Lantern", price=1, quantity=10)
    item5 = Item(name="Fruit", price=2.5, quantity=2)


if __name__ == "__main__":
    main()
