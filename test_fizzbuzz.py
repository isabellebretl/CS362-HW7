import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test_fb1(self):
        for i in [3, 6, 9, 12]:
            self.assertEqual(fizzbuzz.fizzbuzz(i), "Fizz")

if __name__ == '__main__':
    unittest.main()