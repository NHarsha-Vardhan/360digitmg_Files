
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Q1 

UNIV_df = pd.read_excel(r"C:\Users\HP\Desktop\University_Clustering.xlsx")
UNIV_df.columns

# Q1A) 

# Create a boxplot
sns.boxplot(x=UNIV_df["GradRate"])
plt.xlabel('GradRate Boxplot')
plt.title('GradRate')
plt.show()


# Create a histogram
plt.hist(UNIV_df['GradRate'], bins=5, color='green')
plt.xlabel('GradRate')
plt.ylabel('Frequency')
plt.title('Histogram of GradRate')
plt.show()

# Create a density plot
sns.kdeplot(UNIV_df['GradRate'], shade=True, color='green')
plt.xlabel('GradRate')
plt.ylabel('Density')
plt.title('Density Plot of GradRate')
plt.show()

# Q1D) 

# Count the number of occurrences in Typeofsales
counts = UNIV_df['State'].value_counts()

# Plot the counts as a bar chart
counts.plot(kind='bar')
# Add labels and title
plt.xlabel('State Name')
plt.ylabel('Count of Unis')
plt.title('University Location Plot')
plt.xticks(rotation =0, size = 11)
plt.show()

# Q2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

UNIV_df = pd.read_excel(r"C:\Users\HP\Desktop\University_Clustering.xlsx")

# Q2A) 
# Create scatter plot
sns.scatterplot(x='Accept', y='GradRate', data=UNIV_df)
plt.xlabel('Accept')
plt.ylabel('GradRate')
plt.title('Acceptance vs Gradrate scatter plot')
plt.grid()
plt.show()

# Q2B) 

# Plot a line plot between numerical and categorical columns
plt.plot(UNIV_df.Univ, UNIV_df['Accept'])
plt.xlabel('University names')
plt.ylabel('Acceptance Rate')
plt.xticks(rotation = 90)
plt.title('Line plot of Universities acceptance')
plt.show()

# Plot a bar plot between numerical and categorical columns
plt.bar(UNIV_df.Univ, UNIV_df['Accept'])
plt.xlabel('University names')
plt.ylabel('Acceptance Rate')
plt.xticks(rotation = 90)
plt.title('Bar plot of Universities acceptance')
plt.show()

# Q3 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

UNIV_df = pd.read_excel(r"C:\Users\HP\Desktop\University_Clustering.xlsx")

# Q3A) 

# Create Heatmap 
# define the numerical correlation matrix
numerical_corr = UNIV_df.corr()
# plot the correlation matrix using seaborn
sns.heatmap(numerical_corr, cmap='coolwarm', annot=True)
plt.show()

# create a pairplot
sns.pairplot(UNIV_df)
# show the plot
plt.show()


# Q3B) 
# calculate the dataframe correlation matrix
# pip install dython
from dython.nominal import associations
complete_correlation= associations(UNIV_df, filename= 'complete_correlation.png', figsize=(10,10))

# Q4
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

MARKS_df = pd.read_csv(r"C:\Users\HP\Desktop\Z 253\Marks Data.csv")

sns.distplot(MARKS_df['Social.Studies'])
sns.distplot(MARKS_df['Science'])
sns.distplot(MARKS_df['Math'])

MARKS_df['Social.Studies'].mean()
MARKS_df['Social.Studies'].median()
MARKS_df['Social.Studies'].mode()

MARKS_df['Science'].mean()
MARKS_df['Science'].median()
MARKS_df['Science'].mode()



 







