import random


class TechStack:

    def __init__(self):
        self.tech_names = []

    def add_tech(self, name):
        if not name in self.tech_names:
            self.tech_names.append(name)
            return self
        return self

    def get_tech(self):
        return random.choice(self.tech_names)
