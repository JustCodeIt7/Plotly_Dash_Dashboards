"""
Example 3: Multi-Category Axes Demonstration
============================================

This example demonstrates:
- Creating charts with multi-level categorical axes
- Understanding hierarchical categories
- Using nested groupings for better data organization

Great for showing data with natural hierarchical groupings!
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

print("=== Example 3: Multi-Category Axes ===")
print("Creating charts with hierarchical categorical groupings...")

# Example 1: Simple Multi-Category Bar Chart
print("1. Basic Multi-Category Bar Chart")

fig1 = go.Figure()

# Create multi-level categories: [Main Category, Sub Category]
fig1.add_trace(go.Bar(
    x=[['Q1', 'Q1', 'Q2', 'Q2', 'Q3', 'Q3', 'Q4', 'Q4'],
       ['Sales', 'Marketing', 'Sales', 'Marketing', 'Sales', 'Marketing', 'Sales', 'Marketing']],
    y=[20, 15, 25, 18, 30, 22, 35, 28],
    name="Revenue (in thousands)",
    marker_color='lightblue'
))

fig1.update_layout(
    title="Quarterly Department Performance",
    xaxis_title="Quarter / Department",
    yaxis_title="Revenue ($k)",
    font=dict(size=12),
    plot_bgcolor='white'
)

fig1.show()

print("\n" + "="*50)

# Example 2: Multi-Category with Multiple Series
print("2. Multi-Category with Multiple Data Series")

fig2 = go.Figure()

# Add first series (Current Year)
fig2.add_trace(go.Bar(
    x=[['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
       ['Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B']],
    y=[100, 85, 95, 78, 88, 92, 82, 75],
    name="2023 Sales",
    marker_color='steelblue'
))

# Add second series (Previous Year)
fig2.add_trace(go.Bar(
    x=[['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
       ['Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B']],
    y=[90, 80, 87, 75, 85, 88, 78, 72],
    name="2022 Sales",
    marker_color='lightcoral'
))

fig2.update_layout(
    title="Regional Store Performance Comparison",
    xaxis_title="Region / Store",
    yaxis_title="Sales (in thousands)",
    barmode='group',  # Place bars side by side
    font=dict(size=12),
    plot_bgcolor='white'
)

fig2.show()

print("\n" + "="*50)

# Example 3: Understanding the Structure
print("3. Understanding Multi-Category Structure")

# Create a simple example to show the concept
categories_main = ['Team A', 'Team A', 'Team B', 'Team B']
categories_sub = ['Morning', 'Evening', 'Morning', 'Evening']
values = [45, 38, 52, 41]

# Show what the data looks like
print("Data Structure:")
print("Main Categories:", categories_main)
print("Sub Categories: ", categories_sub)
print("Values:         ", values)

fig3 = go.Figure()

fig3.add_trace(go.Bar(
    x=[categories_main, categories_sub],
    y=values,
    marker_color=['gold', 'orange', 'lightgreen', 'green'],
    text=values,
    textposition='auto'
))

fig3.update_layout(
    title="Team Performance: Morning vs Evening Shifts",
    xaxis_title="Team / Shift Time",
    yaxis_title="Productivity Score",
    font=dict(size=12),
    plot_bgcolor='white',
    showlegend=False
)

fig3.show()

print("\n" + "="*50)

# Example 4: Practical Application - Website Analytics
print("4. Practical Example: Website Traffic Analytics")

# Simulate website analytics data
traffic_data = {
    'source': ['Social Media', 'Social Media', 'Search Engine', 'Search Engine', 
               'Direct', 'Direct', 'Email', 'Email'],
    'device': ['Mobile', 'Desktop', 'Mobile', 'Desktop', 
               'Mobile', 'Desktop', 'Mobile', 'Desktop'],
    'visitors': [1200, 800, 2100, 1500, 900, 650, 400, 350]
}

fig4 = go.Figure()

fig4.add_trace(go.Bar(
    x=[traffic_data['source'], traffic_data['device']],
    y=traffic_data['visitors'],
    marker_color='teal',
    text=traffic_data['visitors'],
    textposition='auto'
))

fig4.update_layout(
    title="Website Traffic by Source and Device Type",
    xaxis_title="Traffic Source / Device Type",
    yaxis_title="Number of Visitors",
    font=dict(size=12),
    plot_bgcolor='white'
)

fig4.show()

print("Key Learning Points:")
print("1. Multi-category axes help organize hierarchical data")
print("2. Use nested lists [main_category, sub_category] for x or y values")
print("3. Plotly automatically detects and creates multi-level axes")
print("4. Great for comparing data across multiple dimensions")
print("5. Perfect for business dashboards and analytical reports")