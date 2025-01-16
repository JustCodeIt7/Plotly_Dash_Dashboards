#%%
import plotly.express as px

# %%
# Create a sample dataset
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 15, 7, 20]
}

# Create a basic dot plot
fig = px.scatter(data, x="Category", y="Values", title="Basic Dot Plot", labels={"x": "Category", "y": "Values"})

# Show the plot
fig.show()

# %%
import plotly.express as px
import pandas as pd

# Data: Students' scores in different subjects
students = ["Alice", "Bob", "Charlie", "Diana", "Edward"]
subjects = ["Math", "Science", "English", "History", "Art"]

# Scores by each student in each subject
scores = [
    [85, 90, 88, 95, 80],  # Alice
    [78, 85, 82, 90, 75],  # Bob
    [92, 88, 84, 89, 83],  # Charlie
    [88, 92, 91, 94, 87],  # Diana
    [75, 80, 78, 85, 70]   # Edward
]

# Create a DataFrame
data = []
for student, student_scores in zip(students, scores):
    for subject, score in zip(subjects, student_scores):
        data.append({"Student": student, "Subject": subject, "Score": score})

df = pd.DataFrame(data)

# Create a dot plot
fig = px.scatter(
    df,
    x="Score",
    y="Subject",
    color="Student",
    title="Students' Performance Across Subjects",
    labels={"Score": "Score (out of 100)", "Subject": "Subjects"},
    size="Score",  # Optionally adjust dot size
)

fig.show()
# %%
import plotly.express as px
import pandas as pd

# Categorical data for styled dot plot
categories = ["Group A", "Group B", "Group C", "Group D"]
values = [10, 15, 5, 20]

# Create a DataFrame for the plot
styled_data = pd.DataFrame({
    "Category": categories,
    "Value": values
})

# Create a styled dot plot
fig = px.scatter(
    styled_data,
    x="Category",
    y="Value",
    title="Styled Categorical Dot Plot",
    labels={"Value": "Values", "Category": "Categories"},
    color="Category",  # Color dots by category
    size="Value",  # Size based on value
    template="plotly_dark"  # Apply a dark theme to differentiate
)

# Show the plot
fig.show()
# %%


# %%