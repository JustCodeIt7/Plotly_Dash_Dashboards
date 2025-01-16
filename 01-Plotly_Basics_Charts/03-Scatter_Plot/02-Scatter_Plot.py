# %%
# 1. IMPORT LIBRARIES
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# %%
# 2. CREATE A SAMPLE DATASET
# In this example, we'll simulate data representing employee
# demographics and salaries within a company.
#   - 'Age': random ages between 20 and 60
#   - 'Salary': random salaries between 30d 150k
#   - 'Department': categorical feature with 3 departments
#   - 'PerformanceScore': numeric score between 1 and 10


np.random.seed(42)  # For reproducible random numbers

num_records = 150
ages = np.random.randint(20, 60, size=num_records)
salaries = np.random.randint(30000, 150000, size=num_records)
departments = np.random.choice(['IT', 'HR', 'Sales'], size=num_records)
performance = np.random.uniform(1, 10, size=num_records).round(2)

df = pd.DataFrame({
    'Age': ages,
    'Salary': salaries,
    'Department': departments,
    'PerformanceScore': performance
})

# Let's take a quick look at the first few rows:
print(df.head())

# %%
# 3. BASIC SCATTER PLOT
# ------------------------------------------------------------
# We'll create a simple scatter plot of Age vs. Salary.
fig_basic = px.scatter(
    df,
    x='Age',
    y='Salary',
    title='Basic Scatter Plot: Age vs. Salary'
)
fig_basic.show()

# %%
# 4. SCATTER PLOT WITH COLOR AND SIZE
# ------------------------------------------------------------
# We can enhance our scatter plot by coloring points by Department
# and scaling the marker size by PerformanceScore.
# This allows us to visualize three variables in a 2D plot.
fig_color_size = px.scatter(
    df,
    x='Age',
    y='Salary',
    color='Department',
    size='PerformanceScore',
    title='Scatter Plot with Color by Department and Size by PerformanceScore',
    labels={
        'Age': 'Employee Age',
        'Salary': 'Salary (USD)',
        'PerformanceScore': 'Performance Score'
    },
    hover_data=['Department', 'PerformanceScore']
)
fig_color_size.show()

# %%
# 5. FACETED SCATTER PLOTS
# ------------------------------------------------------------
# Sometimes it's helpful to view separate scatter plots for each
# category (e.g., each Department). We can use facet_col or facet_row
# to split the scatter plot by a categorical column.
fig_facet = px.scatter(
    df,
    x='Age',
    y='Salary',
    color='Department',
    facet_col='Department',
    facet_col_wrap=1,  # Places each facet on a separate row
    title='Faceted Scatter Plots by Department'
)
# Adjust the layout for readability
fig_facet.update_layout(
    height=800
)
fig_facet.show()

# %%
# 6. SCATTER PLOT WITH MULTIPLE DIMENSIONS
# ------------------------------------------------------------
# We can also visualize data in 3D. Let's create a 3D scatter plot
# to explore Age, Salary, and PerformanceScore. We'll color points
# by Department.
fig_3d = px.scatter_3d(
    df,
    x='Age',
    y='Salary',
    z='PerformanceScore',
    color='Department',
    title='3D Scatter Plot: Age, Salary, and Performance Score'
)
fig_3d.show()

# %%
# 7. ADVANCED LAYOUT CUSTOMIZATION
# ------------------------------------------------------------
# We'll customize the layout of our 2D scatter plot to demonstrate
# how to modify titles, legends, axes, and more using Plotly.
fig_custom_layout = px.scatter(
    df,
    x='Age',
    y='Salary',
    color='Department',
    size='PerformanceScore',
    title='Advanced Layout Customization: Age vs. Salary'
)

# Update various layout elements
fig_custom_layout.update_layout(
    title=dict(
        text='Age vs. Salary (Customized Layout)',
        x=0.5,  # Center the chart title
        xanchor='center'
    ),
    xaxis_title='Employee Age (Years)',
    yaxis_title='Salary (USD per Year)',
    legend_title_text='Department Legend',
    font=dict(
        family='Arial, Helvetica, sans-serif',
        size=14,
        color='black'
    )
)

fig_custom_layout.show()

# %%
# 8. SUBPLOTS WITH MULTIPLE SCATTER PLOTS
# ------------------------------------------------------------
# Using plotly.graph_objects and plotly.subplots, we can create
# multiple scatter plots in one figure for side-by-side comparisons.
from plotly.subplots import make_subplots

fig_subplots = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Department: IT", "Department: HR")
)

# Filter data for IT and HR
df_it = df[df['Department'] == 'IT']
df_hr = df[df['Department'] == 'HR']

# Scatter for IT in subplot(1,1)
fig_subplots.add_trace(
    go.Scatter(
        x=df_it['Age'],
        y=df_it['Salary'],
        mode='markers',
        marker=dict(
            size=df_it['PerformanceScore'] * 3,  # Scale marker size
            color='blue',
            opacity=0.7
        ),
        name='IT'
    ),
    row=1, col=1
)

# Scatter for HR in subplot(1,2)
fig_subplots.add_trace(
    go.Scatter(
        x=df_hr['Age'],
        y=df_hr['Salary'],
        mode='markers',
        marker=dict(
            size=df_hr['PerformanceScore'] * 3,
            color='green',
            opacity=0.7
        ),
        name='HR'
    ),
    row=1, col=2
)

# Update layout and titles
fig_subplots.update_layout(
    title='Subplots: Comparing IT vs. HR',
    showlegend=True,
    height=600
)

# Adjust axis labels for each subplot
fig_subplots.update_xaxes(title_text='Age (Years)', row=1, col=1)
fig_subplots.update_yaxes(title_text='Salary (USD)', row=1, col=1)
fig_subplots.update_xaxes(title_text='Age (Years)', row=1, col=2)
fig_subplots.update_yaxes(title_text='Salary (USD)', row=1, col=2)

fig_subplots.show()

# %%
# 9. PUTTING IT ALL TOGETHER
# ------------------------------------------------------------
# The above code blocks demonstrate various ways to create,
# customize, and extend scatter plots with Plotly. In a real
# YouTube tutorial, you would walk through each section:
#  - Explaining how the data is generated or loaded
#  - Demonstrating basic vs. advanced plots
#  - Highlighting the power of color, size, facet, and 3D
#  - Showing how to create subplots for side-by-side comparisons
#  - Finishing with advanced layout tweaks for a professional look
# %%
