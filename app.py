from src.recommender import load_data, recommend_assessments

def run_demo():
    df = load_data("shl_data.csv")

    print("SHL Assessment Recommendation Engine\n")

    job_family = input("Enter Job Family (e.g. Data Analyst): ")
    skills_input = input("Enter skills (comma separated): ")

    candidate_skills = [s.strip().lower() for s in skills_input.split(",")]

    results = recommend_assessments(
        candidate_skills=candidate_skills,
        job_family=job_family,
        data=df,
        top_n=3
    )

    print("\nRecommended Assessments:\n")
    print(results[["assessment_name", "job_family", "difficulty", "score"]])


if __name__ == "__main__":
    run_demo()
