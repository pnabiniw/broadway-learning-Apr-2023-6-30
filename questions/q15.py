"""
What are classmethods and staticmethods in python?
"""

class A:

    @classmethod
    def create_obj(cls, year):
        return cls()

    @staticmethod
    def get_message():
        return "A class static method"

