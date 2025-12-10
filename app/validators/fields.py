from app.validators.result import ValidationResult
import re
from datetime import datetime, date

EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9_.]+\.[a-zA-Z]{2,}$"
)

PHONE_PATTERN = re.compile(
    r"^\+[1-9]\d{1,14}$"
)

def validate_name(value: str, field: str, min_length: int=1, max_length:int=100)->ValidationResult:
    result = ValidationResult()

    if not isinstance(value, str):
        add_error(field, "Must be a string")
        return result

    value = value.strip()
    if len(value) < min_length:
        result.add_error(field, f"Length must be atleast {min_length} characters.")
        return result

    if len(value) > max_length:
        result.add_error(field, f"Cannot exceed {max_length} characters.")
    return result

def validate_email(value:str, length:int, field:str="email")->ValidationResult:
    result = ValidationResult()

    if not isinstance(value, str):
        result.add_error(field, "Must be a string")
        return result

    value = value.strip()
    if not value:
        result.add_error(field, "Cannot be empty")
        return result

    if len(value) > length:
        result.add_error(field, f"Cannot exceed {length} characters.")
        return result

    if not EMAIL_PATTERN.match(value):
        result.add_error(field, "Invalid Email format")
    return result

def validate_phone(value:str, field:str="phone")->ValidationResult:
    result = ValidationResult()
    if not isinstance(value, str):
        result.add_error(field, "Must be a string")
        return result

    value = value.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

    if not value:
        result.add_error(field, "Cannot be empty")
        return result

    if not value.startswith("+"):
        result.add_error(field, "Invalid format. Must start with +")
        return result

    if not PHONE_PATTERN.match(value):
        result.add_error(field, "Invalid format. Example: '+1656565656'")

    return result

def validate_date_of_birth(value:str, field="date_of_birth")->ValidationResult:
    result = ValidationResult()

    if not isinstance(value, str):
        result.add_error(field, "Must be a string")
        return result
        
    try:
        parsed = datetime.strptime(value, '%Y-%m-%d').date()
    except ValueError:
        result.add_error(field, "Invalid date format. Expected: YYYY-MM-DD")
        return result

    if parsed > date.today():
        result.add_error(field, "Cannot be in the future")
        return result

    if parsed.year < 1900:
        result.add_error(field, "Year must be 1900 or later")
    return result
