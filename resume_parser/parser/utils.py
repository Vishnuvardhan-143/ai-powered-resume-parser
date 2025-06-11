import re

EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
PHONE_REGEX = r'(\+?\d{1,3})?[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'

def extract_emails(text):
    return re.findall(EMAIL_REGEX, text)

def extract_phone_numbers(text):
    return re.findall(PHONE_REGEX, text)
