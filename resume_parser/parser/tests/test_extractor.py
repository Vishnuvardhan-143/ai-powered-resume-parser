from parser.extractor import ResumeExtractor

sample_text = """
John Doe
Software Engineer
Google
Skills: Python, Machine Learning, NLP, SQL
Phone: +1 123-456-7890
Email: john.doe@example.com
"""

extractor = ResumeExtractor(sample_text)

def test_extract_companies():
    companies = extractor.extract_entities()["companies"]
    assert any("Google" in company for company in companies)

def test_extract_emails():
    emails = extractor.extract_emails()
    assert "john.doe@example.com" in emails

def test_extract_skills():
    skills = extractor.extract_entities()["skills"]
    assert any("Python" in skill for skill in skills)

def test_extract_phones():
    phones = extractor.extract_phones()
    assert any("+1" in phone for phone in phones)
