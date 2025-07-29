#%%
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({
    "country": ["Japan", "Germany", "Brazil", "Nigeria"],
    "y1960": [67.8, 69.3, 54.9, 37.2],
    "y2020": [84.6, 81.3, 75.9, 54.7],
})

fig = go.Figure()
for _, row in df.iterrows():
    fig.add_trace(
        go.Scatter(
            x=[row["y1960"], row["y2020"]],
            y=[row["country"], row["country"]],
            mode="lines+markers",
            line=dict(color="slategray", width=4),
            marker=dict(size=10, color=["tomato", "seagreen"]),
            showlegend=False,
        )
    )

fig.update_layout(
    title="Life expectancy 1960 → 2020", xaxis_title="Years", height=250, margin=dict(l=80, r=30, t=50, b=30)
)
fig.show()
# %%
scores = pd.DataFrame({
    "student": ["Alice", "Bob", "Carla", "David"],
    "before": [55, 60, 65, 50],
    "after": [70, 75, 80, 65],
})

fig = go.Figure()
for _, row in scores.iterrows():
    fig.add_trace(
        go.Scatter(
            y=[row["before"], row["after"]],
            x=[row["student"], row["student"]],
            mode="lines+markers",
            line=dict(color="black", width=2.5),
            marker=dict(size=11, color=["crimson", "navy"]),
            showlegend=False,
        )
    )

fig.update_layout(
    title="Pre-test vs Post-test scores", yaxis_title="Score", height=400, margin=dict(l=50, r=30, t=60, b=60)
)
fig.show()
# %%
import plotly.graph_objects as go
import pandas as pd

# ---- aggregated survival data ----
df = pd.DataFrame({
    "Pclass": ["1st class", "2nd class", "3rd class"] * 2,
    "Sex": ["female", "female", "female", "male", "male", "male"],
    "share": [96, 89, 50, 37, 17, 14],
})

pclass = ["1st class", "2nd class", "3rd class"]  # top→bottom
line_x, line_y, female, male = [], [], [], []

for p in pclass:
    f = df.loc[(df.Sex == "female") & (df.Pclass == p), "share"].values[0]
    m = df.loc[(df.Sex == "male") & (df.Pclass == p), "share"].values[0]
    female.append(f)
    male.append(m)
    line_x.extend([f, m, None])
    line_y.extend([p, p, None])

fig = go.Figure()
fig.add_trace(go.Scatter(x=line_x, y=line_y, mode="lines", line=dict(color="#85868a", width=3), showlegend=False))

fig.add_trace(
    go.Scatter(
        x=female,
        y=pclass,
        mode="markers",
        marker_symbol="circle",
        marker_size=12,
        marker_color="#1e5f97",
        name="female",
    )
)

fig.add_trace(
    go.Scatter(
        x=male, y=pclass, mode="markers", marker_symbol="circle", marker_size=12, marker_color="#abaa9c", name="male"
    )
)

fig.update_layout(
    title="<b>Titanic survival rate by class & sex</b>",
    xaxis_title="Survival %",
    height=300,
    margin=dict(l=120, r=40, t=60, b=40),
    showlegend=True,
)
fig.show()
# %%
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# --------------------------------------------------------------------------------
# Example 1: Basic Dumbbell Plot
# This example creates a simple dumbbell plot comparing scores for different
# teams between two years. It establishes the fundamental pattern:
# 1. Melt the data into a long format.
# 2. Use px.line() to draw the connecting lines.
# 3. Use fig.add_trace(go.Scatter()) to add the markers ("bells").
# --------------------------------------------------------------------------------
print("--- Running Example 1: Basic Dumbbell Plot ---")

# 1. Create the DataFrame
df1 = pd.DataFrame({
    "Category": ["Team A", "Team B", "Team C", "Team D", "Team E"],
    "Value_2023": [85, 91, 78, 88, 72],
    "Value_2024": [92, 88, 85, 95, 80],
})

# 2. Melt the DataFrame to a long format suitable for Plotly Express
df1_long = df1.melt(id_vars="Category", value_vars=["Value_2023", "Value_2024"], var_name="Year", value_name="Value")

# 3. Create the plot
# First, draw the connecting lines for each category
fig1 = px.line(
    df1_long,
    x="Value",
    y="Category",
    color="Category",  # Use category for color to ensure separate lines
    orientation="h",  # Horizontal orientation
    title="Team Performance Comparison: 2023 vs. 2024",
)

# Second, add the dots (the "bells") to the ends of the lines
# We use go.Scatter for more control, added via fig.add_trace
fig1.add_trace(
    go.Scatter(
        x=df1_long["Value"],
        y=df1_long["Category"],
        mode="markers",
        marker=dict(color="darkslateblue", size=12),
        showlegend=False,  # Hide this trace from the legend
    )
)

# 4. Customize layout
fig1.update_layout(showlegend=False, yaxis_title=None, xaxis_title="Score")
fig1.show()

# %%
# --------------------------------------------------------------------------------
# Example 2: Grouped Dumbbell Plot with Categorical Colors
# This example uses the `gapminder` dataset to compare life expectancy
# between 1952 and 2007. The dumbbells are colored by continent,
# demonstrating how to group the data visually.
# --------------------------------------------------------------------------------
print("\n--- Running Example 2: Grouped Dumbbell Plot ---")

# 1. Load and filter the gapminder data
df_gap = px.data.gapminder()
df_compare = df_gap[df_gap["year"].isin([1952, 2007])]

# For clarity, let's focus on countries in the Americas
df_americas = df_compare[df_compare["continent"] == "Americas"]

# 2. Create the plot
# Draw the connecting lines, colored by country this time for visual distinction
fig2 = px.line(
    df_americas,
    x="lifeExp",
    y="country",
    color="country",  # Color lines by country
    orientation="h",
    title="Change in Life Expectancy in the Americas (1952 vs. 2007)",
    labels={"lifeExp": "Life Expectancy (Years)", "country": "Country"},
)

# Add the markers (bells). We can use the same color mapping by iterating
# through the data in the original figure.
fig2.add_trace(
    go.Scatter(
        x=df_americas["lifeExp"],
        y=df_americas["country"],
        mode="markers",
        marker=dict(
            color="black",  # Use a single, neutral color for the markers
            size=10,
            line=dict(width=1, color="DarkSlateGrey"),  # Add a border to markers
        ),
        showlegend=False,
    )
)

# 3. Customize layout
fig2.update_layout(
    showlegend=False,
    yaxis={"categoryorder": "total ascending"},  # Sort countries by life expectancy
)
fig2.show()

# %%
# --------------------------------------------------------------------------------
# Example 3: Styled Dumbbell Plot with Custom Hover Data
# This example compares male and female participation in different activities.
# It showcases more advanced styling, including custom colors, different
# marker symbols for each point, and richer hover information.
# --------------------------------------------------------------------------------
print("\n--- Running Example 3: Styled Dumbbell Plot ---")

# 1. Create the DataFrame
df3 = pd.DataFrame([
    dict(Activity="Reading", Female=34, Male=25),
    dict(Activity="Writing", Female=28, Male=32),
    dict(Activity="Coding", Female=19, Male=40),
    dict(Activity="Designing", Female=43, Male=31),
    dict(Activity="Exercising", Female=25, Male=38),
])

# 2. Melt the DataFrame
df3_long = df3.melt(id_vars=["Activity"], value_vars=["Female", "Male"], var_name="Gender", value_name="Hours")

# 3. Create the plot
# We will build this plot from scratch using go.Scatter for maximum control

# Create a figure object
fig3 = go.Figure()

# Add a line trace for each activity
for activity in df3["Activity"]:
    df_activity = df3[df3["Activity"] == activity]
    fig3.add_trace(
        go.Scatter(
            x=[df_activity["Male"].iloc[0], df_activity["Female"].iloc[0]],
            y=[activity, activity],
            mode="lines",
            line=dict(color="lightgray", width=2),
            showlegend=False,
        )
    )

# Add a scatter trace for the 'Male' points
fig3.add_trace(
    go.Scatter(
        x=df3["Male"],
        y=df3["Activity"],
        mode="markers",
        name="Male",
        marker=dict(color="#1f77b4", size=15, symbol="circle"),
    )
)

# Add a scatter trace for the 'Female' points
fig3.add_trace(
    go.Scatter(
        x=df3["Female"],
        y=df3["Activity"],
        mode="markers",
        name="Female",
        marker=dict(color="#ff7f0e", size=15, symbol="diamond"),
    )
)

# 4. Update styling and layout
fig3.update_layout(
    title="Weekly Hours Spent on Activities by Gender",
    xaxis_title="Average Hours per Week",
    yaxis_title=None,
    legend_title_text="Gender",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)

fig3.show()
# %%
import plotly.express as px
import pandas as pd

# ① Load and subset Gapminder sample data
df = px.data.gapminder().query("continent == 'Europe' and year in [1952, 2007]")  # built‑in dataset

# ② Plot the two years as dots
fig = px.scatter(
    df,
    x="lifeExp",
    y="country",
    color="year",  # different colour per year
    title="Change in life expectancy, Europe (1952 vs 2007)",
    height=800,
)

# ③ Add a grey connector for each country (the “dumbbell” bar)
for c in df.country.unique():
    seg = df[df.country == c].sort_values("year")
    fig.add_scatter(x=seg.lifeExp, y=seg.country, mode="lines", showlegend=False, line=dict(color="lightgrey", width=2))

fig.update_layout(xaxis_title="Life expectancy (yrs)")
fig.show()

# %%
import plotly.express as px
import pandas as pd

data = {
    "state": ["Arizona", "Georgia", "Michigan", "Pennsylvania", "Wisconsin"],
    "margin_2016": [-3.5, -5.1, -0.2, -0.7, -0.8],  # GOP wins (‑ values)
    "margin_2020": [0.3, 0.2, 2.8, 1.2, 0.6],  # Dem wins (+ values)
}
df = pd.DataFrame(data).melt(id_vars="state", var_name="year", value_name="margin")

fig = px.scatter(
    df,
    x="margin",
    y="state",
    color="year",
    color_discrete_map={"margin_2016": "red", "margin_2020": "blue"},
    title="Swing‑state vote margin (Clinton → Biden)",
    labels={"margin": "Dem − GOP (%)"},
)

# connectors
for st in df.state.unique():
    seg = df[df.state == st].sort_values("year")
    fig.add_scatter(x=seg.margin, y=seg.state, mode="lines", showlegend=False, line=dict(color="grey", width=2))

fig.add_vline(0, line_dash="dash", line_color="black")  # zero reference
fig.show()

# %%
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "company": ["Apex Co", "Beta Ltd", "Cygnus Inc", "Delta LLC"],
    "revenue_pre": [42, 30, 55, 48],
    "revenue_post": [58, 41, 60, 65],
})
df_long = df.melt(id_vars="company", var_name="period", value_name="rev")

fig = px.scatter(
    df_long,
    x="company",
    y="rev",
    color="period",
    color_discrete_sequence=["orange", "green"],
    size=[14] * len(df_long),  # make endpoints visually prominent
    title="Impact of new product launch on annual revenue (M USD)",
)

# connectors
for comp in df.company:
    seg = df_long[df_long.company == comp].sort_values("period")
    fig.add_scatter(x=seg.company, y=seg.rev, mode="lines", showlegend=False, line=dict(color="lightgrey", width=3))

# Add value labels
fig.update_traces(text=df_long.rev.round(0), textposition="top center")

fig.update_layout(
    yaxis_title="Revenue (million USD)",
    xaxis_title=None,
)
fig.show()

# %%
