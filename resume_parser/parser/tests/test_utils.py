from parser import utils

def test_extract_emails():
    text = "Contact: abc@example.com"
    assert utils.extract_emails(text) == ["abc@example.com"]

def test_extract_phone_numbers():
    text = "Call me at +1 123-456-7890"
    assert utils.extract_phone_numbers(text) == ['+1 ']
