from data import calculate_eligibility_score, get_education_loan_info

score = calculate_eligibility_score(60000, 20000, 0, 750, 30, 'salaried')
print(f'Eligibility Score: {score}/100')

edu = get_education_loan_info(1000000, True, 400000)
for b in edu['banks'][:3]:
    print(f"{b['name']}: {b['rate']}%")

print("Done!")