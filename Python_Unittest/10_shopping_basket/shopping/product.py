class Product:

    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (f"Product(name='{self.name}', price={self.price}, "
                f"quantity={self.quantity})")
