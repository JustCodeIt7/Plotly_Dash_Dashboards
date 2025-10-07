# %%
import plotly.express as px
import pandas as pd
import numpy as np

# Pros:
# Space Efficiency: Efficient at showing hierarchical data in a compact space.
#   - You can display hundreds of data points without scrolling or multiple pages.
# Dual Encoding: You can show two metrics simultaneously
#   - size represents one variable (like revenue) while color represents another (like profit margin).

# Cons:
#   - Limited Detail: While Treemaps show hierarchical relationships, they can obscure individual data points.
#   - Not Ideal for Small Values: Small segments may be hard to see or interpret.
#   - Terrible for Temporal Data: Treemaps are not suitable for showing changes over time.

# Usage:
#   Financial Services - Visualizing portfolio allocations, risk assessments, or financial hierarchies.
#   Computer Science - Disk usage, file system structures, or software component hierarchies.
#   Marketing - Campaign performance across different segments or product categories.
#   Healthcare - Patient demographics, treatment outcomes, or resource allocations.

# %%
################################ Example 1: Basic Treemap ################################
print("Generating Example 1: Basic Treemap of Tips Data")
print("Generating Example 1: Basic Treemap of Tips Data")
df_tips = px.data.tips()  # Load built-in tips dataset
fig1 = px.treemap(
    df_tips, path=[px.Constant("all"), "day", "time", "sex"], values="total_bill"
)  # Set hierarchy and size

fig1.update_layout(
    title_text="Example 1: Basic Treemap of Tips Data",
    margin=dict(t=50, l=25, r=25, b=25),
)  # Adjust plot margins

fig1.show()
print("Example 1 generated.")

# %%
################################ Example 2: Colored Treemap ################################
print("\nGenerating Example 2: Treemap of Global Population (2007)")
df_gapminder = px.data.gapminder().query(
    "year == 2007"
)  # Filter dataset for a single year
fig2 = px.treemap(
    df_gapminder,
    path=[px.Constant("world"), "continent", "country"],
    values="pop",
    color="lifeExp",
    hover_data=["iso_alpha"],  # Color boxes by life expectancy
    color_continuous_scale="RdBu",
    # Set the color scale midpoint to the population-weighted average life expectancy
    color_continuous_midpoint=np.average(
        df_gapminder["lifeExp"], weights=df_gapminder["pop"]
    ),
)
fig2.update_layout(
    title_text="Example 2: Treemap of Global Population (2007) Colored by Life Expectancy",
    margin=dict(t=50, l=25, r=25, b=25),
)
fig2.show()
print("Example 2 generated.")

# %%
################################ Example 3: Custom Data Treemap ################################
print("\nGenerating Example 3: Treemap of Custom Sales Data")
# Create a sample DataFrame from a dictionary
data = {
    "Region": ["North", "North", "South", "South", "East", "East", "West", "West"],
    "Category": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "SubCategory": ["X1", "Y1", "X2", "Y2", "X3", "Y3", "X4", "Y4"],
    "Sales": [100, 150, 200, 50, 300, 250, 120, 180],
    "Profit": [10, 20, 30, 5, 40, 35, 15, 25],
}
df_custom = pd.DataFrame(data)

fig3 = px.treemap(
    df_custom,
    path=[px.Constant("Total Sales"), "Region", "Category", "SubCategory"],
    values="Sales",
    color="Profit",
    hover_data=["Sales", "Profit"],  # Add sales and profit to hover tooltip
    color_continuous_scale="viridis",
)

# Customize the text displayed on each sector of the treemap
text_components = [
    "label",
    "value",
    "percent parent",
    "percent entry",
    "percent root"
]

# Join the list items with a '+' to create the final string
text_info_str = "+".join(text_components)
print(text_info_str)
# Apply the string to the trace update
fig3.update_traces(textinfo="+".join(text_components))
fig3.update_traces(textinfo="label+value+percent parent+percent entry+percent root")


fig3.update_layout(
    title_text="Example 3: Treemap of Custom Sales Data Colored by Profit",
    margin=dict(t=50, l=25, r=25, b=25),
)
fig3.show()
print("Example 3 generated and displayed.")
print("\nScript finished.")

# %%
