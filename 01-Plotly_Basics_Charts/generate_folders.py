import os

# List of folder names
folders = [
    "01-scatter_plot",
    "02-line_chart",
    "03-bar_chart",
    "04-pie_chart",
    "05-bubble_chart",
    "06-dot_plot",
    "07-filled_area_plot",
    "08-horizontal_bar_chart",
    "09-gantt_chart",
    "10-sunburst_chart",
    "11-table",
    "12-sankey_diagram",
    "13-treemap_chart",
    "14-webgl_vs_svg",
    "15-figure_factory_table",
    "16-categorical_axes",
    "17-icicle_chart",
    "18-patterns_hatching_texture",
    "19-dumbbell_plot"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Folders created successfully!")
