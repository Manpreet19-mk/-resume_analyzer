def load_skills(filepath):
    skills = set()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            skill = line.strip().lower()
            if skill:
                skills.add(skill)
    return skills


def extract_skills(text, skills_set):
    found = set()
    for skill in skills_set:
        if skill in text:
            found.add(skill)
    return found
