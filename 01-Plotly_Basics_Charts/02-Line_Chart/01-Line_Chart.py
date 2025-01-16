# %%
# PLOTLY LINE CHART TUTORIAL
# ---------------------------------------------------
# This script demonstrates how to create and customize line charts using
# Plotly in Python. Follow the comments to guide you through each step.

# 1. IMPORT LIBRARIES
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# %%
# 2. CREATE A SAMPLE DATASET
# In this example, we will simulate monthly sales data for three product categories over a year.
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
categories = ["Electronics", "Furniture", "Clothing"]

# Create a DataFrame with random (but reasonable) sales values
np.random.seed(42)  # For reproducibility
data = {
    "Month": months * len(categories),
    "Category": sorted(categories * len(months)),
    "Sales": np.random.randint(200, 1000, size=len(months) * len(categories))
}
df = pd.DataFrame(data)

# %%
# 3. BASIC LINE CHART
# A simple line chart showing sales over months (aggregate by month).
# First, we'll aggregate the data by month (summing across all categories).
df_monthly = df.groupby("Month", as_index=False)["Sales"].sum()

fig_basic = px.line(
    df_monthly,
    x="Month",
    y="Sales",
    title="Basic Line Chart: Total Monthly Sales"
)
fig_basic.show()

# %%
# 4. MULTIPLE LINES (COLOR BY CATEGORY)
# We can create a line chart that shows each category's performance across months.

fig_multiple = px.line(
    df,
    x="Month",
    y="Sales",
    color="Category",
    title="Multiple Lines: Monthly Sales by Category"
)
fig_multiple.show()

# %%
# 5. ADDING MARKERS AND CUSTOMIZING LINES
# We can add markers (data points) and change line styles/widths to enhance readability.

fig_custom_lines = px.line(
    df,
    x="Month",
    y="Sales",
    color="Category",
    title="Custom Line Styles with Markers"
)

# Update traces to add markers and customize line styles
fig_custom_lines.update_traces(mode="lines+markers",  # lines+markers shows line and data points
                               line=dict(width=2, dash="solid"))  # dash could be 'dash', 'dot', 'solid', etc.

fig_custom_lines.show()

# %%
# 6. SUBPLOTS WITH MULTIPLE LINE CHARTS
# For advanced layouts, we can use Plotly's make_subplots to display multiple line charts in one figure.

from plotly.subplots import make_subplots

fig_subplots = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Electronics Sales", "Furniture Sales")
)

# Filter data for Electronics and Furniture
df_electronics = df[df["Category"] == "Electronics"]
df_furniture = df[df["Category"] == "Furniture"]

# Create a line chart for Electronics in subplot (1,1)
fig_subplots.add_trace(
    go.Scatter(
        x=df_electronics["Month"],
        y=df_electronics["Sales"],
        mode="lines+markers",
        name="Electronics",
        line=dict(width=2, color="blue")
    ),
    row=1, col=1
)

# Create a line chart for Furniture in subplot (1,2)
fig_subplots.add_trace(
    go.Scatter(
        x=df_furniture["Month"],
        y=df_furniture["Sales"],
        mode="lines+markers",
        name="Furniture",
        line=dict(width=2, color="green")
    ),
    row=1, col=2
)

fig_subplots.update_layout(
    title="Subplots: Electronics vs. Furniture Sales",
    showlegend=False
)
fig_subplots.show()

# %%
# 7. ADVANCED LAYOUT CUSTOMIZATION
# We can adjust titles, fonts, legends, axes, and more to create professional-looking charts.

fig_advanced_layout = px.line(
    df,
    x="Month",
    y="Sales",
    color="Category",
    title="Advanced Layout Customization: Monthly Sales by Category"
)

# Update layout elements
fig_advanced_layout.update_layout(
    title=dict(
        text="Monthly Sales by Category (Customized Layout)",
        x=0.5,  # Center the title horizontally
        xanchor="center"
    ),
    xaxis_title="Month of the Year",
    yaxis_title="Sales (USD)",
    legend_title="Product Category",
    font=dict(
        family="Arial, Helvetica, sans-serif",
        size=14,
        color="black"
    )
)
fig_advanced_layout.show()