from abc import ABC


class MyABC(ABC):
    pass


MyABC.register(tuple)

print(type(MyABC))
print(issubclass(tuple, MyABC))
print(isinstance((), MyABC))
