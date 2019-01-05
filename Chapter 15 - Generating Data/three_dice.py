# Three Dice: If you roll three D6 dice, the smallest number you can
# roll is 3 and the largest number is 18. Create a visualization that
# shows what happens when you roll three D6 dice.

import pygal

from die import Die

# Create two dice.
die_1 = Die(8)
die_2 = Die(8)
die_3 = Die()

# Number of rolls.
rolls = 1_000_000

results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(rolls)]

# Analyze the results.
sum_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

frequencies = [results.count(frequency) for frequency in range(3, sum_result+1)]
posibilities = [posibility for posibility in range(3, sum_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D" + str(die_1.num_sides) + ", a D" + str(die_2.num_sides) + " and a D" + str(die_3.num_sides) + " dice "+ str(rolls) + " times."
hist.x_labels = posibilities
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

legend = "D" + str(die_1.num_sides) + " + D" + str(die_2.num_sides) + " + D" + str(die_3.num_sides)

hist.add(legend, frequencies)
hist.render_to_file('three_dice_visual.svg')