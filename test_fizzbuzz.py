#Catherine Hu
#CS362 HW7

#Should fail first time

import unittest
from fizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.Testcase):
    def test_fizzBuzz(self):
        self.assert(fizzBuzz(3), 'Fizz')
