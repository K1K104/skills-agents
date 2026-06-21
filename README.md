# Mailer (Exercise)

This repository contains a small Flask-based Mailer example used for the Copilot Skills/Agents exercise.

Quickstart

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Unix
# source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run tests:

```bash
pytest -q
```

4. Run the app (for local testing):

```bash
set FLASK_APP=mailer.web
flask run
```

Files of interest
- `mailer/validators.py` — Email validation helper
- `mailer/subscribers.py` — In-memory subscriber manager
- `mailer/email_sender.py` — Simple SMTP-based sender (used in tests with mocks)
- `mailer/web.py` — Minimal Flask app

This scaffold includes tests and basic templates, suitable for extending as part of the exercise.
