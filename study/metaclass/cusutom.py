class InitMeta(type):
    def __new__(mcs, name, parents, attr):
        print("1111111111")
        return type(name, parents, attr)

    def __init__(cls, name, parents, attr):
        print("22222222")
        cls.var = 100
        print(attr)


class NewMeta(type):
    def __new__(mcs, cls_name, parents, attr):
        print("3333333333")
        new_attr = {}
        for name, val in attr.items():
            if not name.startswith('__'):
                new_attr[name] = 100000
            else:
                new_attr[name] = val
        print(new_attr)
        return type(cls_name, parents, new_attr)

    def __init__(cls, name, parents, attr):
        print("444444444444")
        cls.var = 100
        print(attr)


class X(metaclass=InitMeta):
    var = "var"


print(X.var)


class Y(metaclass=NewMeta):
    var = "var"


print(Y.var)


class NormalClass:
    def __init__(self):
        print("11111111111")
        self.var = "100"

    def __new__(cls, *args, **kwargs):
        print("222222")
        print(f"normal{cls}")
        print(f"normal{args}")
        print(f"normal{kwargs}")
        return object


print(NormalClass().var)
