"""
Data Analysis with Python Projects - Medical Data Visualizer


In this project, you will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

#### Data description

The rows in the dataset represent patiets and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to exploring the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

File name: medical_examination.csv

#### Tasks

Create a chart similar to `examples/Figure_1.png`, where we show the counts of good and bad outcomes for cholesterol, gluc, alco variable, active, and smoke for patients with cardio=1 and cardio=0 in different panels.

Use the data to complete the following tasks in `medical_data_visualizer.py`:
* Add an 'overweight' column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
* Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
* Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's `catplot()`. The dataset should be split by 'Cardio' so there is one chart for each 'cardio' value. The chart should look like "examples/Figure_1.png".
* Clean the data. Filter out the following patient segments that represent incorrect data:
  - diastolic pressure is higher then systolic (Keep the correct data with `df['ap_lo'] <= df['ap_hi'])`)
  - height is less than the 2.5th percentile (Keep the correct data with `(df['height'] >= df['height'].quantile(0.025))`)
  - height is more than the 97.5th percentile
  - weight is less then the 2.5th percentile
  - weight is more than the 97.5th percentile
* Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's `heatmap()`. Mask the upper triangle. The chart should look like "examples/Figure_2.png".

Any time a variable is set to 'None', make sure to set it to the correct code.

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('data/medical_examination.csv')

# Add 'overweight' column
df['overweight'] = np.where(df['weight'] / ((df['height'] / 100)**2) > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. 
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)

##### 1. Draw Categorical Plot
df_cat = pd.melt(frame = df, id_vars = 'cardio', value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

df_cat = pd.DataFrame(df_cat.groupby(['variable','value','cardio'])['value'].count()).rename(columns = {'value': 'total'}).reset_index()

plt.figure(figsize = (10,6))
sns.catplot(data = df_cat, x = 'variable', y = 'total', hue = 'value', col = 'cardio', kind = 'bar')


##### 2. Draw Heat Map

# data cleaning.
df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

# Calculate the correlation matrix
corr = df_heat.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype = np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
plt.figure(figsize = (10,9))
sns.heatmap(data = corr, annot = True, fmt ='.1f', mask = mask, vmax = 0.3, center = 0, square = True, linewidths = 0.9,cbar_kws = {'shrink':.5})


plt.show()
