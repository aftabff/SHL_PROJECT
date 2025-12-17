import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data(csv_path: str) -> pd.DataFrame:
    """
    Load SHL assessment catalog from CSV
    """
    return pd.read_csv(csv_path)


def recommend_assessments(
    candidate_skills: list,
    job_family: str,
    data: pd.DataFrame,
    top_n: int = 3
) -> pd.DataFrame:
    """
    Recommend top N assessments based on skill and job similarity
    """

    # Combine text fields
    data = data.copy()
    data["combined"] = data["skills"] + " " + data["job_family"]

    # Build corpus
    corpus = data["combined"].tolist()
    candidate_text = " ".join(candidate_skills) + " " + job_family
    corpus.append(candidate_text)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    similarity_scores = cosine_similarity(
        tfidf_matrix[-1], tfidf_matrix[:-1]
    ).flatten()

    data["score"] = similarity_scores

    return data.sort_values("score", ascending=False).head(top_n)


def main():
    df = load_data("shl_data.csv")

    candidate_profile = {
        "skills": ["python", "sql", "statistics"],
        "job_family": "Data Analyst"
    }

    results = recommend_assessments(
        candidate_profile["skills"],
        candidate_profile["job_family"],
        df
    )

    print("\nRecommended Assessments:\n")
    print(results[["assessment_name", "job_family", "score"]])


if __name__ == "__main__":
    main()
