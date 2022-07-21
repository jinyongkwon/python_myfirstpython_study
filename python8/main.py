str1 = 'hello'
str2 = 'hello'  # Immutable Object
print(f"str1의 주소 : {id(str1)}")
print(f"str2의 주소 : {id(str2)}")

list1 = [10, 20, 30]
list2 = [10, 20, 30]  # Mutable Object
print(f"list1의 주소 : {id(list1)}")
print(f"list2의 주소 : {id(list2)}")
print(f"list1의 0번지 주소 : {id(list1[0])}")
print(f"list2의 0번지 주소 : {id(list2[0])}")

tuple1 = ([10, 20, 30], 10, 20)
print(f"before tuple1 : {tuple1}")
tuple1[0][0] = 20
print(f"after tuple1 : {tuple1}")

list3 = []
list4 = []
list5 = list6 = []
print(f"list3과 list4의 주소 비교 결과 : {list3 is list4}")
print(f"list5와 list6의 주소 비교 결과 : {list5 is list6}")







