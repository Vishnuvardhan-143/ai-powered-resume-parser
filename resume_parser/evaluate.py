import json
from sklearn.metrics import precision_score, recall_score

# Dummy evaluation script (for illustration)

manual = {"skills": ["Python", "SQL", "NLP", "Machine Learning"]}
parsed = {"skills": ["Python", "SQL", "NLP"]}

def evaluate(manual, parsed):
    manual_set = set(manual["skills"])
    parsed_set = set(parsed["skills"])

    tp = len(manual_set & parsed_set)
    fp = len(parsed_set - manual_set)
    fn = len(manual_set - parsed_set)

    precision = tp / (tp + fp + 1e-6)
    recall = tp / (tp + fn + 1e-6)

    print(f"Precision: {precision:.2%}")
    print(f"Recall: {recall:.2%}")

if __name__ == "__main__":
    evaluate(manual, parsed)
