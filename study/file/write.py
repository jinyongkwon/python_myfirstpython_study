filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("test programming1111\n")
    file_object.write("test programming2222\n")

with open(filename, 'a') as file_object:
    file_object.write("test1 programming\n")
    file_object.write("test2 programming\n")