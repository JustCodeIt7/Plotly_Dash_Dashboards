# %%
import plotly.graph_objects as go

################################ Basic Sankey Diagram ################################


# %%
# Generate and display a simple Sankey diagram with two sources and two targets.
def create_basic_sankey():
    # Create the Sankey diagram figure object.
    fig = go.Figure(
        data=[
            go.Sankey(
                # Define the nodes (vertical bars) of the diagram.
                node=dict(
                    pad=15,  # Set vertical padding between nodes.
                    thickness=20,  # Set the width of each node bar.
                    line=dict(
                        color="black", width=0.5
                    ),  # Define the node border style.
                    label=["Source A1", "Source A2", "Target B1", "Target B2"],
                    color="blue",  # Set a uniform color for all nodes.
                ),
                # Define the flows (links) between nodes.
                link=dict(
                    source=[0, 0, 1, 1],  # Map links to their starting nodes by index.
                    target=[
                        2,
                        3,
                        2,
                        3,
                    ],  # Map links to their destination nodes by index.
                    value=[8, 4, 4, 2],  # Define the thickness of each link.
                ),
            )
        ]
    )

    # Configure the chart's title and font size.
    fig.update_layout(title_text="Example 1: Basic Sankey Diagram", font_size=12)
    # Render the Sankey diagram.
    fig.show()


# %%
################################ Multi-Level Sankey Diagram ################################


# Generate a Sankey diagram with an intermediate stage between sources and targets.
def create_multilevel_sankey():
    # Create the Sankey diagram figure object.
    fig = go.Figure(
        data=[
            go.Sankey(
                # Define the nodes for each stage of the flow.
                node=dict(
                    pad=25,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=[
                        "Source A",
                        "Source B",
                        "Intermediate C",
                        "Intermediate D",
                        "Target E",
                        "Target F",
                    ],
                ),
                # Define the links connecting the sources, intermediate stage, and targets.
                link=dict(
                    source=[0, 1, 1, 2, 2, 3],
                    target=[2, 2, 3, 4, 5, 5],
                    value=[10, 5, 15, 8, 7, 15],
                ),
            )
        ]
    )

    # Configure the chart's title and font size.
    fig.update_layout(title_text="Example 2: Multi-Level Sankey Diagram", font_size=12)
    # Render the Sankey diagram.
    fig.show()


################################ Customized Sankey Diagram ################################


# %%
# Generate a Sankey with custom colors for nodes and links.
def create_customized_sankey():
    # Define the labels for each node in the diagram.
    labels = [
        "Coal",
        "Natural Gas",
        "Solar",
        "Electricity Grid",
        "Residential",
        "Industrial",
    ]

    # Define a unique color for each corresponding node.
    node_colors = [
        "rgba(102, 102, 102, 0.8)",  # Coal (grey)
        "rgba(25, 128, 180, 0.8)",  # Natural Gas (blue)
        "rgba(255, 185, 60, 0.8)",  # Solar (yellow)
        "rgba(60, 180, 75, 0.8)",  # Grid (green)
        "rgba(230, 25, 75, 0.8)",  # Residential (red)
        "rgba(145, 30, 180, 0.8)",  # Industrial (purple)
    ]

    # Define a color for each link, using transparency.
    link_colors = [
        "rgba(102, 102, 102, 0.4)",
        "rgba(25, 128, 180, 0.4)",
        "rgba(255, 185, 60, 0.4)",
        "rgba(60, 180, 75, 0.4)",
        "rgba(60, 180, 75, 0.4)",
    ]

    # Create the Sankey diagram figure object.
    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",  # Align nodes to a grid for a cleaner layout.
                # Define the nodes and apply custom colors.
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=labels,
                    color=node_colors,  # Apply the custom node colors.
                ),
                # Define the links and apply custom colors.
                link=dict(
                    source=[0, 1, 2, 3, 3],
                    target=[3, 3, 3, 4, 5],
                    value=[45, 30, 15, 50, 40],
                    color=link_colors,  # Apply the custom link colors.
                ),
            )
        ]
    )

    # Configure the chart's title and font size.
    fig.update_layout(
        title_text="Example 3: Customized Energy Flow Sankey", font_size=12
    )
    # Render the Sankey diagram.
    fig.show()


# %%
################################ Main Execution Block ################################

# Execute the functions to generate and display each Sankey diagram.
if __name__ == "__main__":
    print("Displaying Example 1: Basic Sankey Diagram...")
    create_basic_sankey()

    print("\nDisplaying Example 2: Multi-Level Sankey Diagram...")
    create_multilevel_sankey()

    print("\nDisplaying Example 3: Customized Sankey Diagram...")
    create_customized_sankey()

# %%
