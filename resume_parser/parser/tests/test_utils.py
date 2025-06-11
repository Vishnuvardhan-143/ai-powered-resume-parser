from parser import utils

def test_extract_emails():
    text = "My email is test.user@example.com"
    assert utils.extract_emails(text) == ["test.user@example.com"]

def test_extract_phone_numbers():
    text = "Call me at +1 123-456-7890"
    assert utils.extract_phone_numbers(text) == [('+1',)]
