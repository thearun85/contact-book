from app.validators.result import ValidationResult

def validate_primary_flag(items: list[dict], field:str)->ValidationResult:

    result = ValidationResult()
    if len(items) <= 1:
        return result
        
    count = 0
    count = sum(1 for item in items if item.get("is_primary") is True)

    if count == 0:
        result.add_error(field, "One item must be marked as primary.")
    elif count > 1:
        result.add_error(field, "Only one item can be marked as primary.")

    return result

def validate_duplicate_emails(emails:list[dict])->ValidationResult:

    result = ValidationResult()

    if len(emails) == 0:
        return result

    seen = set()
    for i, email_data in enumerate(emails):
        email = email_data["email"].strip().lower()
        if email in seen:
            result.add_error(f"emails[{i}].email", "Duplicate email address")
        seen.add(email)
    return result

def validate_duplicate_phones(phones: list[dict])->ValidationResult:

    result = ValidationResult()
    if len(phones) == 0:
        return result

    seen = set()
    
    for i, phone_data in enumerate(phones):
        phone = phone_data["number"].strip().replace(" ","").replace("-", "").replace("(", "").replace(")", "")
        if phone in seen:
            result.add_error(f"phones[{i}].number", "Duplicate phone number.")    
        seen.add(phone)

    return result
            
