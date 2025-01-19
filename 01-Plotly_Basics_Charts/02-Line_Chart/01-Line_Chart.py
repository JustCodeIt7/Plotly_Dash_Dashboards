# %% [markdown]
"""
# PLOTLY LINE CHARTS
"""

# %%
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from rich import print

# %% [markdown]
"""
# 2. CREATE A SAMPLE DATASET
"""
# %%
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
categories = ["Electronics", "Furniture", "Clothing"]

# Create a DataFrame with random (but reasonable) sales values
np.random.seed(42)  # For reproducibility
data = {
    "Month": months * len(categories),
    "Category": sorted(categories * len(months)),
    "Sales": np.random.randint(200, 1000, size=len(months) * len(categories)),
}
df = pd.DataFrame(data)
print(df.head(14))

# %% [markdown]
"""# 3. BASIC LINE CHART"""

# %%
df_monthly = df.groupby("Month", as_index=False)["Sales"].sum()

fig_basic = px.line(df_monthly, x="Month", y="Sales", title="Basic Line Chart: Total Monthly Sales")

fig_basic.show()

# %% [markdown]
"""# 4. MULTIPLE LINES (COLOR BY CATEGORY)"""

# %%
fig_multiple = px.line(
    df, x="Month", y="Sales", color="Category", title="Multiple Lines: Monthly Sales by Category"
)
fig_multiple.show()

# %% [markdown]
"""# 5. ADDING MARKERS AND CUSTOMIZING LINES"""

# %%
fig_custom_lines = px.line(
    df, x="Month", y="Sales", color="Category", title="Custom Line Styles with Markers"
)

# Update traces to add markers and customize line styles
fig_custom_lines.update_traces(
    mode="lines+markers",  # lines+markers shows line and data points
    line=dict(width=2, dash="solid"),
)  # dash could be 'dash', 'dot', 'solid', etc.

fig_custom_lines.show()

# %% [markdown]
"""# 6. SUBPLOTS WITH MULTIPLE LINE CHARTS"""

# %%
from plotly.subplots import make_subplots

fig_subplots = make_subplots(
    rows=1, cols=2, subplot_titles=("Electronics Sales", "Furniture Sales")
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
        line=dict(width=2, color="blue"),
    ),
    row=1,
    col=1,
)

# Create a line chart for Furniture in subplot (1,2)
fig_subplots.add_trace(
    go.Scatter(
        x=df_furniture["Month"],
        y=df_furniture["Sales"],
        mode="lines+markers",
        name="Furniture",
        line=dict(width=2, color="green"),
    ),
    row=1,
    col=2,
)

fig_subplots.update_layout(title="Subplots: Electronics vs. Furniture Sales", showlegend=False)
fig_subplots.show()
