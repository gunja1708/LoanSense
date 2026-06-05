# Module 1 — Document Verifier
# extractor.py — Extracts key fields from loan documents

def extract_fields(document_text):
    """
    Takes raw text from a document and extracts key fields.
    Returns a dictionary of extracted information.
    """
    extracted = {
        "name": None,
        "pan_number": None,
        "income": None,
        "bank_name": None,
        "account_number": None,
        "anomalies": []
    }

    # Check for PAN number (format: ABCDE1234F)
    import re
    pan_pattern = r'[A-Z]{5}[0-9]{4}[A-Z]{1}'
    pan_match = re.search(pan_pattern, document_text)
    if pan_match:
        extracted["pan_number"] = pan_match.group()
    else:
        extracted["anomalies"].append("PAN number not found")

    # Check for income (looks for ₹ or Rs followed by numbers)
    income_pattern = r'[₹Rs\.]+\s?[\d,]+'
    income_match = re.search(income_pattern, document_text)
    if income_match:
        extracted["income"] = income_match.group()
    else:
        extracted["anomalies"].append("Income amount not found")

    return extracted


def verify_document(document_text):
    """
    Verifies the document and flags any anomalies.
    """
    print("🔍 Scanning document...\n")
    result = extract_fields(document_text)

    print(f"✅ PAN Number  : {result['pan_number']}")
    print(f"✅ Income      : {result['income']}")

    if result["anomalies"]:
        print("\n⚠️  Anomalies detected:")
        for issue in result["anomalies"]:
            print(f"   ❌ {issue}")
    else:
        print("\n✅ Document looks clean — no anomalies found!")

    return result


# Test it with a sample document
if __name__ == "__main__":
    sample_document = """
    Name: Gunja Sharma
    PAN: ABCDE1234F
    Bank: State Bank of India
    Monthly Income: ₹45,000
    Account: 9876543210
    """

    verify_document(sample_document)