def calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    total_payments = duration_years * 12
    
    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
    else:
        monthly_payment = loan_amount / total_payments

    return round(monthly_payment, 2)

def calculate_total_cost(monthly_payment, duration_years):
    total_payments = duration_years * 12
    total_cost = monthly_payment * total_payments
    return round(total_cost, 2)
