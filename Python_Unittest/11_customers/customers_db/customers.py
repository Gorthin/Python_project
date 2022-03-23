class CustomersDB:

    def __init__(self, connection):
        self.connection = connection

    def add_customer(
        self,
        first_name,
        last_name,
        email,
        phone,
        country
    ):
        cursor = self.connection.cursor()
        sql = """
            INSERT INTO customers
            VALUES (:first_name, :last_name, :email, :phone, :country);"""
        cursor.execute(sql, locals())
        self.connection.commit()
        return cursor.lastrowid

    def find_customers_by_first_name(self, first_name):
        cursor = self.connection.cursor()
        sql = """
            SELECT *
            FROM customers
            WHERE first_name LIKE :first_name
            ORDER BY first_name, last_name;"""
        cursor.execute(sql, locals())
        for row in cursor:
            yield row

    def find_customers_by_country(self, country):
        cursor = self.connection.cursor()
        sql = """
            SELECT *
            FROM customers
            WHERE country LIKE :country
            ORDER BY first_name, last_name;"""
        cursor.execute(sql, locals())
        for row in cursor:
            yield row