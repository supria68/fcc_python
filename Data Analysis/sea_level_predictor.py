"""
Data Analysis with Python Projects - Sea Level Predictor

You will anaylize a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

## Tasks:

1. Use Pandas to import the data from epa-sea-level.csv.
2. Use matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axix.
3. Use the linregress function from scipi.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
4. Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000. The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Task - 1 (Loading the dataset)
data = pd.read_csv('data/epa-sea-level.csv')
print(data.head(3))

# Task - 2 (Scatter plot between Year and CSIRO adjusted sea level)
fig1 = plt.figure(figsize = (10,6))
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], s = 15, alpha = 0.5)
plt.xlabel('Year')
plt.ylabel('Sea level')
plt.title('Sea Level Predictor')

# Task - 3 (Create line of best fit to predict for 2050)
x = data['Year']
y = data['CSIRO Adjusted Sea Level']
stats = linregress(x, y) # m = slope, c = intercept
x_range = range(1880,2050)
line = stats.slope * x_range + stats.intercept
plt.plot(x_range, line, color = 'green')

# Task - 4 (Create second line of best fit)
new_data = data[data['Year'] >= 2000]
x = new_data['Year']
y = new_data['CSIRO Adjusted Sea Level']

stats = linregress(x,y) # m = slope, c = intercept
x_range = range(2000,2050)
line = stats.slope * x_range + stats.intercept

fig2 = plt.figure(figsize = (10,6))
plt.scatter(x, y, alpha = 0.8, s = 15)
plt.plot(x_range, line, color = 'red')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.show()
