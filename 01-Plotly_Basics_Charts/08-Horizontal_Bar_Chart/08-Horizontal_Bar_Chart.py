#%%
# Horizontal Bar Chart
import random
import plotly.express as px
import pandas as pd

#%%
# Horizontal Bar Chart# %% Example 1: Basic Horizontal Bar Chart
# Create sample data
data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India'],
    'GDP': [23000, 17700, 5400, 4300, 3500]
}
df = pd.DataFrame(data)
# %%
# Create basic horizontal bar chart
fig = px.bar(
    df,
    x='GDP',  # Values for the bars (x-axis for horizontal)
    y='Country',  # Categories on y-axis
    orientation='h',  # 'h' for horizontal orientation
    title='GDP by Country (Billions USD)'
)

# Show the figure
fig.show()
# %%
# Example 2: Horizontal Bar Chart with Custom Colors
# Create sample data
tech_companies = {
    'Company': ['Apple', 'Microsoft', 'Google', 'Amazon', 'Meta', 'Tesla', 'NVIDIA'],
    'Revenue': [394.33, 211.91, 282.84, 513.98, 134.90, 96.77, 60.92],
    'Sector': ['Consumer Electronics', 'Software', 'Internet', 'E-commerce', 'Social Media', 'Automotive', 'Semiconductors']
}
df2 = pd.DataFrame(tech_companies)

# Sort the data by revenue
df2 = df2.sort_values('Revenue')

# Create customized horizontal bar chart
fig2 = px.bar(
    df2,
    x='Revenue',
    y='Company',
    orientation='h',
    color='Sector',  # Color bars by sector
    title='Tech Company Revenue (Billions USD)',
    labels={'Revenue': 'Annual Revenue (Billions USD)', 'Company': ''},
    text='Revenue',  # Display values on bars
    height=500,
    color_discrete_sequence=px.colors.qualitative.G10  # Custom color palette
)

# Customize layout
fig2.update_traces(
    texttemplate='%{text:.1f}B',  # Format text with 1 decimal place and B suffix
    textposition='outside'  # Position text outside of bars
)
fig2.update_layout(
    xaxis_title='Annual Revenue (Billions USD)',
    yaxis=dict(autorange="reversed"),  # Reverse y-axis to show highest value at top
    margin=dict(l=20, r=20, t=40, b=20)
)

fig2.show()
# %%
# %% Example 3: Advanced Horizontal Bar Chart with Categories and Annotations
# Create data for social media platforms
social_media = {
    'Platform': ['Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'TikTok', 'Snapchat', 'Twitter'],
    'Users': [2986, 2515, 2000, 1478, 1000, 557, 436],
    'Category': ['Meta', 'Google', 'Meta', 'Meta', 'ByteDance', 'Snap Inc.', 'X Corp'],
    'Founded': [2004, 2005, 2009, 2010, 2016, 2011, 2006]
}
df3 = pd.DataFrame(social_media)

# Create advanced horizontal bar chart
fig3 = px.bar(
    df3,
    x='Users',
    y='Platform',
    orientation='h',
    color='Category',
    title='Social Media Platforms by Monthly Active Users (Millions)',
    text='Users',
    hover_data=['Founded'],  # Add founding year to hover information
    labels={'Users': 'Monthly Active Users (Millions)', 'Platform': '', 'Founded': 'Founded Year'},
    height=600,
    color_discrete_sequence=px.colors.qualitative.Plotly
)

# Customize layout and add features
fig3.update_traces(
    texttemplate='%{text:,}M',
    textposition='inside',
    marker_line_color='black',
    marker_line_width=1
)

# Add a vertical line for average
avg_users = df3['Users'].mean()
fig3.add_vline(
    x=avg_users, 
    line_dash='dash', 
    line_color='grey',
    annotation_text=f'Average: {avg_users:.0f}M',
    annotation_position='top right'
)

# Customize layout
fig3.update_layout(
    xaxis=dict(
        tickformat=',d',  # Format tick labels with commas
        title_font=dict(size=14)
    ),
    yaxis=dict(
        title_font=dict(size=14)
    ),
    title=dict(
        font=dict(size=16)
    ),
    legend_title='Parent Company',
    bargap=0.2
)

fig3.show()
# %%
# Create sample sales data
sales_data = pd.DataFrame({
    'Product': ['Laptops', 'Smartphones', 'Tablets', 'Wearables'],
    'Revenue': [24000, 18500, 9800, 6700],
    'Profit Margin (%)': [12.3, 18.7, 9.5, 22.1]
})

# Create styled horizontal bar chart
fig = px.bar(sales_data,
             x='Revenue',
             y='Product',
             orientation='h',
             title='Q4 Product Performance',
             color='Profit Margin (%)',  # Color by profit margin
             text_auto=True,             # Show values on bars
             labels={'Revenue':'Quarterly Revenue (USD)'},
             color_continuous_scale=px.colors.sequential.Viridis)

fig.update_layout(
    uniformtext_minsize=8,       # Ensure text fits
    plot_bgcolor='rgba(0,0,0,0)',# Transparent background
    yaxis_title=None             # Remove redundant label
)
fig.show()
# %%
# Create multi-dimensional data
regions = ['North', 'South', 'East', 'West']
months = ['Jan', 'Feb', 'Mar']

# Simulated sales data with multiple categories
df = pd.DataFrame({
    'Region': regions * 3,
    'Month': months*4,
    'Sales': [random.randint(80,150) for _ in range(12)],
    'Customers': [random.randint(50,120) for _ in range(12)]
})

# Create interactive horizontal bar chart
fig = px.bar(df,
             x='Sales',
             y='Region',
             orientation='h',
             animation_frame='Month',  # Add animation
             color='Customers',
             hover_name='Region',      # Custom hover text
             labels={'Sales':'Monthly Sales'},
             category_orders={'Month':months})

fig.update_layout(
    title_text='<b>Regional Sales Performance (Animated)</b>',
    font_size=10,
    height=500
)

# Save as HTML for YouTube demo
fig.show()
# %%
