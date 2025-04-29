# Sankey Diagram Tutorial
# This script demonstrates how to create Sankey diagrams in Plotly
# Author: James (YouTube Tutorial)
# Date: April 29, 2025

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# -------------------------------------------------------------------------------
# EXAMPLE 1: Basic Sankey Diagram using Plotly Graph Objects
# -------------------------------------------------------------------------------
print("EXAMPLE 1: Basic Sankey Diagram")

# Define nodes
label_nodes = ["Oil", "Natural Gas", "Coal", 
               "Electricity", "Energy", 
               "Residential", "Commercial", "Industrial", "Transportation"]

# Define links (source, target, value)
source_indices = [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4]
target_indices = [3, 4, 3, 4, 3, 4, 5, 6, 7, 5, 6, 8]
link_values = [5, 10, 8, 12, 3, 7, 9, 6, 15, 10, 8, 12]

# Create a custom color palette for sources
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
link_colors = [colors[src] for src in source_indices[:5]]  # Color by source

# Create the Sankey diagram
fig1 = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=label_nodes,
        color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
               '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=link_values,
        color=link_colors + ['rgba(211, 211, 211, 0.5)'] * 7,  # Use light gray for the rest
    )
)])

# Update layout
fig1.update_layout(
    title_text="Energy Flow Sankey Diagram",
    font_size=14,
    height=600,
    width=800
)

# Show the plot
fig1.show()

# -------------------------------------------------------------------------------
# EXAMPLE 2: Sankey Diagram from DataFrame with Custom Styling
# -------------------------------------------------------------------------------
print("\nEXAMPLE 2: Sankey Diagram from DataFrame")

# Create a DataFrame for a product sales flow
df = pd.DataFrame([
    # Source, Target, Value
    ["Product A", "North America", 100],
    ["Product A", "Europe", 80],
    ["Product A", "Asia", 60],
    ["Product B", "North America", 70],
    ["Product B", "Europe", 90],
    ["Product B", "Asia", 110],
    ["Product C", "North America", 50],
    ["Product C", "Europe", 40],
    ["Product C", "Asia", 30],
    ["North America", "Direct", 120],
    ["North America", "Retail", 100],
    ["Europe", "Direct", 80], 
    ["Europe", "Retail", 130],
    ["Asia", "Direct", 60],
    ["Asia", "Retail", 140],
])

# Rename columns for clarity
df.columns = ['source', 'target', 'value']

# Get unique nodes
all_nodes = sorted(list(set(df['source'].unique().tolist() + df['target'].unique().tolist())))

# Map node names to indices
source_indices = [all_nodes.index(source) for source in df['source']]
target_indices = [all_nodes.index(target) for target in df['target']]

# Create color scheme by node type (product, region, sales channel)
product_color = '#66c2a5'
region_color = '#fc8d62'
channel_color = '#8da0cb'

node_colors = []
for node in all_nodes:
    if node in ["Product A", "Product B", "Product C"]:
        node_colors.append(product_color)
    elif node in ["North America", "Europe", "Asia"]:
        node_colors.append(region_color)
    else:  # Sales channels
        node_colors.append(channel_color)

# Create the Sankey diagram
fig2 = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=all_nodes,
        color=node_colors
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=df['value'].tolist(),
        # Color links based on source node color with some transparency
        color=[f"rgba{tuple(int(c.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (0.5,)}" 
               for c in [node_colors[i] for i in source_indices]]
    )
)])

# Update layout
fig2.update_layout(
    title_text="Product Sales Flow by Region and Channel",
    font_size=14,
    height=600,
    width=800
)

# Show the plot
fig2.show()

# -------------------------------------------------------------------------------
# EXAMPLE 3: Complex Sankey with Hover Information
# -------------------------------------------------------------------------------
print("\nEXAMPLE 3: Complex Sankey with Hover Information")

# Create data for a website user flow
sources = []
targets = []
values = []
labels = []
hovers = []

# Add flow data: Homepage -> various pages
pages = ['Home', 'Products', 'Blog', 'About', 'Contact', 'Cart', 'Checkout', 'Thank You', 'Exit']
page_indices = {page: i for i, page in enumerate(pages)}

# Track data for home page connections
sources.extend([page_indices['Home']] * 5)
targets.extend([page_indices[p] for p in ['Products', 'Blog', 'About', 'Contact', 'Exit']])
values.extend([1000, 750, 400, 300, 550])  # Number of users flowing to each page
hovers.extend([f"{v} users" for v in [1000, 750, 400, 300, 550]])

# Products page connections
sources.extend([page_indices['Products']] * 3)
targets.extend([page_indices[p] for p in ['Cart', 'Home', 'Exit']])
values.extend([350, 250, 400])
hovers.extend([f"{v} users" for v in [350, 250, 400]])

# Blog page connections
sources.extend([page_indices['Blog']] * 3)
targets.extend([page_indices[p] for p in ['Products', 'Home', 'Exit']])
values.extend([200, 300, 250])
hovers.extend([f"{v} users" for v in [200, 300, 250]])

# About page connections
sources.extend([page_indices['About']] * 3)
targets.extend([page_indices[p] for p in ['Contact', 'Home', 'Exit']])
values.extend([100, 150, 150])
hovers.extend([f"{v} users" for v in [100, 150, 150]])

# Contact page connections
sources.extend([page_indices['Contact']] * 2)
targets.extend([page_indices[p] for p in ['Home', 'Exit']])
values.extend([150, 150])
hovers.extend([f"{v} users" for v in [150, 150]])

# Cart page connections
sources.extend([page_indices['Cart']] * 3)
targets.extend([page_indices[p] for p in ['Checkout', 'Products', 'Exit']])
values.extend([200, 50, 100])
hovers.extend([f"{v} users" for v in [200, 50, 100]])

# Checkout page connections
sources.extend([page_indices['Checkout']] * 2)
targets.extend([page_indices[p] for p in ['Thank You', 'Exit']])
values.extend([180, 20])
hovers.extend([f"{v} users" for v in [180, 20]])

# Thank You page connections
sources.extend([page_indices['Thank You']] * 2)
targets.extend([page_indices[p] for p in ['Home', 'Exit']])
values.extend([100, 80])
hovers.extend([f"{v} users" for v in [100, 80]])

# Define custom node colors by page type
node_colors = [
    '#3366CC',  # Home - blue
    '#DC3912',  # Products - red
    '#FF9900',  # Blog - orange
    '#109618',  # About - green
    '#990099',  # Contact - purple
    '#0099C6',  # Cart - teal
    '#DD4477',  # Checkout - pink
    '#66AA00',  # Thank You - lime
    '#B82E2E',  # Exit - dark red
]

# Create the figure with custom hover text
fig3 = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=pages,
        color=node_colors
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        # Color links based on source
        color=[f"rgba{tuple(int(node_colors[src][1:][i:i+2], 16) for i in (0, 2, 4)) + (0.5,)}" 
               for src in sources],
        hovertemplate='%{source.label} → %{target.label}<br>' +
                      'Flow: %{value}<br>' +
                      'Custom info: %{customdata}<extra></extra>',
        customdata=hovers
    )
)])

# Update layout with annotations
fig3.update_layout(
    title_text="Website User Flow Analysis",
    font_size=14,
    height=700,
    width=900,
    annotations=[
        dict(
            x=0.5,
            y=-0.1,
            xref="paper",
            yref="paper",
            text="Visualizing how users navigate through the website",
            showarrow=False,
            font=dict(size=14)
        )
    ]
)

# Show the plot
fig3.show()

# -------------------------------------------------------------------------------
# Summary information for all three examples
# -------------------------------------------------------------------------------
print("\nSANKEY DIAGRAM TUTORIAL SUMMARY:")
print("Example 1: Basic Sankey diagram using Plotly Graph Objects")
print("Example 2: Sankey diagram from DataFrame with custom styling")
print("Example 3: Complex Sankey with hover information and user flow analysis")
print("\nPlotly Sankey diagrams are great for visualizing flows between nodes,")
print("such as energy transfers, website navigation, or product sales channels.")