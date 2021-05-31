import unittest
import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def test_Fizz(self):
        for i in [3, 9, 12, 18, 21]:
            print("test", i)
            self.assertMultiLineEqual(FizzBuzz.FizzBuzz(i), "Fizz")




if __name__ == '__main__':
    unittest.main()
