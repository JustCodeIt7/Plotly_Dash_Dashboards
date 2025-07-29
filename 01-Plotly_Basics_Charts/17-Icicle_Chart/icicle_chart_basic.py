
import plotly.express as px
import pandas as pd

# Create a dataset of employees in a corporate hierarchy
data = {
    "department": ["Corporate", "Corporate", "Corporate", "Sales", "Sales", "Sales", "IT", "IT", "IT"],
    "team": ["Executive", "Finance", "HR", "East", "West", "International", "Infrastructure", "Development", "Support"],
    "employees": [2, 3, 4, 10, 12, 8, 6, 15, 9]
}
df = pd.DataFrame(data)

# Create a basic icicle chart
# The 'path' parameter defines the hierarchy. The first item is the root, and each subsequent item is a child.
# The 'values' parameter determines the size of the rectangles.
fig = px.icicle(df, path=['department', 'team'], values='employees')

# Update the layout for a cleaner look
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Show the plot
fig.show()
