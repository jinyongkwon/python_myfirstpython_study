class InitMeta(type):
    def __init__(cls, name, bases, dct):
        cls.y = 100
        cls.b = 100


class X(metaclass=InitMeta):
    def __init__(self):
        self.t = 300


print(X)
print(X.y)
print(X.t)


class Parent:
    def __init__(self):
        self.y = 110
        self.b = 100


class Child(Parent):
    pass


print(Parent)
print(Parent.y)
print(X.y)
