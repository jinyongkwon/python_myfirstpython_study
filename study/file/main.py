import os.path
test = None
# with open('test1234.txt', 'w', encoding='utf-8') as file_object:
#     file_object.write("가나다라마")
#     test = file_object.read()


with open('test1234.txt', 'r+t', encoding='utf-8') as file_object:
    file_object.write("ABCDE")
    test = file_object.read()


for i in range(0, len(test)):
    print(test[i])


#ASCII
#0~127
#1바이트가 아니야 4bits
#  8bits 16진수로 127을 표현해봐
# 4비트  8bit 0e

# TODO 나머지 2~4bytes인 utf-8은 어떻게 구분할까??

#     print(type(file_object))
#     contents = file_object.read()  # 문자열 형태로 내용 저장
#
# print(contents)
# print(os.path.dirname(__file__)) # 현재 파일(= __file__)이 있는 경로의 디렉토리까지만 반환
