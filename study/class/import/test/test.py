class A:
    def __init__(self):
        print("a")

    def test(self):
        print("a test")


class B(A):
    def __init__(self):
        super().__init__()
        print("b")


class C:
    def __init__(self):
        print("c")

    def test(self):
        print("c test")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("d")


print(D.mro())

d = D()
d.test()
