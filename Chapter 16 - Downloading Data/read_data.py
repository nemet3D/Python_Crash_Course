import csv
from datetime import datetime

class ReadData():
    """A class to read data from CSV files."""

    def __init__(self, filename):
        """Initialize the filename."""
        self.filename = filename

    def read_data(self):
        """Read the data and assign it to specific lists."""
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            self.dates, self.highs, self.lows = [], [], []
            for row in reader:
                try:
                    current_date = datetime.strptime(row[0], "%Y-%m-%d")
                    high = int(row[1])
                    low = int(row[3])
                except ValueError:
                    print(current_date, 'missing data')
                else:
                    self.dates.append(current_date)
                    self.highs.append(high)
                    self.lows.append(low)

            return self.dates, self.highs, self.lows