import unittest

def add(a, b):
    return a+b

def substract(a,b):
    return a-b

class TestScript(unittest.TestCase):
    def test_add(self):
        result = add(2,3)
        self.assertEqual(result, 5)

    def test_substract(self):
        result = substract(5,1)
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()