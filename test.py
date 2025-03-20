import unittest
from utils import calculate_monthly_payment, calculate_total_cost

class TestLoanCalculatorUtils(unittest.TestCase):
    def test_calculate_monthly_payment_with_interest(self):
        loan_amount = 10000
        duration_years = 5
        annual_interest_rate = 5
        expected_payment = 188.71
        result = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_calculate_monthly_payment_no_interest(self):
        loan_amount = 10000
        duration_years = 5
        annual_interest_rate = 0
        expected_payment = 166.67
        result = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_calculate_total_cost(self):
        monthly_payment = 188.71
        duration_years = 5
        expected_total_cost = 11322.6
        result = calculate_total_cost(monthly_payment, duration_years)
        self.assertAlmostEqual(result, expected_total_cost, places=2)

if __name__ == '__main__':
    unittest.main()
