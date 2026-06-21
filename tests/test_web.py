import pytest

from mailer.web import app, manager

@pytest.fixture(autouse=True)
def clear_subscribers():
    manager._subs.clear()
    yield
    manager._subs.clear()

def test_index_page_loads():
    app.config['TESTING'] = True
    with app.test_client() as client:
        response = client.get('/')

    assert response.status_code == 200
    assert b'Witaj, Go%C5%9B%C4%87' not in response.data
    assert b'Witaj, ' in response.data
    assert b'<form method="post" action="/subscribe">' in response.data

@pytest.mark.parametrize('email', ['user@example.com', 'test+1@domain.pl'])
def test_subscribe_success(email):
    app.config['TESTING'] = True
    with app.test_client() as client:
        response = client.post('/subscribe', data={'email': email})

    assert response.status_code == 302
    assert email in manager.list()

@pytest.mark.parametrize('email', ['', 'invalid', 'no-at.com', 'user@'])
def test_subscribe_invalid_email(email):
    app.config['TESTING'] = True
    with app.test_client() as client:
        response = client.post('/subscribe', data={'email': email})

    assert response.status_code == 400
    assert b'Nieprawid' in response.data

def test_subscribe_duplicate():
    app.config['TESTING'] = True
    manager.add('dup@example.com')
    with app.test_client() as client:
        response = client.post('/subscribe', data={'email': 'dup@example.com'})

    assert response.status_code == 400
    assert b'duplikat' in response.data
