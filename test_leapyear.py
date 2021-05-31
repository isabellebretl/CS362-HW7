import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test_ly1(self):
        for i in [2004, 1996, 1816]:
            self.assertEqual(leapyear.leapyear(i), True)

if __name__ == '__main__':
    unittest.main()