import unittest
import LeapYear


class TestLeapYear(unittest.TestCase):
    def test_leapyearSmall(self):
        self.assertEqual(LeapYear.LeapYear(4), True)

    def test_leapYears(self):
        for i in [4, 12, 24, 48, 100, 400]:
            print("leap year ", i)
        self.assertEqual(LeapYear.LeapYear(i), True)


if __name__ == '__main__':
    unittest.main()
