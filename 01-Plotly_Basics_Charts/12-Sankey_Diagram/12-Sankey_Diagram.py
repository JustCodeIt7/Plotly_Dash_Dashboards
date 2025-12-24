# %% [markdown]
# # Plotly Sankey Diagram
# 

# %%
import plotly.graph_objects as go

# %% [markdown]
# ## Example 1: Basic Sankey Diagram
# 
# This opening example keeps the structure simple with two source nodes feeding two targets. It's useful for introducing how link thickness represents the magnitude of each flow and how Plotly handles basic Sankey configuration.
# - A Sankey diagram is a flow diagram where arrow (link) width is proportional to the amount of flow.
# - It shows movement between stages or entities (e.g., energy, materials, money).
# - Built from nodes (sources/targets, often rectangles/labels) and links/arrows (the flows).
# - Best for visualizing resource distribution, energy loss, supply chains, and user journeys.
# - Link thickness indicates magnitude, making the biggest transfers immediately obvious.
# - Named after Captain Matthew Henry Phineas Riall Sankey.
# - Common uses include energy management, marketing/analytics, and economics.

# %%
# Generate and display a simple Sankey diagram with two sources and two targets.
def create_basic_sankey():
    # Define the nodes (the vertical bars).
    # Each node is identified by its index in the 'label' list (0, 1, 2, 3).
    node_data = dict(
        pad=15,  # Vertical padding between nodes in the same column.
        thickness=20,  # Horizontal width of the node bars.
        line=dict(color="red", width=0.5),  # Border around the nodes.
        label=["Source A1", "Source A2", "Target B1", "Target B2"], # Node names.
        color="blue",  # Uniform color for all nodes.
    )

    # Define the links (the flows between nodes).
    link_data = dict(
        # 'source' and 'target' use the indices of the labels defined above.
        # e.g., source 0 is "Source A1", target 2 is "Target B1".
        source=[0, 0, 1, 1],  # Starting node indices for each flow.
        target=[2, 3, 2, 3],  # Ending node indices for each flow.
        value=[8, 4, 4, 2],   # The volume/magnitude of each flow (determines thickness).
    )

    # Create the Sankey trace using the node and link definitions.
    sankey_trace = go.Sankey(
        node=node_data,
        link=link_data,
    )

    # Initialize the figure with the Sankey trace.
    fig = go.Figure(data=[sankey_trace])

    # Update layout settings like title and font.
    fig.update_layout(title_text="Example 1: Basic Sankey Diagram", font_size=12)
    
    # Display the interactive plot.
    fig.show()

create_basic_sankey()

# %% [markdown]
# ## Example 2: Multi-Level Sankey Diagram
# 
# This version adds an intermediate stage so you can trace how volume moves from multiple inputs, through transit nodes, and into final destinations. It's handy for highlighting branching and convergence across different levels in a process.
# 

# %%
################################ Multi-Level Sankey Diagram ################################

# Generate a Sankey diagram with an intermediate stage between sources and targets.
def create_multilevel_sankey():
    # Define nodes for three levels: Source -> Intermediate -> Target.
    # Indices: 0,1 (Sources) | 2,3 (Intermediate) | 4,5 (Targets)
    node_data = dict(
        pad=25, # Increased padding for better separation.
        thickness=20,
        line=dict(color="black", width=0.5),
        label=[
            "Source A",      # Index 0
            "Source B",      # Index 1
            "Intermediate C", # Index 2
            "Intermediate D", # Index 3
            "Target E",      # Index 4
            "Target F",      # Index 5
        ],
    )

    # Define links that connect across the three levels.
    link_data = dict(
        # Flows: A->C, B->C, B->D, C->E, C->F, D->F
        source=[0, 1, 1, 2, 2, 3, 3], # Source indices
        target=[2, 2, 3, 4, 5, 5, 4], # Target indices
        value=[10, 5, 15, 8, 7, 15, ], # Flow volumes
    )

    # Initialize the Sankey object.
    sankey_trace = go.Sankey(
        node=node_data,
        link=link_data,
    )

    # Create the figure.
    fig = go.Figure(data=[sankey_trace])

    # Set the title and font size.
    fig.update_layout(title_text="Example 2: Multi-Level Sankey Diagram", font_size=12)
    
    # Render the diagram.
    fig.show()

################################ Customized Sankey Diagram ################################


create_multilevel_sankey()

# %% [markdown]
# ## Example 3: Customized Energy Flow Sankey
# 
# Here the focus is on styling: distinct node colors identify each energy type while translucent links keep the diagram legible. Use this pattern when you need to clarify categories or emphasize specific pathways with custom palettes.
# 

# %%
# Generate a Sankey with custom colors for nodes and links.
def create_customized_sankey():
    # Define labels for energy sources, the grid, and end-use sectors.
    labels = [
        "Coal",             # 0
        "Natural Gas",      # 1
        "Solar",            # 2
        "Electricity Grid", # 3
        "Residential",      # 4
        "Industrial",       # 5
    ]

    # Define custom colors for each node using RGBA (Red, Green, Blue, Alpha/Transparency).
    # Alpha 0.8 makes the nodes slightly translucent.
    node_colors = [
        "rgba(102, 102, 102, 0.8)",  # Coal (grey)
        "rgba(25, 128, 180, 0.8)",  # Natural Gas (blue)
        "rgba(255, 185, 60, 0.8)",  # Solar (yellow)
        "rgba(60, 180, 75, 0.8)",   # Grid (green)
        "rgba(230, 25, 75, 0.8)",   # Residential (red)
        "rgba(145, 30, 180, 0.8)",  # Industrial (purple)
    ]

    # Define colors for the links. 
    # Using a lower Alpha (0.4) makes the links more transparent than the nodes.
    link_colors = [
        "rgba(102, 102, 102, 0.4)", # Coal to Grid
        "rgba(25, 128, 180, 0.4)",  # Gas to Grid
        "rgba(255, 185, 60, 0.4)",  # Solar to Grid
        "rgba(60, 180, 75, 0.4)",   # Grid to Residential
        "rgba(60, 180, 75, 0.4)",   # Grid to Industrial
    ]

    node_data = dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=node_colors,  # Apply the custom node colors list.
    )

    link_data = dict(
        source=[0, 1, 2, 3, 3], # Indices of starting nodes.
        target=[3, 3, 3, 4, 5], # Indices of ending nodes.
        value=[45, 30, 15, 50, 40], # Flow values.
        color=link_colors,  # Apply the custom link colors list.
    )

    sankey_trace = go.Sankey(
        # 'arrangement' controls how nodes are positioned. 
        # "snap" helps align nodes to a grid for a cleaner look.
        arrangement="snap",  
        node=node_data,
        link=link_data,
    )

    fig = go.Figure(data=[sankey_trace])

    # Configure the chart's title and font size.
    fig.update_layout(
        title_text="Example 3: Customized Energy Flow Sankey", font_size=12
    )
    
    # Render the Sankey diagram.
    fig.show()
create_customized_sankey()



# %%
