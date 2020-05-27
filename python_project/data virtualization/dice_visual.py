from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

# Create a D6.
dice_1 = Dice(6)
dice_2 = Dice(6)
dice_3 = Dice(6)
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = dice_1.roll() * dice_2.roll() * dice_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = dice_1.num_sides * dice_2.num_sides * dice_3.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multiply rolling three D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6_multiply.html')
