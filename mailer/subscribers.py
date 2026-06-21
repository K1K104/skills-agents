from typing import List
from .validators import EmailValidator

class SubscriberManager:
    """Prosty menedżer subskrybentów przechowujący listę w pamięci."""
    def __init__(self):
        self._subs: List[str] = []

    def add(self, email: str) -> bool:
        if not EmailValidator.validate(email):
            return False
        if email in self._subs:
            return False
        self._subs.append(email)
        return True

    def remove(self, email: str) -> bool:
        try:
            self._subs.remove(email)
            return True
        except ValueError:
            return False

    def list(self) -> List[str]:
        return list(self._subs)
