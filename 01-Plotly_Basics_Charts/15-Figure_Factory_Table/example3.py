import plotly.figure_factory as ff

data_matrix = [['Country', 'Year', 'Population'],
               ['United States', 2000, 282200000],
               ['Canada', 2000, 27790000],
               ['United States', 2010, 309000000],
               ['Canada', 2010, 34000000]]

fig = ff.create_table(data_matrix, colorscale=[[0, '#4d004c'],
                                               [0.5, '#f2e5ff'],
                                               [1, '#ffffff']])

fig.show()
