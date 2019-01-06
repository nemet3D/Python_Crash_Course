# Sitka-Death Valley Comparison: The temperature scales on the Sitka and
# Death Valley graphs reflect the different ranges of the data. To
# accurately compare the temperature range in Sitka to that of Death
# Valley, you need identical scales on the y-axis. Change the settings
# for the y-axis on one or both of the charts in Figures 16-5 and 16-6,
# and make a direct comparison between temperature ranges in Sitka and
# Death Valley (or any two places you want to compare). You can also try
# plotting the two data sets on the same chart.

import csv
from datetime import datetime

from matplotlib import pyplot as plt

from read_data import ReadData as RD

# Get dates, high and low temperatures from file.
filename_1 = RD('sitka_weather_2014.csv')
filename_1.read_data()

filename_2 = RD('death_valley_2014.csv')
filename_2.read_data()

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))

# For filename_1
plt.plot(filename_1.dates, filename_1.highs, c='green', alpha=0.8, label='high Sitka, Alaska')
plt.plot(filename_1.dates, filename_1.lows, c='blue', alpha=0.8, label='low Sitka, Alaska')
plt.fill_between(filename_1.dates, filename_1.highs, filename_1.lows, facecolor='blue', alpha=0.6)

# For filename_2
plt.plot(filename_2.dates, filename_2.highs, c='red', alpha=0.2, label='high Death Valley, California')
plt.plot(filename_2.dates, filename_2.lows, c='orange', alpha=0.2, label='high Death Valley, California')
plt.fill_between(filename_2.dates, filename_2.highs, filename_2.lows, facecolor='orange', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures \nDeath Valley, California, 2014", fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend(loc='upper left')

plt.show()