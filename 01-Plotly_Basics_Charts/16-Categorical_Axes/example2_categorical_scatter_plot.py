"""
Example 2: Scatter Plot with Categorical Axis (Dot Plot)
========================================================

This example demonstrates:
- Creating a scatter plot with categorical y-axis
- Using colors and symbols to distinguish categories
- Understanding dot plots vs regular scatter plots

Perfect for comparing values across different categories!
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

print("=== Example 2: Categorical Scatter Plot (Dot Plot) ===")
print("Creating a sports performance comparison chart...")

# Create sample data for different sports and their average scores
sports_data = {
    'sport': ['Basketball', 'Soccer', 'Tennis', 'Swimming', 'Running', 'Baseball'],
    'average_score': [85, 78, 92, 88, 80, 75],
    'difficulty': ['High', 'Medium', 'High', 'Medium', 'Low', 'Medium']
}

df = pd.DataFrame(sports_data)

# Method 1: Simple categorical scatter plot
fig1 = px.scatter(
    df, 
    x='average_score', 
    y='sport',
    title="Sports Performance Scores - Simple Dot Plot",
    labels={'average_score': 'Average Performance Score', 'sport': 'Sport'},
    color='difficulty',
    size_max=15
)

# Make markers larger and more visible
fig1.update_traces(marker=dict(size=12))
fig1.update_layout(
    font=dict(size=12),
    plot_bgcolor='white',
    height=400
)

# Show the first chart
fig1.show()

print("\n" + "="*50)

# Method 2: Enhanced version with custom styling
fig2 = go.Figure()

# Add data points with custom styling
colors = {'High': 'red', 'Medium': 'orange', 'Low': 'green'}
symbols = {'High': 'diamond', 'Medium': 'circle', 'Low': 'square'}

for difficulty in df['difficulty'].unique():
    filtered_df = df[df['difficulty'] == difficulty]
    fig2.add_trace(go.Scatter(
        x=filtered_df['average_score'],
        y=filtered_df['sport'],
        mode='markers',
        marker=dict(
            size=15,
            color=colors[difficulty],
            symbol=symbols[difficulty],
            line=dict(width=2, color='black')
        ),
        name=f'{difficulty} Difficulty',
        text=filtered_df['average_score'],
        textposition='middle right'
    ))

fig2.update_layout(
    title="Sports Performance Scores - Enhanced Dot Plot",
    xaxis_title="Average Performance Score",
    yaxis_title="Sport",
    font=dict(size=12),
    plot_bgcolor='white',
    height=400,
    # Force categorical y-axis
    yaxis=dict(type='category')
)

# Show the second chart
fig2.show()

print("\n" + "="*50)

# Method 3: Horizontal comparison (multiple values per category)
print("Bonus: Multiple values per category...")

# Extended data with multiple measurements per sport
extended_data = {
    'sport': ['Basketball'] * 3 + ['Soccer'] * 3 + ['Tennis'] * 3,
    'score': [85, 88, 82, 78, 76, 80, 92, 90, 94],
    'measurement': ['Game 1', 'Game 2', 'Game 3'] * 3
}

df_extended = pd.DataFrame(extended_data)

fig3 = px.scatter(
    df_extended,
    x='score',
    y='sport',
    color='measurement',
    title="Multiple Measurements per Sport",
    labels={'score': 'Performance Score', 'sport': 'Sport'}
)

fig3.update_traces(marker=dict(size=10))
fig3.update_layout(
    font=dict(size=12),
    plot_bgcolor='white',
    height=300
)

fig3.show()

print("Key Learning Points:")
print("1. Categorical scatter plots are great for comparing values across categories")
print("2. They're often called 'dot plots' when one axis is categorical")
print("3. Use colors and symbols to add extra dimensions to your data")
print("4. Perfect for showing distributions or comparisons within categories")