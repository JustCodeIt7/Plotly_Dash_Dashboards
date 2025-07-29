import plotly.express as px
import pandas as pd

# Data for a fictional company's product line
data = {
    'category': ["Electronics", "Electronics", "Electronics", "Laptops", "Laptops", "Smartphones", "Smartphones", "Gaming Consoles", "Gaming Consoles"],
    'brand': ["Laptops", "Smartphones", "Gaming Consoles", "Brand A", "Brand B", "Brand C", "Brand D", "Brand E", "Brand F"],
    'units_sold': [1500, 2500, 1000, 800, 700, 1200, 1300, 600, 400]
}
df = pd.DataFrame(data)

# Create an icicle chart with custom coloring
# The 'color' parameter is set to the 'brand' column, so each brand will have a unique color.
# The 'color_continuous_scale' parameter can be used if the color data is numerical.
fig = px.icicle(
    df, 
    path=['category', 'brand'], 
    values='units_sold', 
    color='brand'  # Color the chart by brand
)

# Update the layout for a professional look
fig.update_layout(
    title="Product Sales by Category and Brand",
    margin=dict(t=50, l=25, r=25, b=25)
)

# Show the plot
fig.show()
