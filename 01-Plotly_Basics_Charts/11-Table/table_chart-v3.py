import plotly.graph_objects as go
import pandas as pd

# --- Example 1: Basic Table from Lists ---
print("Displaying Example 1: Basic Table from Lists")
header_values_1 = ['Product', 'Quantity', 'Price']
cell_values_1 = [
    ['Apple', 'Banana', 'Orange'],
    [10, 15, 5],
    [0.5, 0.3, 0.6]
]

fig1 = go.Figure(data=[go.Table(
    header=dict(values=header_values_1,
                fill_color='lightblue',
                align='left',
                font=dict(color='black', size=12)),
    cells=dict(values=cell_values_1,
               fill_color='lightgrey',
               align='left',
               font=dict(color='black', size=11)))
])

fig1.update_layout(
    title_text='Example 1: Basic Table from Lists',
    title_x=0.5
)
fig1.show()


# --- Example 2: Table from Pandas DataFrame ---
print("\nDisplaying Example 2: Table from Pandas DataFrame")
# Sample DataFrame
data = {'Col A': [1, 2, 3, 4, 5],
        'Col B': [6, 7, 8, 9, 10],
        'Col C': ['P', 'Q', 'R', 'S', 'T']}
df = pd.DataFrame(data)

fig2 = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='center',
                font=dict(color='navy', size=14)),
    cells=dict(values=[df[col] for col in df.columns], # Pass each column as a list
               fill_color='lavender',
               align='center',
               font=dict(color='darkslategray', size=12),
               height=30) # Set cell height
)])

fig2.update_layout(
    title_text='Example 2: Table from Pandas DataFrame',
    title_x=0.5,
    width=500, # Adjust table width
    height=400 # Adjust table height
)
fig2.show()


# --- Example 3: Table with Styling (Alternating Colors) ---
print("\nDisplaying Example 3: Table with Styling")
header_values_3 = ['Rank', 'Player', 'Score', 'Team']
cell_values_3 = [
    [1, 2, 3, 4, 5],
    ['Player A', 'Player B', 'Player C', 'Player D', 'Player E'],
    [95, 92, 88, 85, 80],
    ['Team X', 'Team Y', 'Team X', 'Team Z', 'Team Y']
]

# Define alternating row colors
row_even_color = 'lightskyblue'
row_odd_color = 'whitesmoke'

fig3 = go.Figure(data=[go.Table(
    header=dict(values=header_values_3,
                line_color='darkslategray',
                fill_color='royalblue',
                align='center',
                font=dict(color='white', size=13)),
    cells=dict(values=cell_values_3,
               line_color='darkslategray',
               # Fill color can be array-like; it cycles through values
               fill_color=[[row_odd_color, row_even_color]*len(cell_values_3[0])],
               align='center',
               font=dict(color='darkslategray', size=11))
)])

fig3.update_layout(
    title_text='Example 3: Table with Styling (Alternating Colors)',
    title_x=0.5
)
fig3.show()

# You can save any figure as an HTML file
# fig1.write_html("table_chart_ex1.html")
# fig2.write_html("table_chart_ex2.html")
# fig3.write_html("table_chart_ex3.html")
