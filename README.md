## SHL Assessment Recommendation Engine — Machine Learning Project

This is a **machine learning–based assessment recommendation system** built using **Python**.  
It was developed as part of the **SHL Research Intern Assessment** to demonstrate skills in  
**data processing, text similarity, and recommendation logic**.

---

### About the Project

The **SHL Assessment Recommendation Engine** recommends the most relevant SHL assessments based on a
candidate’s **job family** and **skill set**.

The system uses **TF-IDF vectorization** to represent textual data and **cosine similarity**
to measure relevance between candidate profiles and available assessments.

All recommendations are generated dynamically from a structured assessment catalog.

---

## Features

-  ML-based recommendation engine using TF-IDF
-  Cosine similarity for assessment ranking
-  Interactive command-line interface
-  Clean and modular project structure
-  Fully reproducible setup using virtual environments
-  Ideal for learning, assessment, and portfolio use

---

## Tech Stack

- Python 3
- Pandas
- Scikit-learn

---

## 📁 Folder Structure

```bash
SHL_PROJECT/
├── shl_data.csv
├── src/
│   └── recommender.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```
Setup Instructions
```bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```
How to Run
```bash

Quick Run (Predefined Input)
```

Interactive Mode
```bash
python app.py
```



Example Input
```bash
Job Family: Data Analyst
Skills: Python, SQL, Statistics
Example Output
Top recommended assessments ranked by similarity score:
Data Interpretation Test
SQL Skills Assessment
Numerical Reasoning Test
Notes
The assessment catalog used in this project is synthetic and created only for demonstration purposes.
The focus of this project is on clarity, correctness, and reproducibility.
The system can be easily extended with a web UI, API, or advanced recommendation logic.
```
Developed by Alok Yadav

---












