import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test_fb1(self):
        for i in [3, 6, 9, 12]:
            self.assertEqual(fizzbuzz.fizzbuzz(i), "Fizz")
    def test_fb2(self):
        for i in [5, 10, 20]:
            self.assertEqual(fizzbuzz.fizzbuzz(i), "Buzz")
    def test_fb3(self):
        for i in [15, 30, 45, 90]:
            self.assertEqual(fizzbuzz.fizzbuzz(i), "FizzBuzz")
    def test_fb4(self):
        for i in [1, 7, 28, 82]:
            self.assertEqual(fizzbuzz.fizzbuzz(i), i)

if __name__ == '__main__':
    unittest.main()