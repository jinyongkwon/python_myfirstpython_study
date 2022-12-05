import unittest


class NumbersTest(unittest.TestCase):
    def test_even(self):
        for i in range(0, 6):
            with self.subTest("가나다라"):
                self.assertEqual(i % 2, 0)
                print("test")


if __name__ == '__main__':
    unittest.main()
