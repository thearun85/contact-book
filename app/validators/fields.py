from app.validators.result import ValidationResult

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
