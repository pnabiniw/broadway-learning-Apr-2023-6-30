"""
1. What are different types of inheritances in python?
 => Single, Multiple, Hierarchical, Multilevel, Hybrid
2. What will be the output of te following code
"""

class A:
    a = 1

class B(A):
    a = 2

class C(A):
    a = 3

class D(B, C):
    a = 4

class E(D):
    pass

print(E.mro())
# E, D, B, C, A
