import os.path

with open('pi_digits.txt') as file_object:
    print(type(file_object))
    contents = file_object.read()  # 문자열 형태로 내용 저장

print(contents)
print(os.path.dirname(__file__))  # 현재 파일(= __file__)이 있는 경로의 디렉토리까지만 반환

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()  # 각 행을 리스트에 담아준다.
    print(lines)

for line in lines:
    print(line.rstrip())
