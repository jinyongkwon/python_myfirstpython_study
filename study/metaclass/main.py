def choose_class(name):
    if name == "test":
        class test():
            pass

        return test  # 클래스를 반환
    else:
        class default():
            pass

        return default


class testClass():
    def __init__(self):
        pass


class typeClass(testClass):
    def __init__(self):
        pass

    a = 10


def test_method(test):
    print(test)


# typeClass = type('typeClass', (testClass,), {'a': 10, 'test_method': test_method})
# typeClass2 = type('typeClass2', (testClass,), {'a': 10, 'test_method': print(130)})
test1 = 12
print(test1.__class__)
test2 = '11'
print(test2.__class__)


def test(): pass


print(test.__class__)
test_class = testClass()
print(test_class.__class__)
test3 = object
print(test3.__class__)

print(test1.__class__.__class__)
print(test2.__class__.__class__)
print(test.__class__.__class__)
print(test_class.__class__.__class__)
print(test3.__class__.__class__)


class Foo(object):
    __metaclass__ = test


foo = Foo()
print(foo.__class__.__class__)

# print(typeClass)
# print(type(typeClass))
# print(typeClass.a)
# typeClass.test = test(typeClass.a)
# typeClass.test
# typeClass.test_method(10)
# test(10)
# print(typeClass2.test_method)
# a = testClass()
# print(a)
# print(testClass)
# test(testClass)
# print(type(testClass))
# print(choose_class("test"))
# print(choose_class("test")())
# print(choose_class('가나다'))
# print(type(choose_class('가나다')))
