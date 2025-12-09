from __future__ import annotations

class ValidationResult:
    def __init__(self):
        self.errors: list[dict] = []

    def add_error(self, field: str, message: str):
        self.errors.append({
            "field": field,
            "message": message
        })
    

    def is_valid(self):
        return len(self.errors) == 0

    def merge(self, other: ValidationResult):
        return self.errors.extend(other.errors)

    def to_dict(self):
        return {
            "error": "ValidationFailed",
            "details": self.errors
        }
