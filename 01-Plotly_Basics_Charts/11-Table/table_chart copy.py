#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plotly Table Chart Tutorial
---------------------------
A comprehensive guide to creating and styling table visualizations with Plotly
"""

import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

print("=" * 50)
print("PLOTLY TABLE CHART TUTORIAL")
print("=" * 50)

# ------------------------------
# PART 1: CREATING A BASIC TABLE
# ------------------------------
print("\n1. Creating a Basic Table")

# Create sample data for our table
data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Desktop', 'Smartwatch'],
    'Price': [1200, 800, 500, 1500, 300],
    'Stock': [25, 50, 35, 10, 45],
    'Rating': [4.5, 4.2, 4.0, 4.8, 3.9]
}

# Convert to DataFrame
df = pd.DataFrame(data)
print("\nSample Data:")
print(df)

# Create a basic table
fig1 = go.Figure(data=[go.Table(
    header=dict(
        values=list(df.columns),
        fill_color='paleturquoise',
        align='center'
    ),
    cells=dict(
        values=[df[col] for col in df.columns],
        fill_color='lavender',
        align='center'
    )
)])

fig1.update_layout(title="Basic Plotly Table")
fig1.show()

print("\nA basic table has been created with a simple header and cell styling.")

# ------------------------------
# PART 2: STYLING THE TABLE
# ------------------------------
print("\n2. Styling the Table")

# Create a more advanced styled table
fig2 = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Product</b>', '<b>Price ($)</b>', '<b>Stock</b>', '<b>Rating</b>'], # Use <b> tags for bold text
        line_color='darkslategray',
        fill_color='royalblue',
        align='center',
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[df[col] for col in df.columns],
        line_color='darkslategray',
        fill_color=[['white', 'lightgrey'] * len(df)],  # alternating row colors
        align=['left', 'center', 'center', 'center'],
        font=dict(color='darkslategray', size=11),
        height=25
    )
)])

fig2.update_layout(
    title_text="Styled Product Inventory Table",
    title_font=dict(size=20),
    width=700,
    height=400
)

fig2.show()

print("\nThe table has been styled with:")
print("- Custom header formatting and colors")
print("- Alternating row colors")
print("- Custom alignment for different columns")
print("- Adjusted font sizes and colors")

# ------------------------------
# PART 3: CONDITIONAL FORMATTING
# ------------------------------
print("\n3. Conditional Formatting")

# Create a table with conditional formatting
# Let's add color scales based on values
stock_colors = ['red' if val < 30 else 'orange' if val < 40 else 'green' for val in df['Stock']]
rating_colors = ['red' if val < 4.0 else 'orange' if val < 4.5 else 'green' for val in df['Rating']]

fig3 = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Product</b>', '<b>Price ($)</b>', '<b>Stock</b>', '<b>Rating</b>'],
        line_color='darkslategray',
        fill_color='grey',
        align='center',
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[df[col] for col in df.columns],
        line_color='darkslategray',
        fill_color=[['white'] * len(df), ['white'] * len(df), 
                   stock_colors, rating_colors],  # Apply colors to stock and rating columns
        align=['left', 'center', 'center', 'center'],
        font=dict(color='darkslategray', size=11),
        height=25
    )
)])

fig3.update_layout(
    title_text="Product Table with Conditional Formatting",
    title_font=dict(size=20),
    width=700,
    height=400
)

fig3.show()

print("\nConditional formatting has been applied:")
print("- Stock levels are color-coded (red < 30, orange < 40, green >= 40)")
print("- Ratings are color-coded (red < 4.0, orange < 4.5, green >= 4.5)")

# ------------------------------
# PART 4: INTERACTIVE HEATMAP TABLE
# ------------------------------
print("\n4. Interactive Heatmap Table")

# Create a larger dataset for a heatmap-style table
# Let's create sales data by region and quarter
regions = ['North', 'South', 'East', 'West', 'Central']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Generate random sales data
sales_data = pd.DataFrame(
    np.random.randint(50, 200, size=(len(regions), len(quarters))),
    columns=quarters,
    index=regions
)

print("\nSales Data by Region and Quarter:")
print(sales_data)

# Create a heatmap table
fig4 = go.Figure(data=[go.Table(
    header=dict(
        values=['Region'] + list(sales_data.columns),
        fill_color='midnightblue',
        align='center',
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[sales_data.index] + [sales_data[col] for col in sales_data.columns],
        # Apply heatmap colors: Calculate RGB values based on sales data.
        # Higher sales -> lower R & G values -> darker blue.
        fill_color=[[f'rgb({255-val}, {255-val}, 255)' for val in sales_data[col]]
                   for col in sales_data.columns],
        align=['left'] + ['center'] * len(sales_data.columns),
        font=dict(color='black', size=11),
        height=25,
        format=[None] + [', .0f'] * len(sales_data.columns)
    )
)])

fig4.update_layout(
    title_text="Sales Heatmap Table by Region and Quarter",
    title_font=dict(size=20),
    width=700,
    height=400
)

fig4.show()

print("\nCreated a heatmap-style table:")
print("- Sales data by region and quarter")
print("- Color intensity corresponds to sales value")
print("- The higher the sales, the darker the blue color")

# ------------------------------
# PART 5: ADDING CALCULATIONS AND TOTALS
# ------------------------------
print("\n5. Adding Calculations and Totals")

# Add a total row and column to our sales data
sales_data_with_totals = sales_data.copy()
sales_data_with_totals['Total'] = sales_data_with_totals.sum(axis=1)
sales_data_with_totals.loc['Total'] = sales_data_with_totals.sum()

print("\nSales Data with Totals:")
print(sales_data_with_totals)

# Create a table with totals
fig5 = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Region</b>'] + [f'<b>{col}</b>' for col in sales_data_with_totals.columns],
        fill_color='royalblue',
        align='center',
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[sales_data_with_totals.index] + 
               [sales_data_with_totals[col] for col in sales_data_with_totals.columns],
        fill_color=[
            ['lightgrey' if i == len(sales_data_with_totals)-1 else 'white' 
             for i in range(len(sales_data_with_totals))],
            *[['lightgrey' if i == len(sales_data_with_totals)-1 else 
               ('lightblue' if j == len(sales_data_with_totals.columns)-1 else 'white') 
               for i in range(len(sales_data_with_totals))] 
              for j in range(len(sales_data_with_totals.columns))]
        ],
        align=['left'] + ['center'] * len(sales_data_with_totals.columns),
        font=dict(
            color=[
                ['black' if i < len(sales_data_with_totals)-1 else 'darkblue' 
                 for i in range(len(sales_data_with_totals))],
                *[['darkblue' if i == len(sales_data_with_totals)-1 or j == len(sales_data_with_totals.columns)-1 
                   else 'black' for i in range(len(sales_data_with_totals))] 
                  for j in range(len(sales_data_with_totals.columns))]
            ],
            size=11
        ),
        height=25,
        format=[None] + [', .0f'] * len(sales_data_with_totals.columns)
    )
)])

fig5.update_layout(
    title_text="Sales Table with Totals",
    title_font=dict(size=20),
    width=800,
    height=400
)

fig5.show()

print("\nCreated a table with totals:")
print("- Calculated row totals (total sales by region)")
print("- Calculated column totals (total sales by quarter)")
print("- Highlighted totals with different colors and formatting")

# ------------------------------
# PART 6: SAVING AND EXPORTING
# ------------------------------
print("\n6. Saving and Exporting Tables")

# Save our table as HTML
fig5.write_html("sales_table.html")
print("\nTable saved as HTML: sales_table.html")

# Save our table as an image
fig5.write_image("sales_table.png")
print("Table saved as PNG: sales_table.png")

print("\n" + "=" * 50)
print("TUTORIAL COMPLETE")
print("=" * 50)
print("\nKey Points:")
print("1. Tables are created using go.Table() in Plotly")
print("2. Headers and cells can be independently styled")
print("3. Conditional formatting enhances data visualization")
print("4. Tables can be combined with calculations and totals")
print("5. Plotly tables can be saved in various formats for sharing")
print("\nThis script demonstrates various approaches to creating")
print("and styling tables in Plotly - perfect for data presentation!")