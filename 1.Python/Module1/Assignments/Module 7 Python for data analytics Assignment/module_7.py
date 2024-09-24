
#1. 1)Please take care of missing data present in the “Data.csv” file using python module 
#“sklearn.impute” and its methods, also collect all the data that has “Salary” less than “70,000”.

import pandas as pd
from sklearn.impute import SimpleImputer

# Step 2: Read the CSV file
data = pd.read_csv("C:/Users/HARSHA/Downloads/Data Set/datasets/Data.csv")
# Check data types of 'Salary' column
print("Data types before imputation:")
print(data.dtypes)

# Convert 'Salary' column to numeric, ignoring errors
data['Salaries'] = pd.to_numeric(data['Salaries'], errors='coerce').isna()

# Check data types after converting 'Salary' column
print("\nData types after converting 'Salary' column:")
print(data.dtypes)

# Step 3: Handle missing data only for numeric values
numeric_columns = data.select_dtypes(include=['number']).columns
numeric_imputer = SimpleImputer(strategy="mean")
data[numeric_columns] = numeric_imputer.fit_transform(data[numeric_columns])


# Step 4: Collect data with "Salary" less than "70,000"
filtered_data = data[data['Salaries'] < 70000]

# Display the results
print("Data with missing values handled:")
print(data.head())

print("\nData with 'Salary' less than 70,000:")
print(filtered_data)

#2. Subtracting dates: 
#‘Python date objects let us treat calendar dates as something similar to numbers: we can compare them, sort them, add, and even subtract them. Do math with dates in a way that would be a pain to do by hand. The 2007 Florida hurricane season was one of the busiest on record, with 8 hurricanes in one year. The first one hit on May 9th, 2007, and the last one hit on December 13th, 2007. How many days elapsed between the first and last hurricane in 2007?
#	Instructions:
#	Import date from datetime.
#	Create a date object for May 9th, 2007, and assign it to the start variable.
#	Create a date object for December 13th, 2007, and assign it to the end variable.
#	Subtract start from end, to print the number of days in the resulting timedelta object.
from datetime import date

# Create date objects
start = date(2007, 5, 9)
end = date(2007, 12, 13)

# Calculate the difference
days_elapsed = end - start

# Print the result
print("Number of days elapsed:", days_elapsed.days)


#3)Representing dates in different ways
#Date objects in Python have a great number of ways they can be printed out as strings. In some cases, you want to know the date in a clear, language-agnostic format. In other cases, you want something which can fit into a paragraph and flow naturally.
#Print out the same date, August 26, 1992 (the day that Hurricane Andrew made landfall in Florida), in a number of different ways, by using the “ .strftime() ” method. Store it in a variable called “Andrew”. 
#Instructions: 	
#Print it in the format 'YYYY-MM', 'YYYY-DDD' and 'MONTH (YYYY)'

from datetime import date

# Create date object
andrew = date(1992, 8, 26)

# Print in different formats
print("YYYY-MM:", andrew.strftime('%Y-%m'))
print("YYYY-DDD:", andrew.strftime('%Y-%j'))
print("MONTH (YYYY):", andrew.strftime('%B (%Y)'))

#4) For the dataset “Indian_cities”, 
#a)Find out top 10 states in female-male sex ratio
#b)Find out top 10 cities in total number of graduates
#c)Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

indian_cities = pd.read_csv("C:/Users/HARSHA/Downloads/Data Set/datasets/Indian_cities.csv")

# Task a: Top 10 states in female-male sex ratio
top_states_sex_ratio = indian_cities.groupby("state_name")["sex_ratio"].mean().sort_values(ascending=False).head(10)
print("Top 10 states in female-male sex ratio:")
print(top_states_sex_ratio)

# Task b: Top 10 cities in total number of graduates
top_cities_graduates = indian_cities.groupby("name_of_city")["total_graduates"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 cities in total number of graduates:")
print(top_cities_graduates)

# Task c: Top 10 cities and their locations in respect of total effective_literacy_rate
top_cities_literacy_rate = indian_cities.groupby("name_of_city")[["effective_literacy_rate_total", "location"]].mean().sort_values(by="effective_literacy_rate_total", ascending=False).head(10)
print("\nTop 10 cities and their locations in respect of total effective_literacy_rate:")
print(top_cities_literacy_rate)

#5) For the data set “Indian_cities”
#a)Construct histogram on literates_total and comment about the inferences
#b)Construct scatter  plot between  male graduates and female graduates

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
indian_cities = pd.read_csv("C:/Users/HARSHA/Downloads/Data Set/datasets/Indian_cities.csv")

# Task a: Construct histogram on literates_total
plt.figure(figsize=(10, 6))
plt.hist(indian_cities['literates_total'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Literates Total in Indian Cities')
plt.xlabel('Total Literates')
plt.ylabel('Frequency')
plt.show()

# Task b: Construct scatter plot between male graduates and female graduates
plt.figure(figsize=(10, 6))
plt.scatter(indian_cities['male_graduates'], indian_cities['female_graduates'], alpha=0.5)
plt.title('Scatter Plot: Male Graduates vs Female Graduates in Indian Cities')
plt.xlabel('Male Graduates')
plt.ylabel('Female Graduates')
plt.show()

#6)For the data set “Indian_cities”
#a)Construct Boxplot on total effective literacy rate and draw inferences
#b)Find out the number of null values in each column of the dataset and delete them.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
indian_cities = pd.read_csv("C:/Users/HARSHA/Downloads/Data Set/datasets/Indian_cities.csv")

# Task a: Construct Boxplot on total effective literacy rate
plt.figure(figsize=(8, 6))
plt.boxplot(indian_cities['effective_literacy_rate_total'].dropna(), vert=False)
plt.title('Boxplot of Total Effective Literacy Rate in Indian Cities')
plt.xlabel('Effective Literacy Rate')
plt.show()

# Task b: Find out the number of null values in each column and delete them
null_values = indian_cities.isnull().sum()
print("Number of null values in each column:")
print(null_values)

# Drop rows with null values
indian_cities_cleaned = indian_cities.dropna()

# Display the cleaned dataset
print("\nCleaned Dataset:")
print(indian_cities_cleaned.head())



