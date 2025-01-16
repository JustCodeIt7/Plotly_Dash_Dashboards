import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Create sample data for various examples
def generate_sales_data():
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
    products = ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch']
    data = []

    for date in dates:
        for product in products:
            sales = np.random.randint(100, 1000)
            revenue = sales * np.random.uniform(500, 2000)
            data.append({
                'date': date,
                'product': product,
                'sales': sales,
                'revenue': revenue,
                'quarter': f'Q{(date.month-1)//3 + 1}'
            })

    return pd.DataFrame(data)

# 1. Basic Bar Chart with Custom Styling
def basic_bar_chart():
    df = generate_sales_data()
    quarterly_sales = df.groupby('quarter')['sales'].sum().reset_index()

    fig = px.bar(quarterly_sales,
                 x='quarter',
                 y='sales',
                 title='Quarterly Sales Performance - 2024',
                 labels={'sales': 'Total Units Sold', 'quarter': 'Quarter'},
                 color_discrete_sequence=['#2ecc71'])

    fig.update_layout(
        plot_bgcolor='white',
        showlegend=False,
        hoverlabel=dict(bgcolor="white"),
        title_x=0.5
    )

    return fig

# 2. Grouped Bar Chart with Multiple Categories
def grouped_bar_chart():
    df = generate_sales_data()
    product_quarter_sales = df.groupby(['quarter', 'product'])['sales'].sum().reset_index()

    fig = px.bar(product_quarter_sales,
                 x='quarter',
                 y='sales',
                 color='product',
                 barmode='group',
                 title='Quarterly Sales by Product - 2024',
                 labels={'sales': 'Units Sold', 'quarter': 'Quarter'},
                 color_discrete_sequence=['#3498db', '#e74c3c', '#f1c40f', '#9b59b6'])

    fig.update_layout(
        xaxis_tickangle=-45,
        title_x=0.5,
        bargap=0.2
    )

    return fig

# 3. Stacked Bar Chart with Percentage
def stacked_percentage_bar():
    df = generate_sales_data()
    product_quarter_sales = df.pivot_table(
        values='sales',
        index='quarter',
        columns='product',
        aggfunc='sum'
    ).reset_index()

    # Calculate percentages
    for col in product_quarter_sales.columns[1:]:
        total = product_quarter_sales[product_quarter_sales.columns[1:]].sum(axis=1)
        product_quarter_sales[f'{col}_pct'] = product_quarter_sales[col] / total * 100

    fig = go.Figure()
    products = ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch']
    colors = ['#1abc9c', '#3498db', '#9b59b6', '#e74c3c']

    for product, color in zip(products, colors):
        fig.add_trace(go.Bar(
            name=product,
            x=product_quarter_sales['quarter'],
            y=product_quarter_sales[f'{product}_pct'],
            marker_color=color
        ))

    fig.update_layout(
        barmode='stack',
        title='Product Mix by Quarter (Percentage)',
        yaxis_title='Percentage of Total Sales',
        xaxis_title='Quarter',
        title_x=0.5,
        showlegend=True,
        legend_title='Products'
    )

    return fig

# 4. Bar Chart with Error Bars
def bar_chart_with_errors():
    df = generate_sales_data()
    monthly_stats = df.groupby('product').agg({
        'sales': ['mean', 'std']
    }).reset_index()
    monthly_stats.columns = ['product', 'mean_sales', 'std_sales']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Average Sales',
        x=monthly_stats['product'],
        y=monthly_stats['mean_sales'],
        error_y=dict(
            type='data',
            array=monthly_stats['std_sales'],
            visible=True,
            color='#2c3e50'
        ),
        marker_color='#3498db'
    ))

    fig.update_layout(
        title='Average Product Sales with Standard Deviation',
        xaxis_title='Product',
        yaxis_title='Average Units Sold',
        title_x=0.5,
        showlegend=False
    )

    return fig

# 5. Animated Bar Chart
def animated_bar_chart():
    df = generate_sales_data()

    fig = px.bar(df,
                 x='product',
                 y='sales',
                 color='product',
                 animation_frame='date',
                 animation_group='product',
                 range_y=[0, df['sales'].max() * 1.2],
                 title='Monthly Sales Evolution')

    fig.update_layout(
        showlegend=False,
        title_x=0.5,
        xaxis_tickangle=-45
    )

    return fig

# Main execution
if __name__ == "__main__":
    # Generate and show all charts
    basic_bar_chart().show()
    grouped_bar_chart().show()
    stacked_percentage_bar().show()
    bar_chart_with_errors().show()
    animated_bar_chart().show()
