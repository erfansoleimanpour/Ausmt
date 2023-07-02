import unittest

def calculate_sum():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", result)




class TestCalculateSum(unittest.TestCase):

    def test_calculate_sum(self):
        # Test case 1: Positive numbers
        self.assertEqual(calculate_sum(2, 3), 5)

        # Test case 2: Negative numbers
        self.assertEqual(calculate_sum(-5, -7), -12)

        # Test case 3: Decimal numbers
        self.assertEqual(calculate_sum(1.5, 2.5), 4.0)

        # Test case 4: Zero
        self.assertEqual(calculate_sum(0, 0), 0)

        # Test case 5: Non-numeric input
        with self.assertRaises(ValueError):
            calculate_sum('a', 3)

        # Test case 6: Missing input
        with self.assertRaises(ValueError):
            calculate_sum(5)

if __name__ == '__main__':
    unittest.main()

