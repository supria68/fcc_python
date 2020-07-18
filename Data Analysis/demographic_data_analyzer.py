"""
Data Analysis with Python Projects - Demographic Data Analyzer

In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database.

You must use Pandas to answer the following questions:
* How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (`race` column)
* What is the average age of men?
* What is the percentage of people who have a Bachelor's degree?
* What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
* What percentage of people without advanced education make more than 50K?
* What is the minimum number of hours a person works per week?
* What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
* What country has the highest percentage of people that earn >50K and what is that percentage?
* Identify the most popular occupation for those who earn >50K in India. 

### Dataset Source

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

"""
import numpy as np
import pandas as pd

# Loading the dataset
data = pd.read_csv('data/adult.data')
print("Given dataframe: \n")
print(data.head(3))

print("\n ###### Data Analysis ###### \n")
# Question 1: How many people of each race are represented in this dataset?
race_count = data[' race'].value_counts()
print("Number of each race:\n", race_count)


# Question 2: What is the average age of men?
average_age_men = round(data[data[' sex'] == ' Male']['age'].mean(), 1)
print("\nAverage age of men: ", average_age_men)


# Question 3:  What is the percentage of people who have a Bachelor's degree?
temp = data[' education'].value_counts(normalize = True) * 100
percentage_bachelors = round(temp[' Bachelors'], 1)
print("\nPercentage with Bachelors degrees: {}%\n".format(percentage_bachelors))


# Question 4: What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
adv_degree = data[(data[' education'] == ' Bachelors') | (data[' education'] == ' Masters') | (data[' education'] == ' Doctorate')]
temp = adv_degree[' salary'].value_counts(normalize = True)
higher_education_rich = round(temp.loc[' >50K'] * 100, 1)
print("Percentage with higher education that earn >50K: {}%\n".format(higher_education_rich))


# Question 5: What percentage of people without advanced education make more than 50K?
degrees_to_keep = [' HS-grad', ' Some-college',' Prof-school',' Assoc-voc',' Assoc-acdm',' 10th',' 11th',' 7th-8th',' 12th',' 9th',' 5th-6th',' 1st-4th']
no_adv_degree = data[data[' education'].isin(degrees_to_keep)]
temp = no_adv_degree[' salary'].value_counts(normalize = True)
lower_education_rich = round(temp.loc[' >50K'] * 100, 1)
print("Percentage without lower education that earn >50K: {}%\n".format(lower_education_rich))


# Question 6:  What is the minimum number of hours a person works per week?
min_work_hours = data[' hours-per-week'].min()
print("Min work time: {} hours/week\n".format(min_work_hours))


# Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
temp = data[data[' hours-per-week'] == 1]
temp = temp[' salary'].value_counts(normalize = True)
rich_percentage = round(temp.loc[' >50K'] * 100, 1)
print("Percentage of rich among those who work fewest hours: {}%\n".format(rich_percentage))


# Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
temp = data.groupby(' native-country')[' salary'].value_counts(normalize = True).reset_index(name = 'percents')
country = temp[temp[' salary'] == ' >50K'].sort_values(by = 'percents', ascending = False)
highest_earning_country = country.iloc[0][' native-country']
highest_earning_country_percentage = round(country.iloc[0]['percents'] * 100, 1)

print("Country with highest percentage of rich: {}\n".format(highest_earning_country))
print("Highest percentage of rich people in country: {}%\n".format(highest_earning_country_percentage))


# Question 9: Identify the most popular occupation for those who earn >50K in India.
temp = data[(data[' native-country'] == ' India') & (data[' salary'] == ' >50K')]
temp = temp[' occupation'].value_counts().reset_index()
top_IN_occupation = temp['index'][0]

print("Top occupations in India: {}\n".format(top_IN_occupation))

