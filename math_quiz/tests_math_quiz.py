import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_arithmetic_operation

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val=1
        max_val=10
        for _ in range(1000):  # Test a large number of random values
            rand_num=generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of the expected operators
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, operators)

    def test_perform_arithmetic_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 4, '*', '8 * 4', 32),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, result = perform_arithmetic_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(result, expected_answer)

if __name__ == "__main__":
    unittest.main()
