import unittest


class Calculator(object):
    def add(self, x, y):
        return x + y


class tddexample(unittest.TestCase):
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2, 2)
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()
