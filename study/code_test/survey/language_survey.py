from survey import AnonymousSurvey

question = "처음 배운 코딩 언어는 ?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("q를 입력하면 종료합니다.")
while True:
    response = input("코딩 언어는 : ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("조사에 응해주셔서 감사합니다.")
my_survey.show_results()