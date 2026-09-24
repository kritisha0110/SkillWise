import numpy as np

DIMENSIONS = [
    "programming", "dsa", "maths_stats", "communication",
    "sql_data_analysis", "creative_design", "leadership_management",
    "problem_solving", "git_version_control", "cloud_platforms", "ai_ml_concepts"
]

ROLE_PROFILES = {
    "Data Analyst":                 [7, 5, 6, 8, 10, 4, 6, 7, 7, 4, 6],
    "Data Scientist / ML Engineer": [9, 6, 9, 6, 9, 6, 5, 8, 8, 6, 10],
    "Backend Developer":            [10, 9, 5, 6, 5, 5, 5, 9, 10, 6, 6],
    "Frontend Developer":           [8, 6, 5, 7, 4, 10, 6, 7, 8, 4, 5],
    "Product Manager":              [5, 4, 6, 9, 5, 8, 10, 8, 5, 4, 6],
    "UI/UX Designer":               [3, 2, 3, 8, 3, 10, 6, 7, 3, 2, 3],
}

def score_roles(user_ratings):
    user_vec = np.array(user_ratings)
    results = {}
    for role, profile in ROLE_PROFILES.items():
        role_vec = np.array(profile)
        similarity = np.dot(user_vec, role_vec) / (np.linalg.norm(user_vec) * np.linalg.norm(role_vec))
        results[role] = round(similarity * 100, 1)
    return results

# TEST: yeh ek fake user hai jiske numbers strong coding-wale hain, weak leadership
test_user = [3, 2, 4, 8, 3, 10, 7, 6, 3, 2, 3]

scores = score_roles(test_user)
for role, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{role}: {score}%")