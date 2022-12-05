import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = '../down_data/sitka_weather_07-2014.csv'

dates, highs, lows = [], [], []
with open(filename) as f:
    reader = csv.reader(f, delimiter=',', quotechar=' ')
    print(next(reader))
    header_row = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        high = (int(row[1]) - 32) * 5 / 9
        low = (int(row[3]) - 32) * 5 / 9
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)  # alpha = 투명도
ax.fill_between(dates, highs, lows, facecolor='red', alpha=0.1)
ax.set_title("Daily high and low temperatures, 2014-07", fontsize=24)
ax.set_xlabel(' ', fontsize=16)
fig.autofmt_xdate()  # x눈금을 살짝 기울임
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
