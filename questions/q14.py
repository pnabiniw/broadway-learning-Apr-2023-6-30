"""
What are magic methods? Explain with examples.
"""

class A:
    r = 1

    def __gt__(self, other):
        return self.r > other.r

obj1 = A()
obj1.r = 2
objj2 = A()
objj2.r = 5

print(objj2 > obj1)
