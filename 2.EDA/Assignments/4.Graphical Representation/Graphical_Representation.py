'''
1.       Univariate plots for UNIV data (Plot must have Title, X & Y label)
A)      Plot numerical column with 3 different plots ?
B)      What are bin parameters? What are the methods to define the number of bins and bin sizes ?
C)      Why do density plots exceed the range values of the column ?
D)      Plot categorical columns by taking unique values ?
'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# Assuming df is your DataFrame
df = pd.DataFrame(pd.read_csv(r'F:\Liser Time\360digitmg\2.EDA\Assignments\4.Graphical Representation\Data Sets\Marks Data.csv'))
df_1 = pd.DataFrame(pd.read_excel(r'F:\Liser Time\360digitmg\2.EDA\Assignments\4.Graphical Representation\Data Sets\University_Clustering.xlsx'))
numerical_column = df['Math']

df.describe()
# A) Plot numerical column with 3 different plots ?
# 1. Histogram
plt.figure(figsize=(12, 6))
plt.subplot(131)
# B) What are bin parameters? What are the methods to define the number of bins and bin sizes ?
plt.hist(numerical_column, bins='auto', color='blue', alpha=0.7) 
plt.title('Histogram')
plt.xlabel('Numerical Column')
plt.ylabel('Frequency')


# 2. Box Plot
plt.subplot(132)
sns.boxplot(x=numerical_column, color='green')
plt.title('Box Plot')
plt.xlabel('Numerical Column')

# 3. KDE (Kernel Density Estimation) Plot  '''It is used for categorical values plotting'''
plt.subplot(133)
sns.kdeplot(numerical_column, color='orange', fill=True)
plt.title('Density Plot')
plt.xlabel('Numerical Column')
plt.ylabel('Density')

plt.tight_layout()
plt.show()

import seaborn as sns

# Assuming df is your DataFrame and 'categorical_column' is a categorical column
categorical_column = df_1['Univ']

#C)Why do density plots exceed the range values of the column ?
'''
Density plots, especially in the context of kernel density estimation (KDE), can extend beyond the observed range of the data for a couple of reasons:
a) Smoothing Effect
b) Assumed Distribution
c) Boundary Correction
d) Bandwidth Parameter
'''
#D)Plot categorical columns by taking unique values ?    
# Count Plot (Bar Plot)  '''It is used for categorical values plotting'''
plt.figure(figsize=(10, 5))
sns.countplot(x=categorical_column)
plt.title('Count Plot of Categorical Column')
plt.xlabel('Categorical Column')
plt.ylabel('Count')
plt.show()

'''
2.  Bivariate graphs for UNIV data (Plot must be readable [use rotation], have all labels)
A)       Plot 2 numerical columns with scatter plot [use grid] ?
B)       2 Different plots for plotting a numerical column with a categorical  column (bar, line) ?
C)       How are bar plots different from histogram?
'''    
### A) Plot 2 numerical columns with a scatter plot [use grid]:


import matplotlib.pyplot as plt
import seaborn as sns
# A) Plot 2 numerical columns with scatter plot [use grid] ?
# Assuming df is your DataFrame with numerical columns 'numerical_col1' and 'numerical_col2'
numerical_col1 = df['Math']
numerical_col2 = df['Science']
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

sns.scatterplot(x= numerical_col1, y= numerical_col2, data=df)

plt.title('Scatter Plot of Numerical Columns')
plt.xlabel('Numerical Column 1')
plt.ylabel('Numerical Column 2')

plt.show()


This code creates a scatter plot using Seaborn for two numerical columns.

### B) 2 Different plots for plotting a numerical column with a categorical column (bar, line):

#### Bar Plot:

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame with numerical column 'numerical_col' and categorical column 'categorical_col'
plt.figure(figsize=(10, 6))
numerical_col = df_1['Top10']
categorical_col = df_1['Univ']
sns.barplot(x= categorical_col, y= numerical_col, data=df_1, ci=None)

plt.title('Bar Plot of Numerical Column by Category')
plt.xlabel('Categorical Column')
plt.ylabel('Numerical Column')

plt.xticks(rotation=45)
plt.show()
#df_1.head()

#### Line Plot:

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame with numerical column 'numerical_col' and categorical column 'categorical_col'
plt.figure(figsize=(10, 6))
numerical_col = df_1['Top10']
categorical_col = df_1['Univ']
sns.lineplot(x= categorical_col, y= numerical_col, data=df_1, marker='o')

plt.title('Line Plot of Numerical Column by Category')
plt.xlabel('Categorical Column')
plt.ylabel('Numerical Column')

plt.xticks(rotation=45)
plt.show()


### C) How are bar plots different from histograms?
'''
- **Bar Plot:** A bar plot is used for displaying the counts or frequencies of categorical data. It represents each category on the x-axis and the corresponding count or value on the y-axis. Bars are separated, and there is often space between them.

- **Histogram:** A histogram is used for visualizing the distribution of a continuous variable. It divides the range of values into intervals (bins) and represents the frequency or probability of occurrences within each bin. Histograms have contiguous bars, as they represent ranges of values rather than distinct categories.

In summary, bar plots are used for categorical data, while histograms are used for visualizing the distribution of continuous data.    


'''
#3.       Plot multivariate graphs (correlation heatmap, pairplot)

#A) Plot for only numerical data ?
#B) Plot multivariate graphs for both numerical and categorical columns ?
#C) What does it mean when a correlation value says 1? When it is negative? When it is zero?
'''

#A) Plot for only numerical data:

For numerical data, you can use a correlation heatmap to visualize the correlation between different numerical columns. Here's an example using the seaborn library:


import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df contains your numerical data
numerical_data = df.select_dtypes(include='number')
correlation_matrix = numerical_data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap for Numerical Data')
plt.show()


B) Plot multivariate graphs for both numerical and categorical columns:

For a multivariate analysis involving both numerical and categorical columns, you can use a pairplot from seaborn. However, pairplots are generally more suitable for numerical variables. If you have categorical variables, you might want to explore other visualization methods like grouping or using categorical plots.


# Assuming df contains both numerical and categorical columns
sns.pairplot(df, hue='categorical_column')
plt.title('Pairplot for Numerical and Categorical Data')
plt.show()


#C) Interpretation of correlation values:

- Correlation value of 1: Perfect positive correlation. It indicates that as one variable increases, the other variable also increases proportionally.
  
- Negative correlation: A correlation value of -1 indicates a perfect negative correlation. It means that as one variable increases, the other variable decreases proportionally.

- Correlation value of 0: No linear correlation. The variables are not linearly related. However, it's important to note that there might be non-linear relationships or other types of dependencies that are not captured by the correlation coefficient.

'''
#4.       Plot Skewness & Probability distribution for each column of marks data. (Hist, box, density)
#A)      What is normally distributed and What will be the relationship between mean, median & mode ?
#B)     Which data variables are positively skewed and What will be the relationship between mean, median & mode
#C)      What are negatively skewed/distributed and What will be the relationship between mean, median & mode
#D)      What are the distinctive differences between skewness and distribution?

'''
#A) Plot Skewness & Probability distribution for each column of marks data. (Hist, box, density):

For each column in the "marks" data, you can create histograms, box plots, and density plots to visualize the skewness and probability distribution. Here's an example using seaborn and matplotlib:


import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df_marks contains your "marks" data
for column in df.columns:
    plt.figure(figsize=(15, 5))

    # Histogram
    plt.subplot(1, 3, 1)
    sns.histplot(df[column], kde=True, color='skyblue')
    plt.title(f'Histogram for {column}')

    # Box plot
    plt.subplot(1, 3, 2)
    sns.boxplot(y=df[column], color='salmon')
    plt.title(f'Box Plot for {column}')

    # Density plot
    plt.subplot(1, 3, 3)
    sns.kdeplot(df[column], color='green', fill=True)
    plt.title(f'Density Plot for {column}')

    plt.show()

print(df.columns)
df.skew()
df.std()
df.mean()
#B) What is normally distributed, and what will be the relationship between mean, median & mode?

A normal distribution is symmetric and bell-shaped. In a perfectly normal distribution, the mean, median, and mode are all equal and located at the center of the distribution.

#C) Which data variables are positively skewed, and what will be the relationship between mean, median & mode?

For positively skewed distributions, the tail is on the right side. In such cases, the mean is typically greater than the median, and both are greater than the mode.

#D) What are negatively skewed/distributed, and what will be the relationship between mean, median & mode?

For negatively skewed distributions, the tail is on the left side. In such cases, the mean is typically less than the median, and both are less than the mode.

#E) What are the distinctive differences between skewness and distribution?

- Skewness measures the asymmetry of a distribution. It indicates whether the data is skewed to the right (positive skewness) or to the left (negative skewness).
  
- Distribution refers to the way data is spread across different values. It can be normal, skewed, uniform, etc. Skewness is one aspect of the distribution that describes its asymmetry.










