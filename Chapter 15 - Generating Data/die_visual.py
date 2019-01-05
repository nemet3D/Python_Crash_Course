# Automatic Labels: Modify die.py and dice_visual.py by replacing the
# list we used to set the value of hist.x_labels with a loop to generate
# this list automatically. If you’re comfortable with list
# comprehensions, try replacing the other for loops in die_visual.py and
# dice_visual.py with comprehensions as well.

# Two D8s: Create a simulation showing what happens if you roll two
# eightsided dice 1000 times. Increase the number of rolls gradually
# until you start to see the limits of your system’s capabilities.

# Multiplication: When you roll two dice, you usually add the two
# numbers together to get the result. Create a visualization that shows
# what happens if you multiply these numbers instead.

import pygal

from die import Die

# Create two dice.
die_1 = Die(8)
die_2 = Die(8)

# Number of rolls.
rolls = 1_000_000

results = [die_1.roll() * die_2.roll() for roll_num in range(rolls)]

# Analyze the results.
total = die_1.num_sides * die_2.num_sides

frequencies = [results.count(frequency) for frequency in range(1, total+1)]
posibilities = [posibility for posibility in range(1, total+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D" + str(die_1.num_sides) + " and a D" + str(die_2.num_sides) + " dice " + str(rolls) + " times."
hist.x_labels = posibilities
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

legend = "D" + str(die_1.num_sides) + " + D" + str(die_2.num_sides)

hist.add(legend, frequencies)
hist.render_to_file('die_visual.svg')