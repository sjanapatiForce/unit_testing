import unittest
import functions

class TestCalculator(unittest.TestCase):
    def test_add(self):
        #self.assertEqual(first, second, msg=None)
        self.assertEqual(functions.add(1,2), 3, 'not correct')
        self.assertEqual(functions.add(-1, 1), 0)
        self.assertEqual(functions.add(-1,-1), -2)
        self.assertEqual(functions.add(0, 0), 0)
    def test_divide(self):
        """test for dividing numbers"""
        self.assertEqual(functions.divide(10,2),5)


if __name__ == "__main__":
    unittest.main(verbosity=2)

    def test_is_even(self):
        """test for even number"""
        self.assertTrue(functions.is_even(4))
        for x in [2,3,6,-64,0]:
            with self.subTest(number=x):
                self.assertTrue(functions.is_even(x))
