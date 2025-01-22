# ================
# 1. IMPORTS & DATA PREP
# ================
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Create sample dataset
np.random.seed(42)
num_records = 150
df = pd.DataFrame(
    {
        "Age": np.random.randint(20, 60, num_records),
        "Salary": np.random.randint(30000, 150000, num_records),
        "Department": np.random.choice(["IT", "HR", "Sales"], num_records),
        "PerformanceScore": np.random.uniform(1, 10, num_records).round(2),
    }
)

# ================
# 2. MULTIDIMENSIONAL SCATTER PLOT
# ================
fig_multi = px.scatter(
    df,
    x="Age",
    y="Salary",
    color="Department",
    size="PerformanceScore",
    title="<b>Multivariate Analysis</b><br>Age vs Salary by Department & Performance",
    labels={"Salary": "Salary (USD)", "PerformanceScore": "Performance"},
    hover_data=["Department", "PerformanceScore"],
    size_max=20,
    color_discrete_sequence=px.colors.qualitative.Vivid,
)

# Add layout customization
fig_multi.update_layout(
    hoverlabel=dict(bgcolor="white", font_size=12),
    legend=dict(orientation="h", y=-0.15),
    title_x=0.5,
    plot_bgcolor="rgba(240,240,240,0.8)",
)

# ================
# 3. FACETED PLOTS WITH STATISTICS
# ================
fig_facet = px.scatter(
    df,
    x="Age",
    y="Salary",
    color="PerformanceScore",
    facet_col="Department",
    facet_col_wrap=1,
    title="<b>Faceted Analysis</b><br>Departmental Salary Distributions",
    height=700,
    color_continuous_scale="Viridis",
)

# Add average salary lines and annotations
for i, department in enumerate(df["Department"].unique(), 1):
    avg_salary = df[df["Department"] == department]["Salary"].mean()
    fig_facet.add_hline(
        y=avg_salary,
        line_dash="dot",
        line_color="red",
        annotation_text=f"Avg: ${avg_salary:,.0f}",
        annotation_position="top right",
        row=i,
        col=1,
    )

# ================
# 4. COMPARATIVE SUBPLOTS
# ================
fig_subplots = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=("<b>IT Department</b>", "<b>HR Department</b>"),
    shared_yaxes=True,
    horizontal_spacing=0.1,
)

# IT Department Subplot
it_scatter = px.scatter(
    df[df["Department"] == "IT"],
    x="Age",
    y="Salary",
    color="PerformanceScore",
    size="PerformanceScore",
    color_continuous_scale="Bluered",
).update_traces(name="IT", showlegend=True)

# HR Department Subplot
hr_scatter = px.scatter(
    df[df["Department"] == "HR"],
    x="Age",
    y="Salary",
    color="PerformanceScore",
    size="PerformanceScore",
    color_continuous_scale="Tealrose",
).update_traces(name="HR", showlegend=True)

# Combine subplots
fig_subplots.add_trace(it_scatter.data[0], row=1, col=1)
fig_subplots.add_trace(hr_scatter.data[0], row=1, col=2)

# Format subplots
fig_subplots.update_layout(
    title_text="<b>Department Comparison</b><br>Performance Impact Analysis",
    coloraxis_showscale=False,
    legend=dict(orientation="h", y=-0.2),
    height=500,
)
fig_subplots.update_xaxes(title_text="Age", row=1, col=1)
fig_subplots.update_xaxes(title_text="Age", row=1, col=2)
fig_subplots.update_yaxes(title_text="Salary (USD)", row=1, col=1)

# ================
# 5. DISPLAY ALL PLOTS
# ================
fig_multi.show()
fig_facet.show()
fig_subplots.show()
