# LoanSense — Real Indian Banking Data (June 2026)
# Source: RBI guidelines, Paisabazaar, official bank websites

BANK_DATA = {
    "SBI": {
        "name": "State Bank of India",
        "home_loan_rate_min": 7.50,
        "home_loan_rate_max": 8.70,
        "personal_loan_rate_min": 10.30,
        "personal_loan_rate_max": 15.00,
        "car_loan_rate_min": 8.75,
        "car_loan_rate_max": 10.25,
        "education_loan_rate_min": 7.15,
        "education_loan_rate_max": 11.15,
        "education_loan_max_amount": 30000000,
        "education_loan_collateral_free": 7500000,
        "education_loan_girl_concession": 0.50,
        "education_loan_moratorium": "Course + 6 months",
        "processing_fee": "0.35% (min ₹2,000)",
        "max_tenure_years": 30,
        "min_loan_amount": 1500000,
        "type": "Public Sector",
        "best_for": "Lowest rates, women borrowers, premier institutes"
    },
    "HDFC": {
        "name": "HDFC Credila",
        "home_loan_rate_min": 7.90,
        "home_loan_rate_max": 13.20,
        "personal_loan_rate_min": 10.50,
        "personal_loan_rate_max": 24.00,
        "car_loan_rate_min": 8.90,
        "car_loan_rate_max": 11.00,
        "education_loan_rate_min": 9.50,
        "education_loan_rate_max": 13.50,
        "education_loan_max_amount": 150000000,
        "education_loan_collateral_free": 7500000,
        "education_loan_girl_concession": 0.0,
        "education_loan_moratorium": "Course + 12 months",
        "processing_fee": "Up to 0.50% (min ₹3,000)",
        "max_tenure_years": 30,
        "min_loan_amount": 1500000,
        "type": "Private Sector",
        "best_for": "Fast approval, study abroad, large amounts"
    },
    "ICICI": {
        "name": "ICICI Bank",
        "home_loan_rate_min": 8.50,
        "home_loan_rate_max": 10.05,
        "personal_loan_rate_min": 10.65,
        "personal_loan_rate_max": 16.00,
        "car_loan_rate_min": 8.85,
        "car_loan_rate_max": 10.50,
        "education_loan_rate_min": 9.00,
        "education_loan_rate_max": 13.00,
        "education_loan_max_amount": 30000000,
        "education_loan_collateral_free": 15000000,
        "education_loan_girl_concession": 0.0,
        "education_loan_moratorium": "Course + 6 months",
        "processing_fee": "Up to 0.50% (min ₹3,000)",
        "max_tenure_years": 30,
        "min_loan_amount": 1500000,
        "type": "Private Sector",
        "best_for": "NRIs, self-employed, collateral-free up to ₹1.5Cr"
    },
    "AXIS": {
        "name": "Axis Bank",
        "home_loan_rate_min": 8.35,
        "home_loan_rate_max": 11.90,
        "personal_loan_rate_min": 10.49,
        "personal_loan_rate_max": 22.00,
        "car_loan_rate_min": 8.80,
        "car_loan_rate_max": 11.00,
        "education_loan_rate_min": 13.70,
        "education_loan_rate_max": 15.20,
        "education_loan_max_amount": 7500000,
        "education_loan_collateral_free": 4000000,
        "education_loan_girl_concession": 0.0,
        "education_loan_moratorium": "Course + 12 months",
        "processing_fee": "Up to 1% (min ₹10,000)",
        "max_tenure_years": 30,
        "min_loan_amount": 3000000,
        "type": "Private Sector",
        "best_for": "Balance transfer, top-up loans"
    },
    "KOTAK": {
        "name": "Kotak Mahindra Bank",
        "home_loan_rate_min": 7.99,
        "home_loan_rate_max": 12.00,
        "personal_loan_rate_min": 10.99,
        "personal_loan_rate_max": 20.00,
        "car_loan_rate_min": 8.99,
        "car_loan_rate_max": 11.50,
        "education_loan_rate_min": 10.99,
        "education_loan_rate_max": 16.00,
        "education_loan_max_amount": 10000000,
        "education_loan_collateral_free": 7500000,
        "education_loan_girl_concession": 0.0,
        "education_loan_moratorium": "Course + 6 months",
        "processing_fee": "Up to 0.50%",
        "max_tenure_years": 20,
        "min_loan_amount": 1500000,
        "type": "Private Sector",
        "best_for": "High credit score borrowers"
    }
}

# RBI Guidelines 2026
RBI_GUIDELINES = {
    "min_cibil_score": 700,
    "best_rate_cibil_score": 750,
    "min_monthly_income_salaried": 25000,
    "min_monthly_income_self_employed": 16667,
    "min_age": 21,
    "max_age_salaried": 65,
    "max_age_self_employed": 70,
    "max_foir": 0.50,
    "ltv_ratios": {
        "upto_30_lakh": 0.90,
        "30_to_75_lakh": 0.80,
        "above_75_lakh": 0.75
    }
}

# Education Loan Government Schemes 2026
EDUCATION_SCHEMES = {
    "PM_VIDYALAXMI": {
        "name": "PM Vidyalaxmi Scheme",
        "description": "Central govt scheme for top institutions",
        "max_amount": 1000000,
        "interest_rate": 0,
        "eligibility": "Family income < ₹8 lakh, top 860 institutions"
    },
    "CENTRAL_SCHEME": {
        "name": "Central Sector Interest Subsidy",
        "description": "Interest subsidy during moratorium",
        "max_amount": 1000000,
        "interest_rate": 0,
        "eligibility": "Family income < ₹4.5 lakh"
    },
    "DR_AMBEDKAR": {
        "name": "Dr. Ambedkar Interest Subsidy",
        "description": "For OBC/EBC students abroad",
        "max_amount": 2000000,
        "interest_rate": 0,
        "eligibility": "OBC/EBC students, family income < ₹8 lakh"
    }
}


def calculate_eligibility_score(income, expenses, existing_emis,
                                 cibil_score, age, employment_type):
    score = 0

    # CIBIL Score (40 points)
    if cibil_score >= 800:
        score += 40
    elif cibil_score >= 750:
        score += 35
    elif cibil_score >= 700:
        score += 25
    elif cibil_score >= 650:
        score += 15

    # FOIR (30 points)
    total_obligations = expenses + existing_emis
    foir = total_obligations / income if income > 0 else 1
    if foir <= 0.30:
        score += 30
    elif foir <= 0.40:
        score += 20
    elif foir <= 0.50:
        score += 10

    # Income adequacy (20 points)
    min_income = RBI_GUIDELINES["min_monthly_income_salaried"] if employment_type == "salaried" else RBI_GUIDELINES["min_monthly_income_self_employed"]
    if income >= min_income * 3:
        score += 20
    elif income >= min_income * 2:
        score += 15
    elif income >= min_income:
        score += 10

    # Age factor (10 points)
    if 25 <= age <= 45:
        score += 10
    elif 21 <= age <= 55:
        score += 7
    else:
        score += 3

    return min(score, 100)


def get_best_bank(loan_type, loan_amount, cibil_score):
    rate_key = f"{loan_type}_rate_min"
    eligible_banks = []
    for bank_key, bank in BANK_DATA.items():
        if rate_key in bank:
            eligible_banks.append({
                "bank": bank_key,
                "name": bank["name"],
                "rate": bank[rate_key],
                "max_rate": bank[f"{loan_type}_rate_max"],
                "best_for": bank["best_for"],
                "type": bank["type"],
                "collateral_free": bank.get("education_loan_collateral_free"),
                "moratorium": bank.get("education_loan_moratorium"),
                "girl_concession": bank.get("education_loan_girl_concession", 0)
            })
    eligible_banks.sort(key=lambda x: x["rate"])
    return eligible_banks


def get_education_loan_info(loan_amount, is_girl_student, family_income):
    """
    Returns education loan recommendations with govt schemes.
    """
    banks = get_best_bank("education_loan", loan_amount, 700)
    schemes = []

    if family_income <= 450000:
        schemes.append(EDUCATION_SCHEMES["CENTRAL_SCHEME"])
    if family_income <= 800000:
        schemes.append(EDUCATION_SCHEMES["PM_VIDYALAXMI"])
        schemes.append(EDUCATION_SCHEMES["DR_AMBEDKAR"])

    return {
        "banks": banks,
        "govt_schemes": schemes,
        "girl_concession": "0.50% rate concession available at SBI" if is_girl_student else None,
        "tax_benefit": "Interest deduction under Section 80E — no upper limit for 8 years"
    }


def calculate_max_loan_amount(income, existing_emis, annual_rate, tenure_years):
    max_emi = (income * RBI_GUIDELINES["max_foir"]) - existing_emis
    if max_emi <= 0:
        return 0
    monthly_rate = annual_rate / (12 * 100)
    n = tenure_years * 12
    max_loan = max_emi * ((1 + monthly_rate) ** n - 1) / (monthly_rate * (1 + monthly_rate) ** n)
    return round(max_loan)
# Real Document Requirements by Loan Type
DOCUMENT_REQUIREMENTS = {
    "home_loan": {
        "name": "Home Loan",
        "icon": "🏠",
        "documents": [
            {
                "name": "Aadhaar Card",
                "category": "Identity Proof",
                "mandatory": True,
                "description": "Both sides required. Must be linked to mobile number.",
                "accepted_formats": "PDF, JPG, PNG"
            },
            {
                "name": "PAN Card",
                "category": "Identity Proof",
                "mandatory": True,
                "description": "Required for loans above ₹50,000 as per RBI guidelines.",
                "accepted_formats": "PDF, JPG, PNG"
            },
            {
                "name": "Last 3 Months Salary Slips",
                "category": "Income Proof",
                "mandatory": True,
                "description": "Must show gross salary, deductions and net pay clearly.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Last 6 Months Bank Statement",
                "category": "Income Proof",
                "mandatory": True,
                "description": "Primary salary account. Must show regular salary credits.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Form 16 (Last 2 Years)",
                "category": "Income Proof",
                "mandatory": True,
                "description": "Issued by employer. Required for salaried individuals.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Property Documents",
                "category": "Property Proof",
                "mandatory": True,
                "description": "Sale agreement, title deed, NOC from builder.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Passport Size Photos",
                "category": "Other",
                "mandatory": True,
                "description": "Recent photographs, white background.",
                "accepted_formats": "JPG, PNG"
            },
            {
                "name": "Employment Certificate",
                "category": "Employment Proof",
                "mandatory": False,
                "description": "Letter from employer confirming current employment.",
                "accepted_formats": "PDF"
            }
        ]
    },
    "education_loan": {
        "name": "Education Loan",
        "icon": "🎓",
        "documents": [
            {
                "name": "Aadhaar Card (Student + Parent)",
                "category": "Identity Proof",
                "mandatory": True,
                "description": "Both student and co-applicant (parent/guardian) Aadhaar required.",
                "accepted_formats": "PDF, JPG, PNG"
            },
            {
                "name": "PAN Card (Student + Parent)",
                "category": "Identity Proof",
                "mandatory": True,
                "description": "PAN of both student and co-applicant required.",
                "accepted_formats": "PDF, JPG, PNG"
            },
            {
                "name": "Admission Letter",
                "category": "Academic Proof",
                "mandatory": True,
                "description": "Official admission letter from the institution with fee structure.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Mark Sheets (10th, 12th, Graduation)",
                "category": "Academic Proof",
                "mandatory": True,
                "description": "All previous academic records required.",
                "accepted_formats": "PDF, JPG"
            },
            {
                "name": "Fee Structure Document",
                "category": "Academic Proof",
                "mandatory": True,
                "description": "Complete fee structure from institution for entire course.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Parent's Income Proof",
                "category": "Income Proof",
                "mandatory": True,
                "description": "Salary slips or ITR of parent/guardian for last 2 years.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Bank Statement (6 Months)",
                "category": "Income Proof",
                "mandatory": True,
                "description": "Parent's primary bank account statements.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Scholarship Letter (if any)",
                "category": "Other",
                "mandatory": False,
                "description": "Any scholarship or financial aid received.",
                "accepted_formats": "PDF"
            }
        ]
    },
    "car_loan": {
        "name": "Car Loan",
        "icon": "🚗",
        "documents": [
            {
                "name": "Aadhaar Card",
                "category": "Identity Proof",
                "mandatory": True,
                "description": "Valid Aadhaar card required.",
                "accepted_formats": "PDF, JPG, PNG"
            },
            {
                "name": "PAN Card",
                "category": "Identity Proof",
                "mandatory": True,
                "description": "Required for all car loans.",
                "accepted_formats": "PDF, JPG, PNG"
            },
            {
                "name": "Last 3 Months Salary Slips",
                "category": "Income Proof",
                "mandatory": True,
                "description": "Latest salary slips showing net take-home pay.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Last 6 Months Bank Statement",
                "category": "Income Proof",
                "mandatory": True,
                "description": "Salary account bank statements.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Car Proforma Invoice",
                "category": "Vehicle Proof",
                "mandatory": True,
                "description": "Quotation from car dealer with vehicle details and price.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Driving License",
                "category": "Other",
                "mandatory": False,
                "description": "Valid driving license of applicant.",
                "accepted_formats": "PDF, JPG, PNG"
            }
        ]
    },
    "personal_loan": {
        "name": "Personal Loan",
        "icon": "💰",
        "documents": [
            {
                "name": "Aadhaar Card",
                "category": "Identity Proof",
                "mandatory": True,
                "description": "Valid Aadhaar card required.",
                "accepted_formats": "PDF, JPG, PNG"
            },
            {
                "name": "PAN Card",
                "category": "Identity Proof",
                "mandatory": True,
                "description": "Required for all personal loans.",
                "accepted_formats": "PDF, JPG, PNG"
            },
            {
                "name": "Last 3 Months Salary Slips",
                "category": "Income Proof",
                "mandatory": True,
                "description": "Latest salary slips required.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Last 3 Months Bank Statement",
                "category": "Income Proof",
                "mandatory": True,
                "description": "Primary salary account statements.",
                "accepted_formats": "PDF"
            },
            {
                "name": "Employment ID Card",
                "category": "Employment Proof",
                "mandatory": False,
                "description": "Company ID card for identity verification.",
                "accepted_formats": "JPG, PNG"
            }
        ]
    }
}


if __name__ == "__main__":
    score = calculate_eligibility_score(
        income=60000, expenses=20000, existing_emis=0,
        cibil_score=750, age=30, employment_type="salaried"
    )
    print(f"Eligibility Score: {score}/100")

    print("\n🎓 Education Loan — Best Banks:")
    edu_info = get_education_loan_info(1000000, True, 400000)
    for b in edu_info["banks"][:3]:
        print(f"  {b['name']}: {b['rate']}% — {b['best_for']}")

    print("\n🏛️ Government Schemes Available:")
    for s in edu_info["govt_schemes"]:
        print(f"  {s['name']}: {s['description']}")

    print(f"\n💰 Tax Benefit: {edu_info['tax_benefit']}")