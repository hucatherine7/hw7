#Catherine Hu
#CS362 HW7

#Should fail first time

import unittest
import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), 'Fizz')


if __name__ == '__main__':
    unittest.main(verbosity=2)
