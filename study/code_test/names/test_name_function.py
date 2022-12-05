import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('kwon', 'jinyong')
        self.assertEqual(formatted_name, 'Kwon Jinyong')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('kwon', 'yong', 'jin')
        self.assertEqual(formatted_name, "Kwon Jin Yong")


if __name__ == '__main__':
    unittest.main()
