a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

a = {"a": 1, "b": 2, "c": 3}
b = {"a": 1, "b": 2, "c": 3}
print(a == b)
print(a is b)

a = [b]
b = [a]

print(a==b)