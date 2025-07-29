import plotly.figure_factory as ff
import pandas as pd

df = pd.DataFrame({
    "Name": ["Luke", "Anakin", "Padme", "Yoda"],
    "Age": [25, 50, 45, 353],
    "Planet": ["Tatooine", "Tatooine", "Naboo", "Dagobah"]
})

fig = ff.create_table(df)
fig.show()
