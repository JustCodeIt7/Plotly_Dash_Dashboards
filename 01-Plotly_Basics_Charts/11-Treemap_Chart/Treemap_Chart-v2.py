import plotly.express as px
import pandas as pd

# Example 1: Basic Treemap with explicit data
# This example shows a simple treemap where data is provided directly.
print("Example 1: Basic Treemap")
fig1 = px.treemap(
    names=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    title="Family Tree (Basic)"
)
fig1.update_traces(root_color="lightgrey")
fig1.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig1.show()

# Example 2: Treemap with hierarchical data using a DataFrame and path
# This example uses a pandas DataFrame and the 'path' parameter to define the hierarchy.
print("\nExample 2: Hierarchical Treemap with DataFrame")
df = px.data.tips()
fig2 = px.treemap(
    df,
    path=[px.Constant("all"), 'day', 'time', 'sex'],  # Defines the hierarchy levels
    values='total_bill',  # Size of the sectors based on total_bill
    title="Restaurant Tips Analysis (Hierarchical)"
)
fig2.update_traces(root_color="lightgrey")
fig2.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig2.show()

# Example 3: Treemap with color customization based on a continuous variable
# This example demonstrates how to color the treemap sectors based on another column ('tip').
print("\nExample 3: Treemap with Continuous Color Scale")
fig3 = px.treemap(
    df,
    path=[px.Constant("all"), 'day', 'time', 'sex'],
    values='total_bill',
    color='tip',  # Color sectors based on the 'tip' amount
    hover_data=['tip'], # Show tip amount on hover
    color_continuous_scale='RdBu', # Use a Red-Blue color scale
    color_continuous_midpoint=df['tip'].mean(), # Center the color scale around the mean tip
    title="Restaurant Tips Analysis (Colored by Tip Amount)"
)
fig3.update_traces(root_color="lightgrey")
fig3.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig3.show()

print("\nScript finished. Three treemap examples were generated.")
