from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 3}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='두개의 정육면체 주사위를 1000번 던진 결과', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'down_data': data, 'layout': my_layout}, filename='d6_d6_.html')
