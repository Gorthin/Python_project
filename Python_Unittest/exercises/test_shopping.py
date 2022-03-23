import unittest
from shopping.basket import ShoppingBasket


class TestShoppingBasketWithNoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket without any product...')
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):
        pass

    def test_getting_product_out_of_range_should_raise_error(self):
        pass

    def test_total_amount_should_be_zero(self):
        pass


class TestShoppingBasketWithOneProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket with one product...')
        cls.basket = ShoppingBasket().add_product('milk', 3.0)

    def test_size_of_basket_should_be_one(self):
        pass

    def test_total_amount_should_have_tax(self):
        pass

    def test_getting_product(self):
        pass

    def test_getting_product_out_of_range_should_raise_error(self):
        pass


class TestShoppingBasketWithTwoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket with two products...')
        cls.basket = ShoppingBasket() \
            .add_product('milk', 3.0) \
            .add_product('water', 2.0)

    def test_size_of_basket_should_be_two(self):
        pass

    def test_order_of_products(self):
        pass

    def test_total_amount_should_have_tax(self):
        pass

    def test_getting_product_out_of_range_should_raise_error(self):
        pass


