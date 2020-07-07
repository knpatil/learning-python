
import unittest

from calc import addition

class CalcTestCase(unittest.TestCase):

    def test_addition(self):
        # 1. setup test data
        num1 = 100
        num2 = 300

        # 2. call the method you want to test
        result = addition(num1, num2)

        # 3. verify the result
        self.assertEqual(result, 400)  # verify the result

    def test_with_negative_numbers(self):
        # 1. setup test data
        num1 = -100
        num2 = -300

        # 2. call the method you want to test
        result = addition(num1, num2)

        # 3. verify the result
        self.assertEqual(result, 400)  # verify the result

    def test_with_negative_numbers3(self):
        # 1. setup test data
        num1 = -100
        num2 = 500

        # 2. call the method you want to test
        result = addition(num1, num2)

        # 3. verify the result
        self.assertEqual(result, 400)  # verify the result

if __name__ == '__main__':
    unittest.main()

