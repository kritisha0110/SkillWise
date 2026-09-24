import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="SkillWise", page_icon="🎯", layout="wide")

DIMENSIONS = [
    "programming", "dsa", "maths_stats", "communication",
    "sql_data_analysis", "creative_design", "leadership_management",
    "problem_solving", "git_version_control", "cloud_platforms", "ai_ml_concepts"
]

DIMENSION_LABELS = {
    "programming": "Programming",
    "dsa": "DSA",
    "maths_stats": "Maths & Stats",
    "communication": "Communication",
    "sql_data_analysis": "SQL & Data Analysis",
    "creative_design": "Creative & Design Thinking",
    "leadership_management": "Leadership & Management",
    "problem_solving": "Problem Solving",
    "git_version_control": "Git/Version Control",
    "cloud_platforms": "Cloud Platforms",
    "ai_ml_concepts": "AI/ML Concepts",
}

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

# ---------- STYLING ----------
st.markdown("""
<style>
div[class*="st-key-skillbox"] {
    background-color: #3a3420 !important;
    border: 2px solid #FFD700 !important;
    border-radius: 12px !important;
    padding: 10px !important;
}
.stSlider label {
    text-align: center;
    display: block;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 style='text-align: center;'>SkillWise</h1>", unsafe_allow_html=True)
st.write("Estimate your skills on a scale of 1-10 (10 being high proficiency) using the sliders below")

# ---------- SLIDERS ----------
user_ratings = []
col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

for i, dim in enumerate(DIMENSIONS):
    with columns[i % 3]:
        with st.container(border=True, key=f"skillbox_{dim}"):
            rating = st.slider(DIMENSION_LABELS[dim], min_value=1, max_value=10, value=5)
            user_ratings.append(rating)

# ---------- RESULTS ----------
if st.button("Check My Fit"):
    scores = score_roles(user_ratings)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    roles = [item[0] for item in sorted_scores]
    percentages = [item[1] for item in sorted_scores]

    st.subheader("Your Results:")

    fig = px.bar(
        x=percentages,
        y=roles,
        orientation="h",
        labels={"x": "Match %", "y": "Role"},
        title="Career Fit Scores"
    )
    fig.update_xaxes(range=[min(percentages) - 5, max(percentages) + 2])
    st.plotly_chart(fig)

    st.subheader("Your Skill Breakdown:")
    skill_labels = [DIMENSION_LABELS[dim] for dim in DIMENSIONS]
    fig2 = px.pie(
        names=skill_labels,
        values=user_ratings,
        title="Your Skill Distribution"
    )
    st.plotly_chart(fig2)