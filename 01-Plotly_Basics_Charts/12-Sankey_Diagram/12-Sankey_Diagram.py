"""
Plotly Sankey Diagram Examples for YouTube Tutorial
===================================================

This file contains three progressively complex Sankey diagram examples:
1. Basic Sankey Diagram - Simple energy flow
2. Intermediate Sankey Diagram - Multi-step process flow
3. Advanced Sankey Diagram - Complex business process with styling

Requirements:
pip install plotly pandas
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# =============================================================================
# EXAMPLE 1: BASIC SANKEY DIAGRAM - Simple Energy Flow
# =============================================================================


def basic_sankey_diagram():
    """
    Basic Sankey diagram showing simple energy flow from sources to uses
    Perfect for beginners to understand the core concepts
    """
    print("Creating Basic Sankey Diagram...")

    # Define the nodes (sources and targets)
    node_labels = ["Coal", "Natural Gas", "Nuclear", "Electricity", "Industry", "Residential"]

    # Define the flows (source, target, value)
    # Source and target are indices of the node_labels list
    source = [0, 1, 2, 3, 3]  # Coal, Natural Gas, Nuclear, Electricity, Electricity
    target = [3, 3, 3, 4, 5]  # Electricity, Electricity, Electricity, Industry, Residential
    value = [50, 30, 20, 60, 40]  # Flow values

    # Create the basic Sankey diagram
    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(pad=15, thickness=20, line=dict(color="black", width=0.5), label=node_labels),
                link=dict(source=source, target=target, value=value),
            )
        ]
    )

    fig.update_layout(title_text="Basic Sankey Diagram: Energy Flow", font_size=12, width=800, height=400)

    fig.show()
    return fig


# =============================================================================
# EXAMPLE 2: INTERMEDIATE SANKEY DIAGRAM - Multi-step Process Flow
# =============================================================================


def intermediate_sankey_diagram():
    """
    Intermediate Sankey diagram showing a manufacturing process
    Includes more nodes and multiple transformation steps
    """
    print("Creating Intermediate Sankey Diagram...")

    # Manufacturing process: Raw Materials -> Processing -> Products -> Distribution
    node_labels = [
        "Raw Material A",
        "Raw Material B",
        "Raw Material C",  # 0, 1, 2
        "Processing Plant 1",
        "Processing Plant 2",  # 3, 4
        "Product X",
        "Product Y",
        "Product Z",  # 5, 6, 7
        "Domestic Market",
        "Export Market",
        "Waste",  # 8, 9, 10
    ]

    # Define more complex flows
    source = [0, 1, 2, 0, 1, 3, 3, 4, 4, 5, 6, 7, 5, 6, 3, 4]
    target = [3, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9, 10, 10]
    value = [40, 35, 25, 20, 15, 25, 20, 30, 20, 15, 20, 20, 10, 15, 10, 5]

    # Add colors to make it more visually appealing
    node_colors = [
        "#FF6B6B",
        "#FF6B6B",
        "#FF6B6B",  # Raw materials - red
        "#4ECDC4",
        "#4ECDC4",  # Processing - teal
        "#45B7D1",
        "#45B7D1",
        "#45B7D1",  # Products - blue
        "#96CEB4",
        "#96CEB4",
        "#DDA0DD",  # Markets - green, Waste - purple
    ]

    link_colors = ["rgba(70, 181, 209, 0.4)" for _ in range(len(source))]

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=20, thickness=25, line=dict(color="black", width=1), label=node_labels, color=node_colors
                ),
                link=dict(source=source, target=target, value=value, color=link_colors),
            )
        ]
    )

    fig.update_layout(
        title_text="Intermediate Sankey: Manufacturing Process Flow", font_size=11, width=1000, height=600
    )

    fig.show()
    return fig


# =============================================================================
# EXAMPLE 3: ADVANCED SANKEY DIAGRAM - Complex Business Process
# =============================================================================


def advanced_sankey_diagram():
    """
    Advanced Sankey diagram with custom styling, hover info, and complex data
    Shows a complete business revenue flow with multiple revenue streams
    """
    print("Creating Advanced Sankey Diagram...")

    # Complex business revenue flow
    revenue_data = {
        "source": [
            # Revenue Sources (0-4)
            "Online Sales",
            "Retail Stores",
            "B2B Sales",
            "Subscriptions",
            "Partnerships",
            # Cost Centers (5-9)
            "Operations",
            "Marketing",
            "R&D",
            "Admin",
            "Sales",
            # Final Categories (10-12)
            "Net Profit",
            "Reinvestment",
            "Shareholders",
        ]
    }

    # Create a more realistic business flow
    source_indices = [
        # Revenue to Operations
        0,
        1,
        2,
        3,
        4,  # All revenue sources to operations
        # Operations to cost centers
        5,
        5,
        5,
        5,
        5,  # Operations to all cost centers
        # Cost centers to final outcomes
        6,
        7,
        8,
        9,  # Some costs to reinvestment
        5,
        5,
        5,  # Remaining operations to profit categories
    ]

    target_indices = [
        # Revenue to Operations
        5,
        5,
        5,
        5,
        5,  # All to operations
        # Operations to cost centers
        6,
        7,
        8,
        9,
        10,  # To marketing, R&D, admin, sales, net profit
        # Cost centers to outcomes
        11,
        11,
        11,
        11,  # To reinvestment
        10,
        11,
        12,  # To net profit, reinvestment, shareholders
    ]

    values = [
        # Revenue flows
        250,
        180,
        120,
        90,
        60,  # Revenue sources
        # Cost allocations
        150,
        120,
        80,
        100,
        250,  # Operations to costs and profit
        # Final allocations
        40,
        30,
        25,
        35,  # Costs to reinvestment
        100,
        80,
        70,  # Final profit distribution
    ]

    # Custom colors for different categories
    node_colors = [
        # Revenue sources - Green shades
        "#2E8B57",
        "#3CB371",
        "#90EE90",
        "#98FB98",
        "#00FA9A",
        # Operations - Orange
        "#FF8C00",
        # Cost centers - Red shades
        "#DC143C",
        "#B22222",
        "#CD5C5C",
        "#F08080",
        # Final outcomes - Blue shades
        "#4169E1",
        "#1E90FF",
        "#00BFFF",
    ]

    # Create custom link colors based on value
    max_value = max(values)
    link_colors = []
    for val in values:
        intensity = val / max_value
        alpha = 0.3 + (intensity * 0.4)  # Alpha between 0.3 and 0.7
        link_colors.append(f"rgba(70, 130, 180, {alpha})")

    # Custom hover text
    hover_text = [f"Flow: {val}M USD" for val in values]

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=25,
                    thickness=30,
                    line=dict(color="black", width=2),
                    label=revenue_data["source"],
                    color=node_colors,
                    hovertemplate="%{label}<br>Total: %{value}M USD<extra></extra>",
                ),
                link=dict(
                    source=source_indices,
                    target=target_indices,
                    value=values,
                    color=link_colors,
                    hovertemplate="%{source.label} → %{target.label}<br>Amount: %{value}M USD<extra></extra>",
                ),
            )
        ]
    )

    # Advanced layout with annotations
    fig.update_layout(
        title={
            "text": "Advanced Sankey: Business Revenue Flow Analysis",
            "x": 0.5,
            "xanchor": "center",
            "font": {"size": 16, "color": "#2C3E50"},
        },
        font=dict(size=12, color="#34495E"),
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        width=1200,
        height=700,
        margin=dict(l=50, r=50, t=80, b=50),
    )

    # Add annotations for better explanation
    fig.add_annotation(
        x=0.02,
        y=0.98,
        text="Revenue Sources",
        showarrow=False,
        font=dict(size=14, color="#2E8B57", weight="bold"),
        xref="paper",
        yref="paper",
    )

    fig.add_annotation(
        x=0.98,
        y=0.98,
        text="Final Outcomes",
        showarrow=False,
        font=dict(size=14, color="#4169E1", weight="bold"),
        xref="paper",
        yref="paper",
    )

    fig.show()
    return fig


# =============================================================================
# BONUS: DATA-DRIVEN SANKEY FROM CSV/DATAFRAME
# =============================================================================


def create_sankey_from_data():
    """
    Bonus example: Create Sankey diagram from pandas DataFrame
    Useful for real-world data analysis
    """
    print("Creating Data-Driven Sankey Diagram...")

    # Sample data that might come from a CSV file
    flow_data = pd.DataFrame({
        "source": [
            "Website",
            "Website",
            "Social Media",
            "Social Media",
            "Email",
            "Email",
            "Leads",
            "Leads",
            "Customers",
            "Customers",
        ],
        "target": ["Leads", "Bounce", "Leads", "Bounce", "Leads", "Bounce", "Customers", "Lost", "Retained", "Churned"],
        "value": [500, 1500, 300, 700, 200, 100, 400, 600, 320, 80],
    })

    # Get unique nodes
    all_nodes = list(pd.concat([flow_data["source"], flow_data["target"]]).unique())

    # Create mapping from node names to indices
    node_mapping = {node: i for i, node in enumerate(all_nodes)}

    # Convert source and target to indices
    source_indices = [node_mapping[source] for source in flow_data["source"]]
    target_indices = [node_mapping[target] for target in flow_data["target"]]

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=all_nodes,
                    color=[
                        "#FF9999",
                        "#66B2FF",
                        "#99FF99",
                        "#FFCC99",
                        "#FF99CC",
                        "#99CCFF",
                        "#FFB366",
                        "#B3B3FF",
                        "#66FFB2",
                        "#FFD700",
                    ],
                ),
                link=dict(source=source_indices, target=target_indices, value=flow_data["value"].tolist()),
            )
        ]
    )

    fig.update_layout(title_text="Data-Driven Sankey: Customer Journey Analysis", font_size=12, width=900, height=500)

    fig.show()
    return fig


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🎯 Plotly Sankey Diagram Tutorial Examples")
    print("=" * 50)

    # Run all examples
    try:
        print("\n1️⃣ Running Basic Example...")
        basic_fig = basic_sankey_diagram()

        print("\n2️⃣ Running Intermediate Example...")
        intermediate_fig = intermediate_sankey_diagram()

        print("\n3️⃣ Running Advanced Example...")
        advanced_fig = advanced_sankey_diagram()

        print("\n🎁 Bonus: Data-Driven Example...")
        data_fig = create_sankey_from_data()

        print("\n✅ All Sankey diagrams created successfully!")
        print("\n💡 Tips for your YouTube tutorial:")
        print("   - Start with the basic example to explain core concepts")
        print("   - Show how to add colors and styling with the intermediate example")
        print("   - Demonstrate advanced features like hover text and annotations")
        print("   - Include the data-driven example for real-world applications")

    except Exception as e:
        print(f"❌ Error creating diagrams: {e}")
        print("Make sure you have plotly installed: pip install plotly pandas")
