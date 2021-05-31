import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test_ly1(self):
        for i in [2004, 1996, 1816]:
            self.assertEqual(leapyear.leapyear(i), True)
    def test_ly2(self):
        for i in [2100, 1700, 900]:
            self.assertEqual(leapyear.leapyear(i), False)
    def test_ly3(self):
        for i in [2000, 1600, 2400]:
            self.assertEqual(leapyear.leapyear(i), True)

if __name__ == '__main__':
    unittest.main()