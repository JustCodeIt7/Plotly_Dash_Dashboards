"""
Simplified Plotly Sankey Diagram Examples
==========================================

Three progressively complex Sankey diagram examples with clean, reusable code.

Requirements: pip install plotly pandas
"""

import plotly.graph_objects as go
import pandas as pd
from typing import List, Dict, Tuple


class SankeyBuilder:
    """Helper class to build Sankey diagrams with consistent styling."""

    def __init__(self, title: str, width: int = 800, height: int = 500):
        self.title = title
        self.width = width
        self.height = height
        self.nodes = []
        self.links = []

    def add_flow(self, source: str, target: str, value: float):
        """Add a flow between two nodes."""
        self.links.append({"source": source, "target": target, "value": value})

        # Collect unique nodes
        for node in [source, target]:
            if node not in self.nodes:
                self.nodes.append(node)

    def create_figure(self, node_colors: List[str] = None, link_opacity: float = 0.4) -> go.Figure:
        """Create the Sankey figure from collected data."""

        # Create node mapping
        node_map = {node: i for i, node in enumerate(self.nodes)}

        # Convert links to indices
        source_indices = [node_map[link["source"]] for link in self.links]
        target_indices = [node_map[link["target"]] for link in self.links]
        values = [link["value"] for link in self.links]

        # Default colors if none provided
        if node_colors is None:
            node_colors = [f"hsl({i * 360 // len(self.nodes)}, 70%, 60%)" for i in range(len(self.nodes))]

        # Create link colors with transparency
        link_colors = [f"rgba(100, 150, 200, {link_opacity})" for _ in values]

        fig = go.Figure(
            go.Sankey(
                node=dict(
                    pad=20,
                    thickness=25,
                    line=dict(color="black", width=1),
                    label=self.nodes,
                    color=node_colors[: len(self.nodes)],
                ),
                link=dict(source=source_indices, target=target_indices, value=values, color=link_colors),
            )
        )

        fig.update_layout(title_text=self.title, font_size=12, width=self.width, height=self.height)

        return fig


def create_basic_sankey() -> go.Figure:
    """Basic energy flow example - perfect for beginners."""

    builder = SankeyBuilder("Basic Sankey: Energy Flow", width=800, height=400)

    # Energy sources to electricity
    builder.add_flow("Coal", "Electricity", 50)
    builder.add_flow("Natural Gas", "Electricity", 30)
    builder.add_flow("Nuclear", "Electricity", 20)

    # Electricity to end uses
    builder.add_flow("Electricity", "Industry", 60)
    builder.add_flow("Electricity", "Residential", 40)

    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#DDA0DD", "#FFD93D"]

    return builder.create_figure(node_colors=colors)


def create_intermediate_sankey() -> go.Figure:
    """Manufacturing process with multiple transformation steps."""

    builder = SankeyBuilder("Intermediate Sankey: Manufacturing Process", width=1000, height=600)

    # Raw materials to processing
    raw_materials = ["Raw Material A", "Raw Material B", "Raw Material C"]
    processing_plants = ["Processing Plant 1", "Processing Plant 2"]

    flows = [
        ("Raw Material A", "Processing Plant 1", 40),
        ("Raw Material A", "Processing Plant 2", 20),
        ("Raw Material B", "Processing Plant 1", 35),
        ("Raw Material B", "Processing Plant 2", 15),
        ("Raw Material C", "Processing Plant 2", 25),
        # Processing to products
        ("Processing Plant 1", "Product X", 25),
        ("Processing Plant 1", "Product Y", 20),
        ("Processing Plant 1", "Waste", 10),
        ("Processing Plant 2", "Product Y", 30),
        ("Processing Plant 2", "Product Z", 20),
        ("Processing Plant 2", "Waste", 5),
        # Products to markets
        ("Product X", "Domestic Market", 15),
        ("Product X", "Export Market", 10),
        ("Product Y", "Domestic Market", 30),
        ("Product Y", "Export Market", 20),
        ("Product Z", "Export Market", 20),
    ]

    for source, target, value in flows:
        builder.add_flow(source, target, value)

    # Color scheme: materials=red, processing=teal, products=blue, markets=green, waste=purple
    colors = ["#FF6B6B"] * 3 + ["#4ECDC4"] * 2 + ["#45B7D1"] * 3 + ["#96CEB4"] * 2 + ["#DDA0DD"]

    return builder.create_figure(node_colors=colors, link_opacity=0.3)


def create_advanced_sankey() -> go.Figure:
    """Advanced business revenue flow with custom styling."""

    # Business revenue flow data
    flows = [
        # Revenue sources (in millions USD)
        ("Online Sales", "Operations", 250),
        ("Retail Stores", "Operations", 180),
        ("B2B Sales", "Operations", 120),
        ("Subscriptions", "Operations", 90),
        ("Partnerships", "Operations", 60),
        # Operations to cost centers and profit
        ("Operations", "Marketing", 150),
        ("Operations", "R&D", 80),
        ("Operations", "Admin", 100),
        ("Operations", "Sales", 120),
        ("Operations", "Gross Profit", 250),
        # Cost centers contribute to reinvestment
        ("Marketing", "Reinvestment", 40),
        ("R&D", "Reinvestment", 60),
        ("Admin", "Reinvestment", 20),
        ("Sales", "Reinvestment", 30),
        # Final profit distribution
        ("Gross Profit", "Net Profit", 100),
        ("Gross Profit", "Reinvestment", 80),
        ("Gross Profit", "Shareholders", 70),
    ]

    builder = SankeyBuilder("Advanced Sankey: Business Revenue Flow", width=1200, height=700)

    for source, target, value in flows:
        builder.add_flow(source, target, value)

    # Custom color scheme
    colors = [
        "#2E8B57",
        "#3CB371",
        "#90EE90",
        "#98FB98",
        "#00FA9A",  # Revenue - greens
        "#FF8C00",  # Operations - orange
        "#DC143C",
        "#B22222",
        "#CD5C5C",
        "#F08080",  # Costs - reds
        "#4169E1",
        "#1E90FF",
        "#00BFFF",  # Outcomes - blues
    ]

    fig = builder.create_figure(node_colors=colors, link_opacity=0.4)

    # Enhanced styling for advanced example
    fig.update_layout(
        title={
            "text": "Advanced Sankey: Business Revenue Flow Analysis",
            "x": 0.5,
            "font": {"size": 16, "color": "#2C3E50"},
        },
        font=dict(size=12, color="#34495E"),
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        margin=dict(l=50, r=50, t=80, b=50),
    )

    return fig


def create_sankey_from_dataframe(df: pd.DataFrame, source_col: str, target_col: str, value_col: str) -> go.Figure:
    """Create Sankey diagram from pandas DataFrame - great for real data."""

    builder = SankeyBuilder("Data-Driven Sankey: Customer Journey")

    for _, row in df.iterrows():
        builder.add_flow(row[source_col], row[target_col], row[value_col])

    return builder.create_figure()


def run_examples():
    """Run all Sankey diagram examples."""

    examples = [
        ("Basic", create_basic_sankey),
        ("Intermediate", create_intermediate_sankey),
        ("Advanced", create_advanced_sankey),
    ]

    figures = {}

    for name, func in examples:
        try:
            print(f"Creating {name} Sankey diagram...")
            fig = func()
            fig.show()
            figures[name] = fig
            print(f"✅ {name} diagram created successfully!")

        except Exception as e:
            print(f"❌ Error creating {name} diagram: {e}")

    # Bonus: DataFrame example
    try:
        print("\nCreating DataFrame-based Sankey...")
        sample_data = pd.DataFrame({
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
            "target": [
                "Leads",
                "Bounce",
                "Leads",
                "Bounce",
                "Leads",
                "Bounce",
                "Customers",
                "Lost",
                "Retained",
                "Churned",
            ],
            "value": [500, 1500, 300, 700, 200, 100, 400, 600, 320, 80],
        })

        df_fig = create_sankey_from_dataframe(sample_data, "source", "target", "value")
        df_fig.show()
        figures["DataFrame"] = df_fig
        print("✅ DataFrame diagram created successfully!")

    except Exception as e:
        print(f"❌ Error creating DataFrame diagram: {e}")

    return figures


if __name__ == "__main__":
    print("🎯 Simplified Plotly Sankey Diagram Examples")
    print("=" * 50)

    figures = run_examples()

    print(f"\n✅ Created {len(figures)} Sankey diagrams!")
    print("\n💡 Key improvements in this refactored version:")
    print("   • SankeyBuilder class eliminates code duplication")
    print("   • Cleaner data structure with simple tuples")
    print("   • Consistent styling across all examples")
    print("   • Better error handling and user feedback")
    print("   • Easy DataFrame integration for real data")
