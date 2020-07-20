"""
Data Analysis with Python Projects - Page View Time Series Visualizer

For this project you will visualize time series data using a line chart, bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

## Tasks:

* Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the "date" column.
* Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
* Create a `draw_line_plot` function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be "Daily freeCodeCamp Forum Page Views 5/2016-12/2019". The label on the x axis should be "Date" and the label on the y axis should be "Page Views".
* Create a `draw_bar_plot` function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of "Months". On the chart, the label on the x axis should be "Years" and the label on the y axis should be "Average Page Views".
* Create a `draw_box_plot` function that uses Searborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)". Make sure the month labels on bottom start at "Jan" and the x and x axis are labeled correctly.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task - 1 (Loading the dataset)
data = pd.read_csv('data/fcc-forum-pageviews.csv', parse_dates = True, index_col = 'date')
print(data.head(5))

# Task - 2 (Data cleaning)
data = data[(data['value'] >= data['value'].quantile(0.025)) & (data['value'] <= data['value'].quantile(0.975))]
print(data.head(5))

# Task - 3 (Line plots - time series plot)
plt.figure(figsize = (10,8))
plt.plot(data, color = 'red') # or plt.plot(data.index, data['value'])
plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
plt.xlabel('Date')
plt.ylabel('Page Views')

# Task - 4 (Bar plots - group by year, month)
data_bar = data.groupby([(data.index.year), (data.index.month)]).mean()

plt.figure(figsize = (12,8))
data_bar.unstack().plot(kind = 'bar')
plt.xlabel('Years')
plt.ylabel('Average Page Views')
plt.legend(title = 'Month', labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'])


# Task - 5 (Box plots - page views distributed within a given year or month over time)
data_copy = data.copy()
data_copy.reset_index(inplace = True)
data_copy['year'] = [i.year for i in data_copy['date']]
data_copy['month'] = [i.strftime('%b') for i in data_copy['date']]
#print(data_copy.head(3))

fig, ax = plt.subplots(1,2,figsize = (20,8))

plt.ylim(10000,180000)
sns.barplot(x = 'year', y = 'value', data = data_copy, ax = ax[0])
ax[0].set_title("Year-Wise Box Plot (Trend)")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Page Views')

plt.ylim(10000,180000)
sns.boxplot(x = 'month',y = 'value', data = data_copy, ax = ax[1])
ax[1].set_title("Month-Year Box Plot (Seasonality)")
ax[1].set_xlabel('Month')
ax[1].set_ylabel('Page Views')


plt.show()
