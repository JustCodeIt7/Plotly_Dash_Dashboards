# %% [markdown]
# # Plotly Figure Factory Table Examples
# 
# Plotly's Figure Factory provides a simple way to create formatted tables for data visualization. Unlike `go.Table`, the `create_table()` function automatically handles styling and layout, making it ideal for quick, professional-looking table displays.
# 

# %%
# Import the necessary libraries for creating tables and handling data.
import plotly.figure_factory as ff
import pandas as pd

# %% [markdown]
# ## Example 1: Basic Table Creation
# 
# Figure Factory makes it easy to create tables from two common data formats: lists of lists and Pandas DataFrames. When using a list of lists, the first row serves as headers. DataFrames automatically use their column names as headers, making them ideal for data analysis workflows.
# 

# %%
# Method 1: Create a table from a list of lists.
# The first row contains column headers, followed by data rows.
data_matrix = [
    ["Country", "Year", "Population"],
    ["United States", 2000, 282200000],
    ["Canada", 2000, 27790000],
    ["United States", 2010, 309000000],
    ["Canada", 2010, 34000000],
]

# Generate the table using Figure Factory's create_table function.
fig1 = ff.create_table(data_matrix)
fig1.show()

print("\n" + "=" * 50 + "\n")

#%%

# Method 2: Create a table from a Pandas DataFrame.
# DataFrames automatically use column names as headers.
df = pd.DataFrame(
    {
        "Name": ["Luke", "Anakin", "Padme", "Yoda"],
        "Age": [25, 50, 45, 353],
        "Planet": ["Tatooine", "Tatooine", "Naboo", "Dagobah"],
    }
)

# Pass the DataFrame directly to create_table.
fig2 = ff.create_table(df)
fig2.show()

# %% [markdown]
# ## Example 2: Customizing Table Appearance
# 
# Tables can be extensively customized to match your presentation needs. You can apply color gradients using `colorscale`, modify fonts with `update_layout()`, and control the table's dimensions. These customizations help create professional, branded visualizations that stand out in reports and dashboards.
# 

# %%
# Create a DataFrame with sales data.
df_sales = pd.DataFrame(
    {
        "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
        "Price": ["$999", "$29", "$79", "$349", "$159"],
        "Stock": [45, 230, 156, 89, 134],
        "Sales": [120, 450, 280, 95, 210],
    }
)

# Create a table with multiple customizations applied.
# 1. Apply a custom colorscale - purple gradient for visual appeal.
fig = ff.create_table(
    df_sales, colorscale=[[0, "#4d004c"], [0.5, "#8b008b"], [1, "#e6d5f0"]]
)

# 2. Customize font properties for better readability and style.
# 3. Set a custom height to control the table's vertical size.
fig.update_layout(
    font=dict(
        size=14,  # Larger font for presentations
        family="Arial",  # Professional, clean font
        color="white",  # White text for contrast with dark colors
    ),
    height=400,  # Fixed height for consistent layout
)

# Display the fully customized table.
fig.show()

# %% [markdown]
# ## Example 3: Working with DataFrame Indexes
# 
# By default, DataFrame index columns are not displayed in Figure Factory tables. However, indexes often contain valuable information such as order IDs, dates, or unique identifiers. Using `reset_index()` converts the index into a regular column, making it visible in your table presentation.
# 

# %%
# Create a DataFrame with a meaningful index (customer IDs).
df_orders = pd.DataFrame(
    {
        "Item": ["Tablet", "Phone", "Laptop"],
        "Quantity": [2, 1, 1],
        "Total": [599, 799, 1299],
    },
    index=["ORD-001", "ORD-002", "ORD-003"],
)

# Reset the index to convert it into a regular column.
# This makes the index visible in the table as "index" column.
df_with_index = df_orders.reset_index()

# Create the table with the index now displayed as a column.
fig = ff.create_table(df_with_index)

# Display the table showing order IDs.
fig.show()



# %%
