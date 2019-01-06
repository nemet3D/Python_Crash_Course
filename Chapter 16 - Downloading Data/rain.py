import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high and low temperatures from file.
filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rains, rain = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            if str(row[21]) == "Rain":
                rain = 1
            else:
                rain = 0
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rains.append(rain)

print(rains)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rains, c='red', alpha=0.5)

# Format plot.
plt.title("Rainy days \nSitka, Alaska, 2014", fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rain", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()