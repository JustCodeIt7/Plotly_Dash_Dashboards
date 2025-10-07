import plotly.graph_objects as go

fig = go.Figure()

# First trace: Hover on points + fills
fig.add_trace(
    go.Scatter(
        x=[0, 0.5, 1, 1.5, 2],
        y=[0, 1, 2, 1, 0],
        fill="tozeroy",
        fillcolor="rgba(0,100,80,0.2)",
        hoveron="points+fills",  # Hover on both points and fills
        line_color="rgb(0,100,80)",
        name="Points + Fills",
        text="Hover works everywhere",
        hoverinfo="text+x+y",
    )
)

# Second trace: Hover only on points (default)
fig.add_trace(
    go.Scatter(
        x=[3, 3.5, 4, 4.5, 5],
        y=[0, 1, 2, 1, 0],
        fill="tozeroy",
        fillcolor="rgba(0,176,246,0.2)",
        hoveron="points",  # Hover only on points
        line_color="rgb(0,176,246)",
        name="Points Only",
        text="Hover only on points",
        hoverinfo="text+x+y",
    )
)

fig.update_layout(title="Hover Behavior Comparison", xaxis_range=[0, 5.2], yaxis_range=[0, 3])

fig.show()
