
import unittest

from name_formatting import get_formatted_name

class NameFormatTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name("virat", "kohli")
        self.assertEqual(formatted_name, "Virat Kohli")

    def test_first_last_name2(self):
        formatted_name = get_formatted_name("sachin", "tendulkar")
        self.assertEqual(formatted_name, "Sachin Tendulkar")

    def test_first_last_name3(self):
        formatted_name = get_formatted_name("virat", "kohli")
        self.assertEqual(formatted_name, "Virat Kohli")

if __name__ == '__main__':
    unittest.main()



