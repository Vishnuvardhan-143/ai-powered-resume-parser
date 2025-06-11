import spacy
import re
from parser.utils import extract_emails, extract_phone_numbers

# Load sample skill set (can be extended easily)
SKILL_KEYWORDS = [
    "Python", "Java", "Machine Learning", "Deep Learning", "NLP",
    "SQL", "C++", "Data Science", "AI", "AWS", "Docker"
]

class ResumeExtractor:
    def __init__(self, file_text):
        self.text = file_text
        self.nlp = spacy.load("en_core_web_sm")
        self.doc = self.nlp(self.text)

    def extract_entities(self):
        companies = []
        degrees = []

        for ent in self.doc.ents:
            if ent.label_ == "ORG":
                companies.append(ent.text.strip())
            if ent.label_ in ["EDUCATION", "WORK_OF_ART"]:
                degrees.append(ent.text.strip())

        skills = self.extract_skills()

        return {
            "skills": list(set(skills)),
            "companies": list(set(companies)),
            "degrees": list(set(degrees))
        }

    def extract_skills(self):
        found_skills = []
        for skill in SKILL_KEYWORDS:
            if skill.lower() in self.text.lower():
                found_skills.append(skill)
        return found_skills

    def extract_emails(self):
        return extract_emails(self.text)

    def extract_phones(self):
        return extract_phone_numbers(self.text)
