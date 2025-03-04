# %% [markdown]
"""
# Bubble Charts
"""
# %%
import plotly.express as px
import pandas as pd

# %% [markdown]
"""
## Simple Bubble Chart
"""
# %%
# Create a simple bubble chart
fig = px.scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], size=[40, 60, 80, 100])

fig.show()

# %% [markdown]
"""
## Setting Marker Size and Color
"""
# %%
# Create a DataFrame for better control
df = pd.DataFrame(
    {
        "x": [1, 2, 3, 4],
        "y": [10, 11, 12, 13],
        "size": [40, 60, 80, 100],
        "color": [
            "rgb(93, 164, 214)",
            "rgb(255, 144, 14)",
            "rgb(44, 160, 101)",
            "rgb(255, 65, 54)",
        ],
        "opacity": [1, 0.8, 0.6, 0.4],
        "group": ["A", "B", "C", "D"],  # Adding a group column for color mapping
    }
)

# Create bubble chart with custom colors
fig = px.scatter(
    df,
    x="x",
    y="y",
    size="size",
    color="group",
    color_discrete_sequence=df["color"].tolist(),
)

# Update marker opacity
for i, opacity in enumerate(df["opacity"]):
    fig.data[0].marker.opacity = df["opacity"].tolist()

fig.show()

# %% [markdown]
"""
## Scaling the Size of Bubble Charts
"""

# %%
# Create a DataFrame
size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]
df = pd.DataFrame(
    {
        "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "y": [11, 12, 10, 11, 12, 11, 12, 13, 12, 11],
        "size": size,
    }
)

# Create bubble chart with scaled sizes
fig = px.scatter(
    df,
    x="x",
    y="y",
    size="size",
    size_max=40,  # Controls the maximum size of the markers
)

# To match the original sizemin parameter
fig.update_traces(marker=dict(sizemin=4))

fig.show()

# %% [markdown]
"""
## Hover Text with Bubble Charts
"""

# %%
# Create a DataFrame
df = pd.DataFrame(
    {
        "x": [1, 2, 3, 4],
        "y": [10, 11, 12, 13],
        "size": [40, 60, 80, 100],
        "text": ["A<br>size: 40", "B<br>size: 60", "C<br>size: 80", "D<br>size: 100"],
        "group": ["A", "B", "C", "D"],  # For color mapping
    }
)

# Create bubble chart with custom hover text
fig = px.scatter(
    df,
    x="x",
    y="y",
    size="size",
    text="text",
    color="group",
    color_discrete_sequence=[
        "rgb(93, 164, 214)",
        "rgb(255, 144, 14)",
        "rgb(44, 160, 101)",
        "rgb(255, 65, 54)",
    ],
)

# Set hover template to show the text
fig.update_traces(hovertemplate="%{text}")

fig.show()

# %%
# Bubble Chart with Colorscale
# Create a DataFrame
df = pd.DataFrame(
    {
        "x": [1, 2, 3, 4],
        "y": [10, 11, 12, 13],
        "size": [40, 60, 80, 100],
        "color_value": [10, 20, 30, 40],  # Color values for the colorscale
    }
)

# Create bubble chart with colorscale
fig = px.scatter(
    df, x="x", y="y", size="size", color="color_value", color_continuous_scale="Viridis"
)

fig.show()

# %% [markdown]
"""
## Categorical Bubble Chart
"""
# %%
# Create a DataFrame
df = pd.DataFrame(
    {
        "category": ["Category A", "Category B", "Category C", "Category D"],
        "y": [10, 20, 15, 25],
        "size": [40, 50, 60, 70],
    }
)

# Create categorical bubble chart
fig = px.scatter(
    df,
    x="category",
    y="y",
    size="size",
    color="category",
    color_discrete_sequence=[
        "rgb(93, 164, 214)",
        "rgb(255, 144, 14)",
        "rgb(44, 160, 101)",
        "rgb(255, 65, 54)",
    ],
)

fig.show()

# %%
