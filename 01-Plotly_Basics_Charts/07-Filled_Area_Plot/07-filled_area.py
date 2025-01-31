# %% [markdown]
"""
# Filled Area Plot

This example demonstrates how to create a filled area plot using Plotly.
Key features:
- Uses Plotly Graph Objects (go) for more control over the plot appearance
- Includes multiple traces with custom fill colors
- Customized axis labels and title
- Hover data with formatted values
- Custom legend with positioning
- Custom color scheme using qualitative colors
- Custom font size and style
"""
# %%
# Import required libraries
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from rich import print

# %%
# Generate sample data
np.random.seed(42)
x = np.arange(1, 10)
y1 = np.random.randint(1, 10, 9)
y2 = np.random.randint(1, 10, 9)
y3 = np.random.randint(1, 10, 9)

# Create a DataFrame
df = pd.DataFrame({"x": x, "y1": y1, "y2": y2, "y3": y3})
print(df)
# %%

# Create a filled area plot
fig = go.Figure()

# Add traces for each line
fig.add_trace(
    go.Scatter(
        x=df["x"], y=df["y1"], fill="tozeroy", mode="lines", name="Line 1", line_color="blue"
    )
)

fig.add_trace(
    go.Scatter(
        x=df["x"], y=df["y2"], fill="tozeroy", mode="lines", name="Line 2", line_color="green"
    )
)

fig.add_trace(
    go.Scatter(x=df["x"], y=df["y3"], fill="tozeroy", mode="lines", name="Line 3", line_color="red")
)

# Update the layout
fig.update_layout(
    title="Filled Area Plot",
    xaxis_title="X-axis",
    yaxis_title="Y-axis",
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
    font=dict(family="Courier New, monospace", size=12, color="RebeccaPurple"),
)

# Show the plot
fig.show()


# %%
# create a filled area plot using Plotly Express
fig = px.area(
    df,
    x="x",
    y=["y1", "y2", "y3"],
    title="Filled Area Plot",
    labels={"value": "Y-axis", "variable": "Line"},
    color_discrete_sequence=["blue", "green", "red"],
)

# Update the layout

fig.update_layout(
    title="Filled Area Plot",
    xaxis_title="X-axis",
    yaxis_title="Y-axis",
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
    font=dict(family="Courier New, monospace", size=12, color="RebeccaPurple"),
)

# Show the plot
fig.show()
# %%
