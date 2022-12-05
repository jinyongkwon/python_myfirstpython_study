test = [1, 2, 3]
tt_iter = iter(test)
next(tt_iter)
del test[1]
print(next(tt_iter))
print(next(tt_iter))
