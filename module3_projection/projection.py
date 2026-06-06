# Module 3 — 5-Year Financial Projection
# projection.py — Projects EMI burden, savings & debt-free date

import matplotlib.pyplot as plt

def calculate_emi(principal, annual_rate, months):
    """
    Calculates monthly EMI using standard formula.
    EMI = P * r * (1+r)^n / ((1+r)^n - 1)
    """
    monthly_rate = annual_rate / (12 * 100)
    emi = principal * monthly_rate * (1 + monthly_rate) ** months
    emi = emi / ((1 + monthly_rate) ** months - 1)
    return round(emi, 2)


def project_finances(income, expenses, loan_amount, annual_rate, loan_years):
    """
    Projects finances over 5 years and plots a chart.
    """
    months = loan_years * 12
    emi = calculate_emi(loan_amount, annual_rate, months)
    monthly_savings = income - expenses - emi

    print(f"\n📊 LoanSense — 5-Year Financial Projection")
    print(f"{'='*45}")
    print(f"💰 Monthly Income   : ₹{income:,.0f}")
    print(f"💸 Monthly Expenses : ₹{expenses:,.0f}")
    print(f"🏦 Monthly EMI      : ₹{emi:,.0f}")
    print(f"💵 Monthly Savings  : ₹{monthly_savings:,.0f}")

    if monthly_savings < 0:
        print(f"\n⚠️  WARNING: EMI exceeds your savings capacity!")
        return

    print(f"🎯 Debt-free in     : {loan_years} years ({months} months)")
    print(f"{'='*45}\n")

    month_list = list(range(1, 61))
    savings_list = []
    emi_burden_list = []
    cumulative_savings = []
    total_savings = 0

    for month in month_list:
        if month <= months:
            emi_burden_list.append(emi)
            savings_list.append(monthly_savings)
        else:
            emi_burden_list.append(0)
            savings_list.append(income - expenses)
        total_savings += savings_list[-1]
        cumulative_savings.append(total_savings)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle('LoanSense — 5-Year Financial Projection', fontsize=16, fontweight='bold')

    ax1.bar(month_list, emi_burden_list, label='EMI Burden', color='#e74c3c', alpha=0.7)
    ax1.bar(month_list, savings_list, bottom=emi_burden_list, label='Monthly Savings', color='#2ecc71', alpha=0.7)
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Amount (₹)')
    ax1.set_title('Monthly EMI Burden vs Savings')
    ax1.legend()

    ax2.plot(month_list, cumulative_savings, color='#3498db', linewidth=2, label='Cumulative Savings')
    ax2.fill_between(month_list, cumulative_savings, alpha=0.3, color='#3498db')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Total Savings (₹)')
    ax2.set_title('Cumulative Savings Over 5 Years')
    ax2.legend()

    plt.tight_layout()
    plt.savefig('data/projection_chart.png')
    plt.show()
    print("✅ Chart saved to data/projection_chart.png")


if __name__ == "__main__":
    income = 60000
    expenses = 20000
    loan_amount = 500000
    annual_rate = 10
    loan_years = 5

    project_finances(income, expenses, loan_amount, annual_rate, loan_years)