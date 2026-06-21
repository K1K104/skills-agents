from typing import NamedTuple, Optional
import smtplib

class SendResult(NamedTuple):
    success: bool
    error: Optional[str]

class EmailSender:
    def __init__(self, smtp_host: str = 'localhost', smtp_port: int = 25):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port

    def send(self, to_address: str, subject: str, body: str, from_address: str = 'noreply@example.com') -> SendResult:
        """Wyślij prostą wiadomość e-mail (sync). Zwraca SendResult."""
        try:
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
                msg = f"Subject: {subject}\nTo: {to_address}\nFrom: {from_address}\n\n{body}"
                smtp.sendmail(from_address, [to_address], msg)
            return SendResult(True, None)
        except Exception as e:
            return SendResult(False, str(e))
