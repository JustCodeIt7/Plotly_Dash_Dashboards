#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plotly Table Chart Tutorial Script
----------------------------------
A comprehensive guide to creating and styling table visualizations with Plotly.
This script demonstrates creating tables from basic to advanced examples.
"""
#%%

import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

print("=" * 50)
print("PLOTLY TABLE TUTORIAL SCRIPT")
print("=" * 50)
#%%
# ------------------------------------
# EXAMPLE 1: CREATING A BASIC TABLE
# ------------------------------------
print("\nDisplaying Example 1: Basic Product Table")

# Create sample data for the first table
data_ex1 = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit'],
    'Price_USD': [1.20, 0.75, 2.50, 3.00],
    'Stock_kg': [150, 200, 80, 120]
}
df_ex1 = pd.DataFrame(data_ex1)
#%%
# Create a basic table
fig1 = go.Figure(data=[go.Table(
    header=dict(
        values=list(df_ex1.columns),  # Headers from DataFrame columns
        fill_color='paleturquoise',    # Light blue header background
        align='center',                # Center-align header text
        font=dict(color='black', size=12) # Header font style
    ),
    cells=dict(
        values=[df_ex1[col] for col in df_ex1.columns], # Cell values from DataFrame
        fill_color='lavender',        # Light purple cell background
        align='left',                 # Left-align cell text
        font=dict(color='darkslategray', size=11) # Cell font style
    )
)])

fig1.update_layout(
    title_text="Example 1: Basic Product Table",
    title_x=0.5 # Center title
)
fig1.show()
print("Example 1 (Basic Table) displayed.")
#%%
# ------------------------------------
# EXAMPLE 2: STYLED TABLE
# ------------------------------------
print("\nDisplaying Example 2: Styled Inventory Table")

# Sample data for a more styled table
data_ex2 = {
    "Item": ["Keyboard", "Mouse", "Monitor", "Webcam", "Desk Lamp"],
    "Brand": ["Logitech", "Razer", "Dell", "Logitech", "Philips"],
    "Price": [75, 50, 300, 60, 25],
    "Units_Sold": [120, 150, 45, 90, 70],
    "Rating": [4.6, 4.3, 4.7, 4.1, 4.5]
}
df_ex2 = pd.DataFrame(data_ex2)
#%%
# Create a styled table
fig2 = go.Figure(data=[go.Table(
    header=dict(
        values=[f"<b>{col}</b>" for col in df_ex2.columns], # Bold header text
        line_color='darkslategray', # Line color for header
        fill_color='royalblue',     # Royal blue header background
        align='center',
        font=dict(color='white', size=13) # White header font
    ),
    cells=dict(
        values=[df_ex2[col] for col in df_ex2.columns],
        line_color='darkslategray', # Line color for cells
        # Alternating row colors for better readability
        fill_color=[['lightcyan', 'white'] * (len(df_ex2) // 2 + 1)],
        align=['left', 'left', 'right', 'center', 'center'], # Custom alignment per column
        font=dict(color='darkslategray', size=12),
        height=30 # Set cell height
    )
)])

fig2.update_layout(
    title_text="Example 2: Styled Inventory Table with Alternating Row Colors",
    title_x=0.5,
    width=700, # Adjust table width
    height=450 # Adjust table height
)
fig2.show()
print("Example 2 (Styled Table) displayed.")
#%%
# -------------------------------------------------
# EXAMPLE 3: TABLE WITH CONDITIONAL CELL FORMATTING
# -------------------------------------------------
print("\nDisplaying Example 3: Table with Conditional Formatting")

# Data for conditional formatting example
data_ex3 = {
    'Student_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Math_Score': [85, 92, 78, 65, 95, 88],
    'Science_Score': [90, 88, 72, 60, 98, 85],
    'Attendance_Pct': [95, 98, 85, 70, 100, 92]
}
df_ex3 = pd.DataFrame(data_ex3)
#%%
# Define colors for conditional formatting
def get_score_colors(scores_series):
    colors = []
    for score in scores_series:
        if score >= 90:
            colors.append('lightgreen')
        elif score >= 80:
            colors.append('lightyellow')
        elif score >= 70:
            colors.append('lightcoral')
        else:
            colors.append('pink')
    return colors

math_score_colors = get_score_colors(df_ex3['Math_Score'])
science_score_colors = get_score_colors(df_ex3['Science_Score'])
attendance_colors = ['lightgreen' if att >= 90 else 'lightyellow' if att >= 80 else 'lightcoral' for att in df_ex3['Attendance_Pct']]

fig3 = go.Figure(data=[go.Table(
    header=dict(
        values=[f"<b>{col.replace('_', ' ')}</b>" for col in df_ex3.columns],
        fill_color='darkslateblue',
        align='center',
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[df_ex3[col] for col in df_ex3.columns],
        fill_color=[ # Apply conditional colors to specific columns
            ['white'] * len(df_ex3), # Student_ID
            ['white'] * len(df_ex3), # Name
            math_score_colors,       # Math_Score
            science_score_colors,    # Science_Score
            attendance_colors        # Attendance_Pct
        ],
        align=['center', 'left', 'center', 'center', 'center'],
        font=dict(color='black', size=11),
        height=28
    )
)])

fig3.update_layout(
    title_text="Example 3: Student Performance with Conditional Formatting",
    title_x=0.5,
    width=800
)
fig3.show()
print("Example 3 (Conditional Formatting) displayed.")
#%%

# -------------------------------------------------
# EXAMPLE 4: ADVANCED TABLE WITH TOTALS (NO CONDITIONAL FORMATTING)
# -------------------------------------------------
print("\nDisplaying Example 4: Advanced Sales Table with Totals")

# Generate more complex sales data
np.random.seed(101) # For consistent random data
regions = ['North', 'South', 'East', 'West']
products = ['Product A', 'Product B', 'Product C']
sales_data_ex4 = pd.DataFrame(
    np.random.randint(1000, 5000, size=(len(regions), len(products))),
    columns=products,
    index=regions
)

# Calculate totals
sales_data_ex4_totals = sales_data_ex4.copy()
sales_data_ex4_totals['Region_Total'] = sales_data_ex4_totals.sum(axis=1)
sales_data_ex4_totals.loc['Product_Total'] = sales_data_ex4_totals.sum()

# Prepare cell values for the table
cell_values = [sales_data_ex4_totals.index.tolist()] + \
              [sales_data_ex4_totals[col].tolist() for col in sales_data_ex4_totals.columns]

# Simple uniform styling (no conditional formatting)
cell_fill_colors = [['lightgray'] * len(sales_data_ex4_totals)] # Index column

for j, col_name in enumerate(sales_data_ex4_totals.columns):
    col_colors = []
    for i, val in enumerate(sales_data_ex4_totals[col_name]):
        if sales_data_ex4_totals.index[i] == 'Product_Total' or col_name == 'Region_Total':
            col_colors.append('lightskyblue') # Color for total cells
        else:
            col_colors.append('white') # Standard white for data cells
    cell_fill_colors.append(col_colors)

fig4 = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Region/Product</b>'] + [f"<b>{col}</b>" for col in sales_data_ex4_totals.columns],
        fill_color='darkgreen',
        align='center',
        font=dict(color='white', size=12),
        line_color='gray'
    ),
    cells=dict(
        values=cell_values,
        fill_color=cell_fill_colors,
        align=['left'] + ['right'] * len(sales_data_ex4_totals.columns), # Right align numbers
        font=dict(
            color= [['black'] * len(sales_data_ex4_totals.index) if c_idx == 0 else # Black for first column
                    ['navy' if sales_data_ex4_totals.index[r_idx] == 'Product_Total' or sales_data_ex4_totals.columns[c_idx-1] == 'Region_Total' else 'black'
                     for r_idx in range(len(sales_data_ex4_totals.index))]
                    for c_idx in range(len(sales_data_ex4_totals.columns) + 1) ],
            size=11
        ),
        height=30,
        format=[None] + [',.0f'] * len(sales_data_ex4_totals.columns) # Format numbers with commas
    )
)])

fig4.update_layout(
    title_text="Example 4: Advanced Sales Table with Totals (No Conditional Formatting)",
    title_x=0.5,
    width=900,
    height=500
)
fig4.show()
print("Example 4 (Advanced Table with Totals Only) displayed.")

# %%
