import unittest
import LeapYear


class TestLeapYear(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(LeapYear.LeapYear(4), True)


if __name__ == '__main__':
    unittest.main()
