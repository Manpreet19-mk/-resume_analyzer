# Resume Analyzer (Python Project)

This project is a simple **resume analyzer** built using Python.  
It reads a resume in PDF format, extracts the text, identifies technical skills, and gives a basic score based on matched skills.

This project focuses on **core Python and logic**, not advanced AI or deep learning.

---

## ✅ What This Project Does

- Reads a resume PDF file
- Extracts text from the resume
- Loads a list of technical skills from a file
- Finds which skills are present in the resume
- Calculates a score based on matched skills
- Prints the result in the terminal


---

## 📁 Project Folder Structure

resume_analyzer/
│
├── app.py # Main program file
├── requirements.txt # Required Python libraries
├── sample_resume.pdf # Sample resume for testing
│
├── data/
│ └── skills_list.txt # List of technical skills
│
├── utils/
│ ├── pdf_parser.py # Extracts text from PDF
│ ├── skill_extractor.py # Extracts skills from text
│ ├── scorer.py # Calculates score
│ └── matcher.py # (Optional future use)
│
└── venv/ # Virtual environment
## ⚙️ How to Set Up the Project

### 1. Create and activate virtual environment

```bash
python -m venv venv
source venv/Scripts/activate

2. Install required libraries
bash
Copy code
pip install -r requirements.txt
python -m spacy download en_core_web_sm

▶️ How to Run the Project
Make sure:
sample_resume.pdf is present in the main folder
skills_list.txt is present inside the data folder
Then run:
python app.py
🖥 Sample Output

Matched skills: {'python', 'sql', 'git'}
Score: 3

🧠 How Skill Matching Works
Resume text is converted to lowercase
Skills are matched using simple keyword search
Each matched skill adds to the score
The logic is transparent and easy to explain

🛠 Technologies Used
Python
PyMuPDF (for PDF reading)
Basic NLP text processing


🚀 Possible Improvements (Future Work)
Support multiple resumes
Rank resumes by score
Add a Streamlit UI
Add AI-based suggestions (optional)

👩‍💻 Author
Manpreet__