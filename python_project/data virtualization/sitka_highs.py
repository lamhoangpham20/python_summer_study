import csv

from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get high temperatures from this file.
    dates, highs, lows, rains = [], [], [], []
    for row in reader:
        high = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        low = int(row[6])
        rain = float(row[3])
        rains.append(rain)
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        
# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, rains, c='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='y', which='major', labelsize=16)
plt.yscale('linear')
plt.show()
