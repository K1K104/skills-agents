from mailer.subscribers import SubscriberManager

def test_subscriber_add_and_list():
    mgr = SubscriberManager()
    assert mgr.add('user@example.com')
    assert mgr.list() == ['user@example.com']

def test_subscriber_duplicates():
    mgr = SubscriberManager()
    assert mgr.add('a@b.com')
    assert not mgr.add('a@b.com')

def test_remove_subscriber():
    mgr = SubscriberManager()
    mgr.add('x@y.com')
    assert mgr.remove('x@y.com')
    assert mgr.list() == []
    assert not mgr.remove('noone@x.com')
