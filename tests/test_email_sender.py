from unittest.mock import patch, MagicMock
from mailer.email_sender import EmailSender

@patch('smtplib.SMTP')
def test_email_sender_success(mock_smtp_class):
    mock_smtp = MagicMock()
    mock_smtp_class.return_value.__enter__.return_value = mock_smtp

    sender = EmailSender(smtp_host='localhost', smtp_port=25)
    result = sender.send('user@example.com', 'Hi', 'Body')

    assert result.success is True
    mock_smtp.sendmail.assert_called()

@patch('smtplib.SMTP')
def test_email_sender_failure(mock_smtp_class):
    mock_smtp = MagicMock()
    mock_smtp.sendmail.side_effect = Exception('boom')
    mock_smtp_class.return_value.__enter__.return_value = mock_smtp

    sender = EmailSender()
    result = sender.send('user@example.com', 'Hi', 'Body')

    assert result.success is False
    assert 'boom' in result.error
