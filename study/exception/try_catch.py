print("나누기를 할 2개의 숫자를 입력하세요")
print("'q'를 누르면 종료합니다.")

while True:
    first_number = input("\n 첫번째 숫자 : ")
    if first_number == 'q':
        break
    second_number = input("\n 두번째 숫자 : ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        pass
    else:
        print(answer)

