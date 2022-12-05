import io
import locale

# dst = None
# from collections import namedtuple
import os

with open('hi.txt', 'r+t', encoding='utf-8', newline='\n') as file_object:
    print(file_object.read())
    print(str(os.linesep)+os.linesep+os.linesep+os.linesep)
    # test = namedtuple('TEST', field_names=['f1', 'f2'])
    # src = test(1, 2)
    # print(id(src))
    # dst = src
    # print(id(dst))
    # print(type(file_object.read()))

f = io.BytesIO(b"some initial binary data: \x00\x01")
# f = io.StringIO("some initial text data")
print(f.read())

# print(dst)
# print(id(dst))
# print(id(src))
# with open('hi2.txt', 'w+t', encoding='utf-8') as file_object:
#     file_object.write("진용")
#     print(file_object.read())
#
# with open('hi3.txt', 'a+b', encoding='utf-8') as file_object:
#     print(file_object.read())

print(locale.getpreferredencoding())
