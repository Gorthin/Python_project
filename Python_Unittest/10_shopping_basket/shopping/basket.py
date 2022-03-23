from shopping.product import Product


class ShoppingBasket:

    def __init__(self):
        self.products = []

    def __len__(self):
        return sum([product.quantity for product in self.products])

    def add_product(self, name, price):
        for product in self.products:
            if product.name == name:
                product.quantity += 1
                return self
        self.products.append(Product(name, price))
        return self

    def get_product(self, index):
        return self.products[index]

    def total(self, tax=21):
        net_value = sum([product.price * product.quantity
                         for product in self.products])
        return round(net_value * (1 + tax / 100.0), 2)

    def display_basket(self):
        print('In basket:')
        for product in self.products:
            print(f'\t{product}')