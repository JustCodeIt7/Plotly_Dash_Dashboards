# %%
import plotly.express as px
import pandas as pd
import numpy as np

# Pros:
# Space Efficiency: They're incredibly efficient at showing hierarchical data in a compact space. You can display hundreds of data points without scrolling or multiple pages.
# Dual Encoding: You can show two metrics simultaneously - size represents one variable (like revenue) while color represents another (like profit margin).

# Cons:
# - Limited Detail: While Treemaps show hierarchical relationships, they can obscure individual data points.
# - Not Ideal for Small Values: Small segments may be hard to see or interpret.
# - Terrible for Temporal Data: Treemaps are not suitable for showing changes over time.

# Usage:
# Financial Services - Visualizing portfolio allocations, risk assessments, or financial hierarchies.
# CS - Disk usage, file system structures, or software component hierarchies.
# Marketing - Campaign performance across different segments or product categories.
# Healthcare - Patient demographics, treatment outcomes, or resource allocations.

# %%
################################ Example 1: Basic Treemap ################################
print("Generating Example 1: Basic Treemap of Tips Data")


# %%
################################ Example 2: Colored Treemap ################################
print("\nGenerating Example 2: Treemap of Global Population (2007)")


# %%
################################ Example 3: Custom Data Treemap ################################
print("\nGenerating Example 3: Treemap of Custom Sales Data")


# %%
