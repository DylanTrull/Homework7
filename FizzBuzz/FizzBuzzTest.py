import unittest
import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def test_Fizz(self):
        for i in [3, 9, 12, 18, 21]:
            print("test Fizz", i)
            self.assertMultiLineEqual(FizzBuzz.FizzBuzz(i), "Fizz")

    def test_Buzz(self):
        for i in [5, 10, 20, 25]:
            print("test Buzz", i)
            self.assertMultiLineEqual(FizzBuzz.FizzBuzz(i), "Buzz")



if __name__ == '__main__':
    unittest.main()
