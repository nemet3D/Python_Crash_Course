import pygal

from die import Die

# Create two dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
sum_result = die_1.num_sides + die_2.num_sides

frequencies = [results.count(frequency) for frequency in range(2, sum_result+1)]
posibilities = [posibility for posibility in range(2, sum_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D" + str(die_1.num_sides) + " and a D" + str(die_2.num_sides) + " dice 50000 times."
hist.x_labels = posibilities
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

legend = "D" + str(die_1.num_sides) + " + D" + str(die_2.num_sides)

hist.add(legend, frequencies)
hist.render_to_file('die_visual.svg')