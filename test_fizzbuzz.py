#Catherine Hu
#CS362 HW7

import unittest
import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), 'Fizz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15), 'FizzBuzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(7), 7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
