import unittest


class Person:

    def __init__(self, name):
        self.name = name


class Worker(Person):
    pass


class TestPerson(unittest.TestCase):

    def test_case_1(self):
        self.assertIsInstance(Person, type)

    def test_case_2(self):
        person = Person('Guido')
        self.assertIsInstance(person, Person)


class TestWorker(unittest.TestCase):

    def test_case_1(self):
        worker = Worker('Adam')
        self.assertIsInstance(worker, Worker)

    def test_case_2(self):
        worker = Worker('Adam')
        self.assertIsInstance(worker, Person)