import re
from load_data import load_json_data

sensitive_info_keywords = ["balance", "account number", "credit card", "debt amount"]
verification_keywords = ["date of birth", "address", "SSN"]

def check_compliance(conversation):
    """Check if a conversation violates privacy compliance."""
    verified = any(re.search(rf"\b{word}\b", entry["text"], re.IGNORECASE) for word in verification_keywords for entry in conversation)
    sensitive_shared = any(re.search(rf"\b{word}\b", entry["text"], re.IGNORECASE) for word in sensitive_info_keywords for entry in conversation)
    return not sensitive_shared or verified  # Compliance OK if no sensitive info was shared or if verification happened first.

if __name__ == "__main__":
    json_data_folder = "data"
    all_data = load_json_data(json_data_folder)
    compliance_results = [conv for conv in all_data if not check_compliance(conv)]
    print(f"Privacy Violations Found in {len(compliance_results)} conversations")
