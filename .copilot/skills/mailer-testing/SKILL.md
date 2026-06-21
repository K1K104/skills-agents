# Mailer Complete Testing Skill

## Cel
Kompleksowe wskazówki i szablony do testowania wszystkich komponentów projektu Mailer.

## Zakres
1. Email Validation
2. Email Sending
3. Subscribers Management
4. Web Interface (Flask)

## Test Template

```python
import pytest
from unittest.mock import Mock, patch
from mailer.email_sender import EmailSender
from mailer.subscribers import SubscriberManager

class TestMailerComponent:
    @pytest.fixture
    def setup(self):
        # Setup fixture
        pass
    
    def test_happy_path(self, setup):
        # Main scenario
        pass
    
    def test_edge_cases(self, setup):
        # Edge cases
        pass
    
    def test_error_handling(self, setup):
        # Error scenarios
        pass
```

## Coverage Requirements
- Functions: 100%
- Branches: 80%
- Lines: 85%

## Narzędzia
- pytest
- pytest-cov
- pytest-mock
- coverage
