import unittest
from sqlite3 import connect
from customers_db.customers import CustomersDB


class TestCustomersDB(unittest.TestCase):

    def setUp(self):
        connection = connect(':memory:')
        cursor = connection.cursor()

        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cursor.execute(create_table_sql)

        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]

        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(insert_sql, customers_data)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    def test_add_customer(self):
        # arrange
        db = CustomersDB(self.connection)
        db.add_customer('Jan', 'Nowak', 'jan.nowak@mail.com', '444', 'Poland')
        cursor = self.connection.cursor()

        # act
        cursor.execute("""
            SELECT *
            FROM customers
            ORDER BY first_name, last_name;
        """)

        # assert
        expected = (
            ('Jan', 'Nowak', 'jan.nowak@mail.com', '444', 'Poland'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(tuple(cursor), expected)

    def test_find_customers_by_first_name(self):
        # arrange
        db = CustomersDB(self.connection)

        # act
        actual = tuple(db.find_customers_by_first_name('John'))

        # assert
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA')
        )
        self.assertEqual(actual, expected)

    def test_find_customers_by_country(self):
        # arrange
        db = CustomersDB(self.connection)

        # act
        actual = tuple(db.find_customers_by_country('USA'))

        # assert
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(actual, expected)