import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

# Create fake data
df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())

# Convert to bar chart with Matplotlib
df.iloc[:10].plot(kind='bar')  # Limiting to the first 10 rows for better readability
plt.title("Bar Chart (Matplotlib)")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()

# Convert to bar chart with Plotly
# Limiting to the first 10 rows for better readability
data = []
for col in df.columns:
    data.append(go.Bar(x=df.index[:10], y=df[col][:10], name=col))

layout = go.Layout(title="Bar Chart (Plotly)", barmode='group')
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

# Launch the Plotly graph in a web browser
pyo.plot(fig)
