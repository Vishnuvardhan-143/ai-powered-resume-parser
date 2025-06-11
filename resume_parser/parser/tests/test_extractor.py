from parser.extractor import ResumeExtractor

sample_text = """
John Doe
Email: john.doe@example.com
Phone: +1 123-456-7890
Education: B.Tech in Computer Science
Experience at Google
Skills: Python, Machine Learning, NLP, SQL
"""

extractor = ResumeExtractor(sample_text)

def test_extract_skills():
    skills = extractor.extract_skills()
    assert "Python" in skills
    assert "NLP" in skills

def test_extract_companies():
    companies = extractor.extract_entities()["companies"]
    assert "Google" in companies

def test_extract_degrees():
    degrees = extractor.extract_degrees()
    assert "B.Tech" in degrees

def test_extract_emails():
    emails = extractor.extract_emails()
    assert "john.doe@example.com" in emails

def test_extract_phones():
    phones = extractor.extract_phones()
    assert ('+1',) in phones
