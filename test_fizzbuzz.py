import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test_fb1(self):
        for i in [3, 6, 9, 12]:
            self.assertEqual(fizzbuzz.fizzbuzz(i), "Fizz")
    def test_fb2(self):
        for i in [5, 10, 20]:
            self.assertEqual(fizzbuzz.fizzbuzz(i), "Buzz")

if __name__ == '__main__':
    unittest.main()