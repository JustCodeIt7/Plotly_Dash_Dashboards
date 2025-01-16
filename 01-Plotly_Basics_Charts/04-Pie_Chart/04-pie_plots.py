# %% [markdown]
""" 
# Pie Chart in Plotly
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

companies = ['Apple', 'Samsung', 'Google', 'Huawei', 'Others']
market_share = np.random.dirichlet(np.ones(5)) * 100
revenue = np.random.uniform(10000, 50000, 5)
growth = np.random.uniform(-10, 30, 5)

df = pd.DataFrame({
    'company': companies,
    'market_share': market_share,
    'revenue': revenue,
    'growth': growth
})

# %% [markdown]
"""
## Example 1: Basic Interactive Pie Chart
"""

# %%
# Create basic interactive pie chart
fig = px.pie(
    df,
    values='market_share',
    names='company',
    title='Global Market Share Distribution',
    hover_data=['revenue', 'growth'],
    labels={'revenue': 'Revenue (M$)', 
            'growth': 'YoY Growth (%)',
            'market_share': 'Market Share (%)'},
    color_discrete_sequence=px.colors.qualitative.Set3
)

# Customize the appearance
fig.update_traces(
    textposition='inside',
    textinfo='percent+label',
    hovertemplate="<b>%{label}</b><br>" +
                  "Market Share: %{value:.1f}%<br>" +
                  "Revenue: $%{customdata[0]:.0f}M<br>" +
                  "Growth: %{customdata[1]:.1f}%<extra></extra>"
)

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    showlegend=False,
    width=800,
    height=600
)

fig.show()

# %% [markdown]
"""
## Example 2: Custom Donut Chart
"""

# %%
# Create custom donut chart
fig = go.Figure()
fig.add_trace(go.Pie(
    labels=df['company'],
    values=df['market_share'],
    hole=0.6,  # Creates donut chart
    textinfo='label+percent',
    textposition='outside',
    pull=[0.1 if x > 30 else 0 for x in df['market_share']],  # Pull out larger segments
    marker=dict(
        colors=px.colors.qualitative.Bold,
        line=dict(color='#ffffff', width=2)
    )
))

# Add central text and customize layout
fig.update_layout(
    title='Market Distribution<br>(with market leaders highlighted)',
    title_x=0.5,
    width=800,
    height=600,
    annotations=[dict(
        text='2024<br>Market<br>Share',
        x=0.5,
        y=0.5,
        font_size=20,
        showarrow=False
    )],
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

fig.show()

# %% [markdown]
"""
## Example 3: Comparative Pie Charts
"""

# %%
# Generate new data for comparison
df1 = df.copy()  # Use existing data for 2023
np.random.seed(43)  # Different seed for 2024 data
market_share_2024 = np.random.dirichlet(np.ones(5)) * 100
df2 = df.copy()
df2['market_share'] = market_share_2024

# Create subplots
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{'type':'domain'}, {'type':'domain'}]],
    subplot_titles=('2023 Market Share', '2024 Market Share')
)

# Add first pie chart (2023)
fig.add_trace(
    go.Pie(
        labels=df1['company'],
        values=df1['market_share'],
        name="2023",
        marker_colors=px.colors.qualitative.Set1,
        domain={'column': 0}
    ),
    1, 1
)

# Add second pie chart (2024)
fig.add_trace(
    go.Pie(
        labels=df2['company'],
        values=df2['market_share'],
        name="2024",
        marker_colors=px.colors.qualitative.Set1,
        domain={'column': 1}
    ),
    1, 2
)

# Update traces and layout
fig.update_traces(
    hole=0.4,
    textposition='inside',
    textinfo='percent+label'
)

fig.update_layout(
    title_text="Market Share Comparison: 2023 vs 2024",
    title_x=0.5,
    width=1200,
    height=600,
    annotations=[
        dict(text='2023', x=0.18, y=0.5, font_size=20, showarrow=False),
        dict(text='2024', x=0.82, y=0.5, font_size=20, showarrow=False)
    ],
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    )
)

fig.show()

# %%
