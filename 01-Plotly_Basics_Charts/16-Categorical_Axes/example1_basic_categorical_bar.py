"""
Example 1: Basic Categorical Bar Chart with Custom Ordering
===========================================================

This example demonstrates:
- Creating a simple bar chart with categorical x-axis
- Using category_orders to control the display order
- Basic categorical axis styling

Perfect for beginners learning about categorical axes in Plotly!
"""

import plotly.express as px
import plotly.graph_objects as go

# Create sample data for a coffee shop's daily sales
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
coffee_sales = [120, 95, 110, 130, 180, 220, 150]

print("=== Example 1: Basic Categorical Bar Chart ===")
print("Creating a coffee shop sales chart with custom day ordering...")

# Method 1: Using Plotly Express with category_orders
fig1 = px.bar(
    x=days, 
    y=coffee_sales,
    title="Coffee Shop Daily Sales - Method 1 (Plotly Express)",
    labels={'x': 'Day of Week', 'y': 'Coffee Sales ($)'},
    # Control the order of days (instead of alphabetical)
    category_orders={'x': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
)

# Customize the appearance
fig1.update_traces(marker_color='brown')
fig1.update_layout(
    showlegend=False,
    font=dict(size=12),
    plot_bgcolor='white'
)

# Show the first chart
fig1.show()

print("\n" + "="*50)

# Method 2: Using Graph Objects with categoryorder
fig2 = go.Figure(data=go.Bar(
    x=days,
    y=coffee_sales,
    marker_color='darkgreen'
))

fig2.update_layout(
    title="Coffee Shop Daily Sales - Method 2 (Graph Objects)",
    xaxis_title="Day of Week",
    yaxis_title="Coffee Sales ($)",
    # Force categorical axis and set custom order
    xaxis=dict(
        type='category',
        categoryorder='array',
        categoryarray=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ),
    font=dict(size=12),
    plot_bgcolor='white'
)

# Show the second chart
fig2.show()

print("Key Learning Points:")
print("1. Use 'category_orders' in Plotly Express to control category sequence")
print("2. Use 'categoryorder' and 'categoryarray' in Graph Objects for custom ordering")
print("3. Categorical axes prevent Plotly from treating text as continuous data")
print("4. Both methods give you full control over how categories appear")