import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the point.
rw = RandomWalk(5_000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=1)

# Emphasize the first and last points.
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()