# Multiple Inheritance

class A:
    a = 1


class B:
    a = 2


class C(A, B):
    pass


obj = C()
print(obj.a)


# Multilevel Inheritance

class A:
    a = 1


class B(A):
    a = 2


class C(B):
    pass


# Hierarchical Inheritance

class A:
    a = 1


class B(A):
    a = 2


class C(A):
    a = 3


# Hybrid Inheritance

class A:
    a = 1

class B:
    a = 2


class C(A, B):
    a = 3


class D(C):
    a = 4


class E(C):
    a = 5


# print(E.mro())



class A:
    a = 1


class B(A):
    a = 2


class C(A):
    a = 3


class D(B, C):
    pass


print(D.mro())  # Method resolution order





