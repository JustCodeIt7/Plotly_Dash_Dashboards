import plotly.express as px
import pandas as pd
import numpy as np # Import numpy for average calculation

# Example 1: Basic Treemap
# Using built-in tips dataset
print("Generating Example 1: Basic Treemap of Tips Data")
df_tips = px.data.tips()
fig1 = px.treemap(df_tips, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
fig1.update_layout(title_text='Example 1: Basic Treemap of Tips Data', margin = dict(t=50, l=25, r=25, b=25))
# fig1.show()
print("Example 1 generated.")

# Example 2: Treemap with Path and Color
# Using built-in gapminder dataset for a specific year
print("\nGenerating Example 2: Treemap of Global Population (2007)")
df_gapminder = px.data.gapminder().query("year == 2007")
fig2 = px.treemap(df_gapminder, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  # Calculate weighted average for midpoint
                  color_continuous_midpoint=np.average(df_gapminder['lifeExp'], weights=df_gapminder['pop']))
fig2.update_layout(title_text='Example 2: Treemap of Global Population (2007) Colored by Life Expectancy', margin = dict(t=50, l=25, r=25, b=25))
# fig2.show()
print("Example 2 generated.")


# Example 3: Treemap from a Pandas DataFrame with Custom Data and Text Info
# Creating a sample DataFrame
print("\nGenerating Example 3: Treemap of Custom Sales Data")
data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'SubCategory': ['X1', 'Y1', 'X2', 'Y2', 'X3', 'Y3', 'X4', 'Y4'],
    'Sales': [100, 150, 200, 50, 300, 250, 120, 180],
    'Profit': [10, 20, 30, 5, 40, 35, 15, 25]
}
df_custom = pd.DataFrame(data)

fig3 = px.treemap(df_custom, path=[px.Constant("Total Sales"), 'Region', 'Category', 'SubCategory'], values='Sales',
                  color='Profit', hover_data=['Sales', 'Profit'],
                  color_continuous_scale='viridis')
# Customize text information displayed on the treemap sectors
fig3.update_traces(textinfo = "label+value+percent parent+percent entry+percent root")
fig3.update_layout(title_text='Example 3: Treemap of Custom Sales Data Colored by Profit', margin = dict(t=50, l=25, r=25, b=25))
fig3.show() # Show the last figure
print("Example 3 generated and displayed.")
print("\nScript finished.")
