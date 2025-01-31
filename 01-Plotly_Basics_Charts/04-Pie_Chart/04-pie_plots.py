# %% [markdown]
"""
# Pie Chart in Plotly

This tutorial demonstrates three different approaches to creating pie charts using Plotly:
1. A basic interactive pie chart using Plotly Express
2. A customized donut chart using Plotly Graph Objects
3. Comparative pie charts using subplots

Each example builds upon the previous one, introducing new concepts and customization options.
"""

# %%
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# %%
# Generate sample market data
np.random.seed(42)  # For reproducibility

companies = ["Apple", "Samsung", "Google", "Huawei", "Others"]
market_share = np.random.dirichlet(np.ones(5)) * 100
revenue = np.random.uniform(10000, 50000, 5)
growth = np.random.uniform(-10, 30, 5)

df = pd.DataFrame(
    {"company": companies, "market_share": market_share, "revenue": revenue, "growth": growth}
)

# %% [markdown]
"""
## Example 1: Basic Interactive Pie Chart

This example demonstrates the fundamentals of creating a pie chart using Plotly Express (px).
Key features:
- Uses the high-level Plotly Express API for quick and easy plotting
- Includes hover data with multiple variables (revenue and growth)
- Custom labels for better readability
- Interactive features like hover tooltips
- Custom color scheme using qualitative colors
- Percentage and label display inside the segments

Key customizations:
- Text positioning inside segments
- Hover template with formatted values
- Centered title with custom font size
- No legend (as labels are inside segments)
"""

# %%
# Create basic interactive pie chart
fig = px.pie(
    df,
    values="market_share",
    names="company",
    title="Global Market Share Distribution",
    hover_data=["revenue", "growth"],
    labels={
        "revenue": "Revenue (M$)",
        "growth": "YoY Growth (%)",
        "market_share": "Market Share (%)",
    },
    color_discrete_sequence=px.colors.qualitative.Set3,
)

# Customize the appearance
fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    hovertemplate="<b>%{label}</b><br>"
    + "Market Share: %{value:.1f}%<br>"
    + "Revenue: $%{customdata[0]:.0f}M<br>"
    + "Growth: %{customdata[1]:.1f}%<extra></extra>",
)

fig.update_layout(title_x=0.5, title_font_size=20, showlegend=False, width=800, height=600)

fig.show()

# %% [markdown]
"""
## Example 2: Custom Donut Chart

This example shows how to create a more sophisticated donut chart using Plotly Graph Objects (go).
Key features:
- Uses the lower-level Graph Objects API for more detailed control
- Converts pie chart to donut chart using the 'hole' parameter
- Pulls out segments with large market share (>30%)
- Custom marker styling with white borders
- Central text annotation
- Horizontal legend placement

Advanced customizations:
- Donut hole size of 60%
- Outside text positioning
- Conditional segment pulling
- Custom marker colors and border styling
- Centered annotations in the donut hole
- Horizontal legend at the top
"""

# %%
# Create custom donut chart
fig = go.Figure()
fig.add_trace(
    go.Pie(
        labels=df["company"],
        values=df["market_share"],
        hole=0.6,  # Creates donut chart
        textinfo="label+percent",
        textposition="outside",
        pull=[0.1 if x > 30 else 0 for x in df["market_share"]],  # Pull out larger segments
        marker=dict(colors=px.colors.qualitative.Bold, line=dict(color="#ffffff", width=2)),
    )
)

# Add central text and customize layout
fig.update_layout(
    title="Market Distribution<br>(with market leaders highlighted)",
    title_x=0.5,
    width=800,
    height=600,
    annotations=[dict(text="2024<br>Market<br>Share", x=0.5, y=0.5, font_size=20, showarrow=False)],
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)

fig.show()

# %% [markdown]
"""
## Example 3: Comparative Pie Charts

This example demonstrates how to create side-by-side pie charts for comparison using subplots.
Key features:
- Creates two pie charts side by side using make_subplots
- Compares market share data between two years
- Consistent styling across both charts
- Shared legend for both charts
- Custom annotations for each chart

Advanced techniques:
- Using subplot specifications with 'domain' type
- Consistent color schemes across charts
- Donut style with 40% hole
- Centered text labels
- Custom positioning of titles and annotations
- Horizontal legend centered at the top
- Wider layout for better comparison

Note: The data for 2024 is randomly generated with a different seed to show variation.
"""

# %%
# Generate new data for comparison
df1 = df.copy()  # Use existing data for 2023
np.random.seed(43)  # Different seed for 2024 data
market_share_2024 = np.random.dirichlet(np.ones(5)) * 100
df2 = df.copy()
df2["market_share"] = market_share_2024

# Create subplots
fig = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "domain"}, {"type": "domain"}]],
    subplot_titles=("2023 Market Share", "2024 Market Share"),
)

# Add first pie chart (2023)
fig.add_trace(
    go.Pie(
        labels=df1["company"],
        values=df1["market_share"],
        name="2023",
        marker_colors=px.colors.qualitative.Set1,
        domain={"column": 0},
    ),
    1,
    1,
)

# Add second pie chart (2024)
fig.add_trace(
    go.Pie(
        labels=df2["company"],
        values=df2["market_share"],
        name="2024",
        marker_colors=px.colors.qualitative.Set1,
        domain={"column": 1},
    ),
    1,
    2,
)

# Update traces and layout
fig.update_traces(hole=0.4, textposition="inside", textinfo="percent+label")

fig.update_layout(
    title_text="Market Share Comparison: 2023 vs 2024",
    title_x=0.5,
    width=1200,
    height=600,
    annotations=[
        dict(text="2023", x=0.18, y=0.5, font_size=20, showarrow=False),
        dict(text="2024", x=0.82, y=0.5, font_size=20, showarrow=False),
    ],
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
)

fig.show()

# %%
import plotly.express as px
import plotly.graph_objects as go

# Sample data for demonstration
regions = ["North", "South", "East", "West"]
sales = [25, 30, 18, 27]

# Create a pie chart using Plotly Express (px)
fig_px = px.pie(
    values=sales,
    names=regions,
    title="Sales Distribution by Region (Plotly Express)",
    labels={"values": "Sales", "names": "Region"},
)

# Customize the hover information and text position
fig_px.update_traces(textposition="inside", textinfo="percent+label")
fig_px.show()

# %%
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Sample data
categories = ["A", "B", "C", "D"]
values = [30, 20, 25, 25]

# Plotly Express version
fig1 = px.pie(
    values=values,
    names=categories,
    title="Plotly Express Pie Chart",
    color_discrete_sequence=px.colors.qualitative.Set3,
)

# Plotly Graph Objects version
fig2 = go.Figure(
    data=[
        go.Pie(
            labels=categories,
            values=values,
            hole=0.3,
            marker=dict(colors=px.colors.qualitative.Set3),
            textinfo="label+percent",
            hoverinfo="label+value",
            showlegend=True,
        )
    ]
)
fig2.update_layout(title="Plotly Graph Objects Pie Chart")

# Create subplots to show both charts
fig3 = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=("Plotly Express", "Plotly Graph Objects"),
    specs=[[{"type": "pie"}, {"type": "pie"}]],
)

# Add traces to subplots
fig3.add_trace(go.Pie(labels=categories, values=values), row=1, col=1)
fig3.add_trace(go.Pie(labels=categories, values=values, hole=0.3), row=1, col=2)

# Update layout
fig3.update_layout(title_text="Comparison: Plotly Express vs Graph Objects")

# Show all figures
fig1.show()
fig2.show()
fig3.show()

# %%
