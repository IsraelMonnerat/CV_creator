import re

def validate_field(field: str, pattern: str) -> bool:
    """
    Validates a field against a given pattern.

    Args:
        field (str): The field to be validated.
        pattern (str): The pattern to match against the field.

    Returns:
        bool: True if the field matches the pattern, False otherwise.
    """
    return re.match(pattern, field) is not None
