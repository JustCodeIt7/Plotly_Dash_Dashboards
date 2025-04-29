# %% [markdown]
"""
# Sunburst Chart Tutorial with Plotly

This tutorial demonstrates how to create Sunburst charts with Plotly.
Sunburst charts are a visualization technique for displaying hierarchical data using 
nested rings where each ring corresponds to a level in the hierarchy.

## What You'll Learn:
1. Basic Sunburst chart structure
2. Creating multi-level hierarchical visualizations
3. Customizing colors, text, and layout
4. Interactive features and callbacks
5. Advanced Sunburst chart techniques
"""

# %%
# Import required libraries
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# %% [markdown]
"""
## Example 1: Basic Sunburst Chart

A simple Sunburst chart showing the distribution of sales across different regions and countries.
"""

# %%
# Create a sample dataset for our basic sunburst chart
data = {
    'Region': ['North America', 'North America', 'Europe', 'Europe', 'Europe', 'Asia', 'Asia', 'Asia'],
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France', 'Japan', 'China', 'India'],
    'Sales': [25000, 12000, 15000, 17000, 13000, 16000, 28000, 18000]
}

df = pd.DataFrame(data)

# Create a basic sunburst chart
fig = px.sunburst(
    df,
    path=['Region', 'Country'],  # Defines the hierarchical levels
    values='Sales',              # Values determine the size of sectors
    title='Sales Distribution by Region and Country',
)

# Show the figure
fig.show()

# %% [markdown]
"""
## Example 2: Multi-level Hierarchical Sunburst Chart

Here we add another level of hierarchy to our data to create a more detailed visualization.
"""

# %%
# Create a more complex dataset with multiple hierarchical levels
data_multilevel = {
    'Region': ['North America', 'North America', 'North America', 'North America', 
               'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
               'Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Asia'],
    'Country': ['USA', 'USA', 'Canada', 'Canada',
                'UK', 'UK', 'Germany', 'Germany', 'France', 'France',
                'Japan', 'Japan', 'China', 'China', 'India', 'India'],
    'Product': ['Laptop', 'Smartphone', 'Laptop', 'Smartphone',
                'Laptop', 'Smartphone', 'Laptop', 'Smartphone', 'Laptop', 'Smartphone',
                'Laptop', 'Smartphone', 'Laptop', 'Smartphone', 'Laptop', 'Smartphone'],
    'Sales': [15000, 10000, 7000, 5000,
              8000, 7000, 10000, 7000, 6000, 7000,
              8000, 8000, 18000, 10000, 10000, 8000]
}

df_multilevel = pd.DataFrame(data_multilevel)

# Create a multi-level sunburst chart
fig_multilevel = px.sunburst(
    df_multilevel,
    path=['Region', 'Country', 'Product'],  # Three levels of hierarchy
    values='Sales',
    title='Sales Distribution by Region, Country, and Product',
    color='Sales',                          # Color based on sales values
    color_continuous_scale='RdBu',          # Red-Blue color scale
    color_continuous_midpoint=np.average(df_multilevel['Sales']),  # Set midpoint for color scale
)

# Show the figure
fig_multilevel.show()

# %% [markdown]
"""
## Example 3: Customized Sunburst Chart

This example shows how to customize the appearance and behavior of the Sunburst chart.
"""

# %%
# Create a slightly modified dataset for our customized example
data_custom = {
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics',
                 'Furniture', 'Furniture', 'Furniture', 'Furniture',
                 'Clothing', 'Clothing', 'Clothing', 'Clothing', 'Clothing'],
    'Subcategory': ['Laptops', 'Smartphones', 'Tablets', 'Wearables', 'Accessories', 'Monitors',
                    'Chairs', 'Tables', 'Desks', 'Bookcases',
                    'Shirts', 'Pants', 'Dresses', 'Shoes', 'Accessories'],
    'Sales': [25000, 32000, 12000, 8000, 5000, 7000,
              12000, 10000, 8000, 6000,
              15000, 12000, 10000, 18000, 6000],
    'Profit Margin': [0.25, 0.35, 0.20, 0.40, 0.50, 0.15,
                      0.20, 0.25, 0.15, 0.10,
                      0.30, 0.25, 0.35, 0.15, 0.45]
}

df_custom = pd.DataFrame(data_custom)
df_custom['Profit'] = df_custom['Sales'] * df_custom['Profit Margin']  # Calculate profit

# Create a customized sunburst chart
fig_custom = px.sunburst(
    df_custom,
    path=['Category', 'Subcategory'],
    values='Sales',
    color='Profit Margin',                      # Color based on profit margin
    color_continuous_scale=px.colors.sequential.Viridis,  # Use a different color scale
    hover_data=['Profit'],                      # Include profit in hover information
    custom_data=['Profit'],                     # Additional data for custom hover template
    title='Product Categories by Sales (with Profit Margin)',
)

# Customize the appearance and behavior
fig_custom.update_traces(
    textinfo='label+percent parent+value',      # Show labels, percentage of parent, and values
    hovertemplate='<b>%{label}</b><br>Sales: $%{value:,.0f}<br>Profit: $%{customdata[0]:,.0f}<br>Profit Margin: %{color:.1%}<extra></extra>',
    insidetextorientation='radial'              # Text orientation
)

# Update layout
fig_custom.update_layout(
    height=700,
    width=800,
    uniformtext=dict(minsize=10, mode='hide'),  # Hide text if it doesn't fit
    coloraxis_colorbar=dict(
        title='Profit Margin',
        tickformat='.0%',
    ),
)

# Show the figure
fig_custom.show()

# %% [markdown]
"""
## Example 4: Sunburst with Graph Objects

While Plotly Express is convenient, using the lower-level Graph Objects API gives even more control.
"""

# %%
# Create a sunburst chart using Graph Objects
fig_go = go.Figure(
    go.Sunburst(
        labels=df_custom['Subcategory'].tolist() + df_custom['Category'].tolist(),
        parents=[''] * len(df_custom['Subcategory']) + df_custom['Category'].tolist(),
        values=df_custom['Sales'].tolist() + [0] * len(df_custom['Category'].unique()),
        branchvalues='total',  # 'total' or 'remainder'
        marker=dict(
            colors=list(range(len(df_custom['Subcategory']))) + [0] * len(df_custom['Category'].unique()),
            colorscale='Reds',
            showscale=True,
            colorbar=dict(
                title='Index Value',
                thickness=15,
                len=0.7,
                tickvals=[0, len(df_custom['Subcategory'])],
                ticktext=['Low', 'High']
            )
        ),
        hovertemplate='<b>%{label}</b><br>Sales: $%{value:,.0f}<extra></extra>',
        name='',
        maxdepth=2  # Limit the displayed depth
    )
)

# Update layout
fig_go.update_layout(
    title="Product Sales - Graph Objects Implementation",
    height=700,
    width=800,
    margin=dict(t=60, l=25, r=25, b=25)
)

# Show the figure
fig_go.show()

# %% [markdown]
"""
## Example 5: Interactive Business Dashboard with Sunburst Chart

Now let's create a more realistic business dashboard with data showing departments, project categories, and project status.
"""

# %%
# Create a realistic business dataset
departments = ['Engineering', 'Marketing', 'Sales', 'Customer Support', 'R&D']
categories = ['Development', 'Design', 'Testing', 'Campaigns', 'Analytics', 
              'Lead Generation', 'Acquisition', 'Retention', 'Technical Support', 
              'Training', 'Research', 'Innovation']
statuses = ['Completed', 'In Progress', 'Planned']

# Generate hierarchical data
np.random.seed(42)  # For reproducibility
business_data = []

for dept in departments:
    # Assign relevant categories for each department
    if dept == 'Engineering':
        dept_categories = ['Development', 'Design', 'Testing']
    elif dept == 'Marketing':
        dept_categories = ['Campaigns', 'Analytics']
    elif dept == 'Sales':
        dept_categories = ['Lead Generation', 'Acquisition', 'Retention']
    elif dept == 'Customer Support':
        dept_categories = ['Technical Support', 'Training']
    else:  # R&D
        dept_categories = ['Research', 'Innovation']
    
    for category in dept_categories:
        for status in statuses:
            # Create more realistic distribution of projects
            if status == 'Completed':
                num_projects = np.random.randint(5, 20)
                budget = np.random.randint(10000, 100000)
                actual_cost = budget * np.random.uniform(0.8, 1.2)  # Some variance in costs
            elif status == 'In Progress':
                num_projects = np.random.randint(3, 15)
                budget = np.random.randint(10000, 80000)
                actual_cost = budget * np.random.uniform(0.5, 0.9)  # Only part of budget spent
            else:  # Planned
                num_projects = np.random.randint(1, 10)
                budget = np.random.randint(10000, 70000)
                actual_cost = 0  # No money spent yet
            
            business_data.append({
                'Department': dept,
                'Category': category,
                'Status': status,
                'Projects': num_projects,
                'Budget': budget,
                'Actual Cost': actual_cost,
                'Budget Utilization': actual_cost / budget if budget > 0 and status != 'Planned' else 0
            })

# Convert to DataFrame
df_business = pd.DataFrame(business_data)

# Create a comprehensive sunburst chart
fig_business = px.sunburst(
    df_business,
    path=['Department', 'Category', 'Status'],
    values='Projects',
    color='Budget Utilization',
    color_continuous_scale=px.colors.diverging.RdYlGn_r,  # Red for over budget, green for under
    color_continuous_midpoint=1.0,  # Midpoint at 100% budget utilization
    hover_data=['Budget', 'Actual Cost'],
    custom_data=['Budget', 'Actual Cost', 'Budget Utilization'],
    title='Project Distribution & Budget Utilization',
)

# Enhance the visualization
fig_business.update_traces(
    textinfo='label+percent entry',
    hovertemplate='<b>%{label}</b><br>' +
                  'Projects: %{value}<br>' +
                  'Budget: $%{customdata[0]:,.0f}<br>' +
                  'Actual Cost: $%{customdata[1]:,.0f}<br>' +
                  'Budget Utilization: %{customdata[2]:.1%}<extra></extra>'
)

# Update layout
fig_business.update_layout(
    height=800,
    width=900,
    title_x=0.5,
    coloraxis_colorbar=dict(
        title='Budget<br>Utilization',
        tickvals=[0, 0.8, 1, 1.2],
        ticktext=['0%', '80%', '100%', '120%']
    ),
)

# Show the figure
fig_business.show()

# %% [markdown]
"""
## Conclusion

Sunburst charts provide a powerful way to visualize hierarchical data in a compact form.
You've learned how to:

1. Create basic and multi-level sunburst charts
2. Customize colors, text, and layout
3. Use both Plotly Express and Graph Objects
4. Build realistic business dashboards

These techniques will help you create compelling visualizations for your data analysis projects.
"""

# %%
# Example of a fully maximal Sunburst chart for a thumbnail or final demo
# Generate sample data for a complete organization structure
org_data = []

# Levels: Division > Department > Team > Role
divisions = ['Technology', 'Operations', 'Business']
departments = {
    'Technology': ['Engineering', 'Product', 'Data Science', 'IT'],
    'Operations': ['Finance', 'HR', 'Facilities', 'Legal'],
    'Business': ['Sales', 'Marketing', 'Customer Success', 'Strategy']
}

teams = {
    'Engineering': ['Frontend', 'Backend', 'Mobile', 'DevOps'],
    'Product': ['Design', 'Research', 'Management'],
    'Data Science': ['Analytics', 'ML/AI', 'Data Engineering'],
    'IT': ['Support', 'Security', 'Infrastructure'],
    'Finance': ['Accounting', 'Treasury', 'Tax', 'Audit'],
    'HR': ['Recruitment', 'Training', 'Benefits', 'Culture'],
    'Facilities': ['Real Estate', 'Maintenance', 'Security'],
    'Legal': ['Compliance', 'IP', 'Corporate'],
    'Sales': ['Enterprise', 'SMB', 'International', 'Partners'],
    'Marketing': ['Brand', 'Digital', 'Events', 'Content'],
    'Customer Success': ['Support', 'Onboarding', 'Renewal'],
    'Strategy': ['Planning', 'M&A', 'Business Intel']
}

roles = ['Junior', 'Mid-level', 'Senior', 'Lead']

# Generate the hierarchical data
np.random.seed(123)
for division in divisions:
    for department in departments[division]:
        for team in teams[department]:
            for role in roles:
                headcount = np.random.randint(1, 20 if role == 'Mid-level' else 10)
                avg_salary = {
                    'Junior': np.random.randint(50000, 70000),
                    'Mid-level': np.random.randint(70000, 100000),
                    'Senior': np.random.randint(100000, 150000),
                    'Lead': np.random.randint(150000, 200000)
                }[role]
                
                org_data.append({
                    'Division': division,
                    'Department': department,
                    'Team': team,
                    'Role': role,
                    'Headcount': headcount,
                    'Avg Salary': avg_salary,
                    'Total Cost': headcount * avg_salary
                })

df_org = pd.DataFrame(org_data)

# Create maximal sunburst chart
fig_max = px.sunburst(
    df_org,
    path=['Division', 'Department', 'Team', 'Role'],
    values='Headcount',
    color='Avg Salary',
    color_continuous_scale='Turbo',
    custom_data=['Total Cost', 'Avg Salary'],
    title='Organization Structure & Compensation Overview',
)

fig_max.update_traces(
    textinfo='label+percent entry+percent parent',
    insidetextorientation='radial',
    hovertemplate='<b>%{label}</b><br>' +
                 'Headcount: %{value}<br>' +
                 'Avg Salary: $%{customdata[1]:,.0f}<br>' +
                 'Total Cost: $%{customdata[0]:,.0f}<extra></extra>'
)

fig_max.update_layout(
    height=900,
    width=900,
    title_x=0.5,
    title_font_size=20,
    margin=dict(t=80, b=20, l=20, r=20),
    coloraxis_colorbar=dict(
        title='Average<br>Salary',
        tickprefix='$',
        tickformat=',.0f'
    ),
)

fig_max.show()
# %%