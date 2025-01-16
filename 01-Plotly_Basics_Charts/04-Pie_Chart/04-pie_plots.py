import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Create sample data for various examples
def generate_market_data():
    np.random.seed(42)

    # Market share data
    companies = ['Apple', 'Samsung', 'Google', 'Huawei', 'Others']
    market_share = np.random.dirichlet(np.ones(5)) * 100
    revenue = np.random.uniform(10000, 50000, 5)
    growth = np.random.uniform(-10, 30, 5)

    return pd.DataFrame({
        'company': companies,
        'market_share': market_share,
        'revenue': revenue,
        'growth': growth
    })

# 1. Basic Interactive Pie Chart
def basic_pie_chart():
    df = generate_market_data()

    fig = px.pie(df,
                 values='market_share',
                 names='company',
                 title='Global Market Share Distribution',
                 hover_data=['revenue', 'growth'],
                 labels={'revenue': 'Revenue (M$)', 'growth': 'YoY Growth (%)'},
                 color_discrete_sequence=px.colors.qualitative.Set3)

    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        showlegend=False
    )

    return fig

# 2. Donut Chart with Custom Styling
def custom_donut_chart():
    df = generate_market_data()

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=df['company'],
        values=df['market_share'],
        hole=0.6,
        textinfo='label+percent',
        textposition='outside',
        pull=[0.1 if x > 30 else 0 for x in df['market_share']],
        marker=dict(
            colors=px.colors.qualitative.Bold,
            line=dict(color='#ffffff', width=2)
        )
    ))

    # Add central text
    fig.update_layout(
        title='Market Distribution<br>(with revenue leaders highlighted)',
        annotations=[dict(
            text='2024<br>Market<br>Share',
            x=0.5, y=0.5,
            font_size=20,
            showarrow=False
        )],
        title_x=0.5
    )

    return fig

# 3. Animated Pie Chart Over Time
def animated_pie_chart():
    # Generate time series data
    periods = 4
    companies = ['Apple', 'Samsung', 'Google', 'Huawei', 'Others']
    data = []

    for quarter in range(1, periods + 1):
        shares = np.random.dirichlet(np.ones(5)) * 100
        for company, share in zip(companies, shares):
            data.append({
                'quarter': f'Q{quarter}',
                'company': company,
                'share': share
            })

    df = pd.DataFrame(data)

    # Frame data for animation
    frames = []
    for quart in df['quarter'].unique():
        frame_data = df[df['quarter'] == quart]
        frames.append(go.Frame(
            data=[go.Pie(labels=frame_data['company'],
                         values=frame_data['share'],
                         textinfo='label+percent')],
            name=quart
        ))

    # Initial data
    fig = go.Figure(
        data=[
            go.Pie(
                labels=df[df['quarter'] == 'Q1']['company'],
                values=df[df['quarter'] == 'Q1']['share'],
                textinfo='label+percent'
            )
        ],
        layout=go.Layout(
            title='Quarterly Market Share Evolution',
            title_x=0.5,
            updatemenus=[{
                'buttons': [
                    {
                        'args': [None, {'frame': {'duration': 1000, 'redraw': True},
                                        'fromcurrent': True}],
                        'label': 'Play',
                        'method': 'animate'
                    },
                    {
                        'args': [[None], {'frame': {'duration': 0, 'redraw': True},
                                          'mode': 'immediate',
                                          'transition': {'duration': 0}}],
                        'label': 'Pause',
                        'method': 'animate'
                    }
                ],
                'direction': 'left',
                'pad': {'r': 10, 't': 87},
                'showactive': False,
                'type': 'buttons',
                'x': 0.1,
                'xanchor': 'right',
                'y': 0,
                'yanchor': 'top'
            }]
        ),
        frames=frames
    )

    fig.update_layout(
        showlegend=True,
        legend_title='Companies'
    )

    return fig

# 4. Multi-level Pie Chart (Sunburst)
def hierarchical_pie_chart():
    # Generate hierarchical data
    data = {
        'category': ['Electronics']*3 + ['Software']*3 + ['Services']*3,
        'subcategory': ['Phones', 'Laptops', 'Tablets',
                        'OS', 'Apps', 'Games',
                        'Cloud', 'Support', 'Consulting'],
        'revenue': np.random.uniform(100, 1000, 9)
    }
    df = pd.DataFrame(data)

    fig = px.sunburst(df,
                      path=['category', 'subcategory'],
                      values='revenue',
                      title='Revenue Distribution by Category',
                      color_discrete_sequence=px.colors.qualitative.Pastel)

    fig.update_layout(
        title_x=0.5,
        width=800,
        height=800
    )

    return fig

# 5. Comparative Pie Charts in Subplots
def comparative_pie_charts():
    # Generate data for two time periods
    df1 = generate_market_data()
    df2 = generate_market_data()

    fig = make_subplots(rows=1, cols=2,
                        specs=[[{'type':'domain'}, {'type':'domain'}]],
                        subplot_titles=('2023 Market Share', '2024 Market Share'))

    fig.add_trace(go.Pie(labels=df1['company'],
                         values=df1['market_share'],
                         name="2023",
                         marker_colors=px.colors.qualitative.Set1),
                  1, 1)

    fig.add_trace(go.Pie(labels=df2['company'],
                         values=df2['market_share'],
                         name="2024",
                         marker_colors=px.colors.qualitative.Set1),
                  1, 2)

    fig.update_traces(hole=0.4, textposition='inside', textinfo='percent+label')
    fig.update_layout(
        title_text="Market Share Comparison: 2023 vs 2024",
        title_x=0.5,
        annotations=[
            dict(text='2023', x=0.18, y=0.5, font_size=20, showarrow=False),
            dict(text='2024', x=0.82, y=0.5, font_size=20, showarrow=False)
        ]
    )

    return fig

# Main execution
if __name__ == "__main__":
    # Generate and show all charts
    basic_pie_chart().show()
    custom_donut_chart().show()
    animated_pie_chart().show()
    hierarchical_pie_chart().show()
    comparative_pie_charts().show()
