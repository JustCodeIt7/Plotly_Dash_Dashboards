#%%
import plotly.express as px
import pandas as pd

# %%
import plotly.express as px
import pandas as pd

# Create a simple project schedule dataset
data = {
    "Task": ["Planning", "Design", "Development", "Testing", "Deployment"],
    "Start": ["2023-01-01", "2023-01-15", "2023-02-01", "2023-03-01", "2023-04-01"],
    "End": ["2023-01-14", "2023-01-31", "2023-02-28", "2023-03-14", "2023-04-07"],
    "Duration": [14, 16, 28, 14, 7]
}

df = pd.DataFrame(data)

# Convert dates to datetime
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Create Gantt chart using bar plot
fig = px.bar(df, x="Task", y="Duration",
             title="Project Schedule (Basic Gantt Chart)",
             color="Task",
             orientation='h',
             labels={"x": "Task", "y": "Duration"})

# Update layout to look more like a Gantt chart
fig.update_layout(xaxis_title="Time", 
                 yaxis_title="", 
                 showlegend=False)

# Show the plot
fig.show()
# %%
import plotly.express as px
import pandas as pd

# Create a dataset with multiple resources
data = {
    "Task": ["Planning", "Planning", "Design", "Design", 
            "Development", "Development", "Testing", "Testing"],
    "Resource": ["Team A", "Team B", "Team A", "Team C",
                 "Team B", "Team D", "Team A", "Team C"],
    "Start": ["2023-01-01", "2023-01-05", "2023-01-15", "2023-02-01",
             "2023-02-10", "2023-03-01", "2023-03-05", "2023-04-01"],
    "End": ["2023-01-14", "2023-01-19", "2023-01-31", "2023-02-14",
           "2023-03-21", "2023-03-28", "2023-03-19", "2023-04-07"]
}

df = pd.DataFrame(data)

# Convert dates to datetime
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Create Gantt chart with multiple resources
fig = px.bar(df, x="Task", y="Resource",
             title="Project Schedule with Multiple Resources",
             color="Resource",
             orientation='h',
             labels={"x": "Task", "y": "Resource"})

# Update layout and remove unnecessary elements
fig.update_layout(xaxis_title="", 
                 yaxis_title="",
                 showlegend=True,
                 barmode='group')

# Show the plot
fig.show()
# %%
import plotly.express as px
import pandas as pd

# Create a dataset with progress information
data = {
    "Task": ["Planning", "Design", "Development", "Testing", "Deployment"],
    "Start": ["2023-01-01", "2023-01-15", "2023-02-01", "2023-03-01", "2023-04-01"],
    "End": ["2023-01-14", "2023-01-31", "2023-02-28", "2023-03-14", "2023-04-07"],
    "Duration": [14, 16, 28, 14, 7],
    "Progress": [75, 50, 90, 30, 20]
}

df = pd.DataFrame(data)

# Convert dates to datetime
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Create interactive Gantt chart with progress
fig = px.bar(df, x="Task", y="Duration",
             title="Project Schedule with Progress Tracking",
             color="Progress",
             orientation='h',
             labels={"x": "Task", "y": "Duration"},
             color_continuous_scale=px.colors.sequential.Viridis)

# Update layout and add annotations
fig.update_layout(xaxis_title="Time", 
                 yaxis_title="",
                 showlegend=True,
                 annotations=[dict(text="Progress:", x=0.5, y=-0.2)])

# Add hover data to show progress percentage
fig.update_traces(hovertemplate="<br>".join([
    "Task: %{x}",
    "Duration: %{y}",
    "Progress: %{color:.0%}"
]))

# Show the plot
fig.show()
# %%
#%%
# Gantt Chart Example 1: Basic Project Timeline
import plotly.express as px
import pandas as pd

# Create sample data
tasks = [
    dict(Task="Research", Start='2023-01-01', Finish='2023-01-10', Resource="Planning"),
    dict(Task="Design", Start='2023-01-11', Finish='2023-01-20', Resource="Planning"),
    dict(Task="Development", Start='2023-01-21', Finish='2023-02-10', Resource="Implementation"),
    dict(Task="Testing", Start='2023-02-11', Finish='2023-02-20', Resource="Validation"),
    dict(Task="Deployment", Start='2023-02-21', Finish='2023-02-28', Resource="Implementation")
]

df = pd.DataFrame(tasks)

# Create Gantt Chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Resource",
    title="Project Timeline - Basic Gantt Chart"
)

# Customize layout
fig.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Project Tasks"
)

fig.show()
# %%
#%%
# Gantt Chart Example 2: Color-coded with detailed information
import plotly.express as px
import pandas as pd

# Create sample data with more details
tasks = [
    dict(Task="Market Research", Department="Marketing", Start='2023-03-01', Finish='2023-03-15', 
         Status="Complete", Completion=100),
    dict(Task="Competitor Analysis", Department="Marketing", Start='2023-03-10', Finish='2023-03-25', 
         Status="Complete", Completion=100),
    dict(Task="UI/UX Design", Department="Design", Start='2023-03-20', Finish='2023-04-10', 
         Status="In Progress", Completion=75),
    dict(Task="Frontend Development", Department="Engineering", Start='2023-04-01', Finish='2023-04-30', 
         Status="In Progress", Completion=40),
    dict(Task="Backend Development", Department="Engineering", Start='2023-04-05', Finish='2023-05-10', 
         Status="In Progress", Completion=30),
    dict(Task="Database Setup", Department="Engineering", Start='2023-03-25', Finish='2023-04-15', 
         Status="Complete", Completion=100),
    dict(Task="Quality Assurance", Department="QA", Start='2023-04-20', Finish='2023-05-15', 
         Status="Not Started", Completion=0),
    dict(Task="User Documentation", Department="Support", Start='2023-05-01', Finish='2023-05-20', 
         Status="Not Started", Completion=0)
]

df = pd.DataFrame(tasks)

# Create Gantt Chart
fig = px.timeline(
    df, 
    x_start="Start", 
    x_end="Finish", 
    y="Task",
    color="Department",
    hover_name="Task",
    hover_data=["Status", "Completion"],
    title="Project Tasks by Department"
)

# Customize layout
fig.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Tasks",
    legend_title="Department"
)

# Add Today marker
fig.add_vline(x='2023-04-15', line_width=2, line_dash="dash", line_color="gray",
              annotation_text="Today", annotation_position="top right")

fig.show()
# %%
#%%
# Gantt Chart Example 3: Advanced with milestones and custom styling
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Create realistic project data
project_data = [
    # Planning Phase
    dict(Task="Project Kickoff", Type="Milestone", Start="2023-06-01", Finish="2023-06-01", Phase="Planning"),
    dict(Task="Requirements Gathering", Type="Task", Start="2023-06-01", Finish="2023-06-10", Phase="Planning"),
    dict(Task="Scope Definition", Type="Task", Start="2023-06-08", Finish="2023-06-15", Phase="Planning"),
    dict(Task="Planning Complete", Type="Milestone", Start="2023-06-15", Finish="2023-06-15", Phase="Planning"),
    
    # Design Phase
    dict(Task="Architecture Design", Type="Task", Start="2023-06-16", Finish="2023-06-25", Phase="Design"),
    dict(Task="UI/UX Design", Type="Task", Start="2023-06-16", Finish="2023-07-01", Phase="Design"),
    dict(Task="Design Approval", Type="Milestone", Start="2023-07-01", Finish="2023-07-01", Phase="Design"),
    
    # Development Phase
    dict(Task="Backend Development", Type="Task", Start="2023-07-02", Finish="2023-07-31", Phase="Development"),
    dict(Task="Frontend Development", Type="Task", Start="2023-07-02", Finish="2023-08-05", Phase="Development"),
    dict(Task="API Integration", Type="Task", Start="2023-07-15", Finish="2023-08-03", Phase="Development"),
    dict(Task="Development Complete", Type="Milestone", Start="2023-08-05", Finish="2023-08-05", Phase="Development"),
    
    # Testing Phase
    dict(Task="Unit Testing", Type="Task", Start="2023-07-25", Finish="2023-08-10", Phase="Testing"),
    dict(Task="Integration Testing", Type="Task", Start="2023-08-06", Finish="2023-08-20", Phase="Testing"),
    dict(Task="User Acceptance Testing", Type="Task", Start="2023-08-21", Finish="2023-08-31", Phase="Testing"),
    dict(Task="Testing Complete", Type="Milestone", Start="2023-08-31", Finish="2023-08-31", Phase="Testing"),
    
    # Deployment
    dict(Task="Deployment Preparation", Type="Task", Start="2023-09-01", Finish="2023-09-05", Phase="Deployment"),
    dict(Task="User Training", Type="Task", Start="2023-09-01", Finish="2023-09-10", Phase="Deployment"),
    dict(Task="Go Live", Type="Milestone", Start="2023-09-15", Finish="2023-09-15", Phase="Deployment")
]

df = pd.DataFrame(project_data)

# Create base Gantt chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Phase",
    color_discrete_sequence=px.colors.qualitative.Plotly,
    hover_name="Task",
    hover_data=["Type", "Start", "Finish"],
    title="Software Development Project Timeline"
)

# Add milestones as diamond markers
milestones = df[df["Type"] == "Milestone"]
fig.add_trace(
    go.Scatter(
        x=milestones["Start"],
        y=milestones["Task"],
        mode="markers",
        marker=dict(symbol="diamond", size=12, color="black"),
        name="Milestone",
        showlegend=True
    )
)

# Add Today marker
fig.add_vline(x="2023-07-15", line_width=2, line_dash="dash", line_color="red",
              annotation_text="Today", annotation_position="top right")

# Enhance layout
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Tasks",
    legend_title="Project Phase",
    height=700,
    plot_bgcolor='rgba(240, 240, 240, 0.5)'
)

fig.show()
# %%
# Example 1: Simple Gantt Chart
import plotly.express as px
import pandas as pd

# Create a simple DataFrame with task information
df = pd.DataFrame({
    "Task": ["A", "B", "C", "D"],
    "Start": ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01"],
    "End": ["2023-01-15", "2023-02-20", "2023-03-25", "2023-04-30"]
})

# Create the Gantt chart
fig = px.timeline(df, x_start="Start", x_end="End", y="Task", 
                 title="Project Timeline (Basic)", 
                 color_discrete_sequence=["#1f77b4"])

fig.show()

# %%
# Example 2: Gantt Chart with Task Categories
import plotly.express as px
import pandas as pd

# Create DataFrame with task categories
df = pd.DataFrame({
    "Task": ["Planning", "Design", "Development", "Testing", "Deployment"],
    "Start": ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01"],
    "End": ["2023-01-31", "2023-02-28", "2023-03-30", "2023-04-25", "2023-05-15"],
    "Category": ["Planning", "Design", "Development", "Testing", "Deployment"]
})

# Create the Gantt chart with different colors for categories
fig = px.timeline(df, x_start="Start", x_end="End", y="Task",
                 color="Category", 
                 title="Project Timeline with Categories",
                 color_discrete_map={
                     "Planning": "#1f77b4",
                     "Design": "#ff7f0e",
                     "Development": "#2ca02c",
                     "Testing": "#d62728",
                     "Deployment": "#9467bd"
                 })

fig.show()
# %%
# Example 3: Gantt Chart with Progress Indicators
import plotly.express as px
import pandas as pd

# Create DataFrame with progress information
df = pd.DataFrame({
    "Task": ["Requirement Gathering", "System Design", "Implementation", "Testing"],
    "Start": ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01"],
    "End": ["2023-01-31", "2023-03-15", "2023-05-01", "2023-06-01"],
    "Progress": [90, 70, 45, 20],
    "Parent Task": ["Planning", "Design", "Development", "Testing"]
})

# Create the Gantt chart with progress indicators
fig = px.timeline(df, x_start="Start", x_end="End", y="Task",
                 title="Project Timeline with Progress",
                 color="Parent Task", 
                 color_discrete_sequence=["#1f77b4", "#ff7f0e"],
                 range_x=["2022-12-01","2023-07-01"])

# Update the figure to show progress
fig.update_layout(
    hovermode='x',
    bargap=0.2,
    height=600
)

fig.show()
# %%
