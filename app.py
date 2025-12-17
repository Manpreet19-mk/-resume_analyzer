import os
from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import load_skills, extract_skills
from utils.scorer import calculate_score

print("APP STARTED")

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print("BASE DIR:", BASE_DIR)

    skills_file = os.path.join(BASE_DIR, "utils", "data", "skills_list.txt")

    resume_file = os.path.join(BASE_DIR, "sample_resume.pdf")

    print("SKILLS FILE PATH:", skills_file)
    print("RESUME FILE PATH:", resume_file)

    skills = load_skills(skills_file)
    text = extract_text_from_pdf(resume_file)
    matched_skills = extract_skills(text, skills)
    score = calculate_score(matched_skills)

    print("Matched skills:", matched_skills)
    print("Score:", score)

if __name__ == "__main__":
    main()
