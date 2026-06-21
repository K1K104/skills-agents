import re
from typing import Optional

class EmailValidator:
    PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    @staticmethod
    def validate(email: Optional[str]) -> bool:
        """Waliduj format emaila (prosty regex, RFC-inspired)."""
        if not email or not isinstance(email, str):
            return False
        return bool(re.match(EmailValidator.PATTERN, email.strip()))
