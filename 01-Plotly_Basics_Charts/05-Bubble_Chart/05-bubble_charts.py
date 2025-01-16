# %% [markdown]
"""
# Bubble Charts
"""
# %%
import plotly.express as px

# %% [markdown]
"""
## Simple Bubble Chart
"""
#%%
import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=[1, 2, 3, 4], y=[10, 11, 12, 13],
    mode='markers',
    marker_size=[40, 60, 80, 100])
])

fig.show()
# %% [markdown]
"""
## Setting Marker Size and Color
"""

# %%
import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=[1, 2, 3, 4], y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
        opacity=[1, 0.8, 0.6, 0.4],
        size=[40, 60, 80, 100])
)])

fig.show()
# %% [markdown]
"""
## Scaling the Size of Bubble Charts
"""

# %%

import plotly.graph_objects as go

size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]
fig = go.Figure(data=[go.Scatter(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[11, 12, 10, 11, 12, 11, 12, 13, 12, 11],
    mode='markers',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4
    )
)])

fig.show()
# %% [markdown]
"""
## Hover Text with Bubble Charts
"""

#%%

import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=[1, 2, 3, 4], y=[10, 11, 12, 13],
    text=['A<br>size: 40', 'B<br>size: 60', 'C<br>size: 80', 'D<br>size: 100'],
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
        size=[40, 60, 80, 100],
    )
)])

fig.show()

# %%
# Bubble Chart with Colorscale
import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(
        size=[40, 60, 80, 100],
        color=[10, 20, 30, 40],  # Color values
        colorscale='Viridis',  # Colorscale
        showscale=True  # Add a color scale legend
    )
)])

fig.show()
# %% [markdown]
"""
## Categorical Bubble Chart
"""
# %%
import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=['Category A', 'Category B', 'Category C', 'Category D'],
    y=[10, 20, 15, 25],
    mode='markers',
    marker=dict(
        size=[40, 50, 60, 70],
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)', 'rgb(44, 160, 101)', 'rgb(255, 65, 54)']
    )
)])

fig.show()

# %%

