#Catherine Hu

import unittest
import leapyear

class TestLeapYear(unittest.TestCase):
    def test_leapyear(self):
        self.assertEqual(leapyear.lpyear(7), False)

    def test_leapyear(self):
        self.assertEqual(leapyear.lpyear(12), True)

    def test_leapyear(self):
        self.assertEqual(leapyear.lpyear(400), True)

    def test_leapyear(self):
        self.assertEqual(leapyear.lpyear(300), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)
