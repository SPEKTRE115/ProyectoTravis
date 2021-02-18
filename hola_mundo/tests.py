import unittest

# Create your tests here.

class TestSmokeTest(unittest.TestCase):

    def test_uno_mas_uno_igual_a_dos(self):
        self.assertEqual(1 + 1,2)

if __name__ == '__main__':
    unittest.main()