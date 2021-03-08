#Catherine Hu

import unittest
import leapyear

class TestLeapYear(unittest.TestCase):
    def test_leapyear(self):
        self.assertEqual(leapyear.lpyear(7), False)
