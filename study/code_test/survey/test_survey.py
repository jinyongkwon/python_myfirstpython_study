import unittest
from survey import AnonymousSurvey


class TestAnonmyousSurvey(unittest.TestCase):
    def setUp(self):
        question = "처음 배운 코딩 언어는?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['C', 'Java', 'Python']
        print("실행")

    def tearDown(self):
        print("종료")

    @unittest.skip("건너뛰기 테스트")
    def test_store_single_response(self):
        print("테스트1")
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        print("테스트2")
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
