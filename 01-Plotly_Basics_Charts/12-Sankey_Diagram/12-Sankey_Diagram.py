import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Example 1: Basic Sankey Diagram with explicit nodes and links

# Define nodes and links directly
fig1 = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"], # Node labels
      color = ["blue", "blue", "green", "green", "red", "red"] # Node colors
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3], # Indices correspond to labels, e.g., A1 is 0
      target = [2, 3, 3, 4, 4, 5], # Indices correspond to labels, e.g., B1 is 2
      value = [8, 4, 2, 8, 4, 2], # Values of the links
      color = ["rgba(0,0,255,0.2)", "rgba(0,0,255,0.2)", "rgba(0,0,255,0.2)",
               "rgba(0,255,0,0.2)", "rgba(0,255,0,0.2)", "rgba(255,0,0,0.2)"] # Link colors (optional)
  ))])

fig1.update_layout(title_text="Example 1: Basic Sankey Diagram", font_size=10)
# fig1.show() # Uncomment to display the figure

# Example 2: Sankey Diagram from a Pandas DataFrame using Plotly Express

# Create a sample DataFrame
data = {
    'Source': ['Energy Source A', 'Energy Source A', 'Energy Source B', 'Use Case 1', 'Use Case 2'],
    'Target': ['Use Case 1', 'Use Case 2', 'Use Case 2', 'End Use X', 'End Use Y'],
    'Value': [30, 20, 50, 25, 75],
    'Color': ['red', 'blue', 'green', 'purple', 'orange'] # Optional: Define colors for links
}
df = pd.DataFrame(data)

# Create the Sankey diagram using px.sankey
# Plotly Express automatically determines nodes from source and target columns
# cspell:ignore sankey
fig2 = px.sankey(df,
                 path=['Source', 'Target'], # Defines the flow direction
                 values='Value',            # Specifies the link values
                 color='Color',             # Optional: Color links based on a column
                 title="Example 2: Sankey Diagram from DataFrame (Plotly Express)")

# fig2.show() # Uncomment to display the figure


# Example 3: More Complex Sankey with Custom Data and Layout using go.Sankey

# Data for a more complex flow (e.g., budget allocation)
labels = ["Revenue", "Expenses", "Salaries", "Marketing", "Operations", "Profit", "Taxes", "Net Profit"]
sources = [0, 0, 1, 1, 1, 5, 5] # Index of source node
targets = [1, 5, 2, 3, 4, 6, 7] # Index of target node
values =  [100, 20, 40, 25, 35, 5, 15] # Value of the flow

# Define node colors (optional)
node_colors = [
    "rgba(31, 119, 180, 0.8)",   # Revenue
    "rgba(255, 127, 14, 0.8)",   # Expenses
    "rgba(44, 160, 44, 0.8)",    # Salaries
    "rgba(214, 39, 40, 0.8)",    # Marketing
    "rgba(148, 103, 189, 0.8)",  # Operations
    "rgba(140, 86, 75, 0.8)",    # Profit
    "rgba(227, 119, 194, 0.8)",  # Taxes
    "rgba(127, 127, 127, 0.8)"   # Net Profit
]

# Define link colors (optional, can be based on source/target or custom)
link_colors = [
    "rgba(174, 199, 232, 0.6)", # Revenue -> Expenses
    "rgba(174, 199, 232, 0.6)", # Revenue -> Profit
    "rgba(255, 187, 120, 0.6)", # Expenses -> Salaries
    "rgba(255, 187, 120, 0.6)", # Expenses -> Marketing
    "rgba(255, 187, 120, 0.6)", # Expenses -> Operations
    "rgba(199, 199, 199, 0.6)", # Profit -> Taxes
    "rgba(199, 199, 199, 0.6)"  # Profit -> Net Profit
]


fig3 = go.Figure(data=[go.Sankey(
    arrangement = "snap", # Aligns nodes vertically
    node = dict(
      pad = 25,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label = labels,
      color = node_colors,
      # Example: Custom hover text for nodes
      # customdata = [1000, 100, 40, 25, 35, 20, 5, 15], # Example custom data
      # hovertemplate='Node %{label}<br />Total Value: %{customdata}<extra></extra>'
    ),
    link = dict(
      source = sources,
      target = targets,
      value = values,
      color = link_colors,
      # Example: Custom hover text for links
      # customdata = ["Info A", "Info B", "Info C", "Info D", "Info E", "Info F", "Info G"],
      # hovertemplate='Link from %{source.label} to %{target.label}<br />Value: %{value}<br />Info: %{customdata}<extra></extra>'
  ))])

fig3.update_layout(
    title_text="Example 3: Complex Sankey with Custom Layout",
    font=dict(size = 12, color = 'black'),
    # paper_bgcolor='lightsteelblue', # Example background color
)

# fig3.show() # Uncomment to display the figure

# --- Displaying all figures ---
# If you want to see all figures when running the script, uncomment the .show() lines above
# Or display them sequentially:
print("Displaying Figure 1: Basic Sankey")
fig1.show()
print("Displaying Figure 2: Sankey from DataFrame")
fig2.show()
print("Displaying Figure 3: Complex Sankey")
fig3.show()

print("Script finished.")
