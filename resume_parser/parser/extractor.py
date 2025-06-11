import spacy
from parser import utils

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = ["Python", "Java", "Machine Learning", "NLP", "Deep Learning", "Git", "SQL"]
DEGREES_DB = ["B.Tech", "M.Tech", "BSc", "MSc", "PhD", "Bachelor", "Master", "Doctor"]

class ResumeExtractor:
    def __init__(self, text):
        self.text = text
        self.doc = nlp(text)

    def extract_entities(self):
        companies = [ent.text for ent in self.doc.ents if ent.label_ == "ORG"]
        return {"companies": companies}

    def extract_skills(self):
        skills = []
        for skill in SKILLS_DB:
            if skill.lower() in self.text.lower():
                skills.append(skill)
        return skills

    def extract_degrees(self):
        degrees = []
        for degree in DEGREES_DB:
            if degree.lower() in self.text.lower():
                degrees.append(degree)
        return degrees

    def extract_emails(self):
        return utils.extract_emails(self.text)

    def extract_phones(self):
        return utils.extract_phone_numbers(self.text)

    def extract_all(self):
        return {
            "skills": self.extract_skills(),
            "companies": self.extract_entities()["companies"],
            "degrees": self.extract_degrees(),
            "emails": self.extract_emails(),
            "phone_numbers": self.extract_phones()
        }
