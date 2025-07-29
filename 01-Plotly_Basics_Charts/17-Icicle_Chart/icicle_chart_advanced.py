import plotly.graph_objects as go

# Data representing a file system structure
labels = ["Root", "Folder A", "Folder B", "File 1", "File 2", "Subfolder A", "File 3", "File 4"]
parents = ["", "Root", "Root", "Folder A", "Folder A", "Folder B", "Subfolder A", "Folder B"]

# Create an icicle chart using graph_objects for more control
# This approach is useful when you have a parent-child relationship defined in your data.
fig = go.Figure(go.Icicle(
    labels=labels,
    parents=parents,
    root_color="lightgrey"  # Set a distinct color for the root node
))

# Update the layout to provide a clear title and remove margins
fig.update_layout(
    title="File System Hierarchy",
    margin=dict(t=50, l=25, r=25, b=25)
)

# Show the plot
fig.show()
