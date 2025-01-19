# %% [markdown]
"""
# PLOTLY BAR CHART TUTORIAL

1. Install plotly (in your terminal or command prompt):

   pip install plotly
"""
#%%
# 2. Import libraries
import plotly.express as px
import pandas as pd

# %%
# 3. Create sample dataset
data = {
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics',
                 'Furniture', 'Furniture', 'Furniture', 'Furniture',
                 'Clothing', 'Clothing', 'Clothing', 'Clothing'],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'] * 3,
    'Sales': [500, 700, 600, 800,
              300, 400, 350, 500,
              250, 300, 400, 450]
}
df = pd.DataFrame(data)
print(df)

# %%
#######################################################
# 4. Basic Bar Chart
#######################################################
df_category_sales = df.groupby('Category', as_index=False)['Sales'].sum()
fig_basic = px.bar(
    df_category_sales,
    x='Category',
    y='Sales',
    title='Total Sales by Category (Basic Bar Chart)'
)
fig_basic.show()
# %%
# %%
#######################################################
# 5. Custom Bar Chart with Color and Hover Data
#######################################################
fig_custom = px.bar(
    df,
    x='Quarter',
    y='Sales',
    color='Category',
    title='Sales by Category and Quarter (Customized)',
    labels={
        'Quarter': 'Quarter of the Year',
        'Sales': 'Total Sales (USD)',
        'Category': 'Product Category'
    },
    hover_data=['Category', 'Sales']
)
fig_custom.show()
# %%
#######################################################
# 6. Grouped Bar Chart
#######################################################
fig_grouped = px.bar(
    df,
    x='Quarter',
    y='Sales',
    color='Category',
    barmode='group',
    title='Sales by Category and Quarter (Grouped Bar Chart)'
)
fig_grouped.show()

#######################################################
# 7. Stacked Bar Chart
#######################################################
fig_stacked = px.bar(
    df,
    x='Quarter',
    y='Sales',
    color='Category',
    barmode='stack',
    title='Sales by Category and Quarter (Stacked Bar Chart)'
)
fig_stacked.show()
# %%
#######################################################
# 8. Horizontal Bar Chart
#######################################################
df_category_sales = df.groupby('Category', as_index=False)['Sales'].sum()
fig_horizontal = px.bar(
    df_category_sales,
    x='Sales',
    y='Category',
    orientation='h',
    title='Total Sales by Category (Horizontal Bar Chart)',
    color='Category'
)
fig_horizontal.show()
# %%
#######################################################
# 9. Advanced Layout Customization
#######################################################
fig_custom_layout = px.bar(
    df,
    x='Quarter',
    y='Sales',
    color='Category',
    barmode='group',
    title='Sales by Category and Quarter (Final Customized Layout)'
)

fig_custom_layout.update_layout(
    title={
        'text': 'Sales by Category and Quarter (Customized Layout)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis=dict(
        title='Quarter',
        titlefont_size=14,
        tickfont_size=12
    ),
    yaxis=dict(
        title='Sales (USD)',
        titlefont_size=14,
        tickfont_size=12
    ),
    legend=dict(
        title='Product Category',
        x=1,
        y=1,
        xanchor='left',
        yanchor='top'
    )
)

fig_custom_layout.show()

# %%
