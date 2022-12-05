from name_function import get_formatted_name

print("q를 입력하면 종료됩니다.")
while True:
    first = input("\n영어로 성을 입력하세요 : ")
    if first == 'q':
        break
    last = input("영어로 이름을 입력하세요 : ")
    if first == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"변경된 이름 : {formatted_name}.")

#
#
# class NamesTestCase2(unittest.TestCase):
#     def test_first_last_name(self):
#         formatted_name = get_formatted_name('kwon', 'jinyong')
#         self.assertEqual(formatted_name, 'Kwon Jinyong')
#
#     def test_first_last_name2(self):
#         formatted_name = get_formatted_name('kwon', 'jinyong')
#         self.assertEqual(formatted_name, 'Kwon Jinyong1')