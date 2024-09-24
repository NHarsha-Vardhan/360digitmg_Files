# Data Visualization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data into Python
education = pd.read_csv(r"F:\Liser_Time\360digitmg\2.EDA\Data Sets\education.csv")

# Read data into Python
education.shape

# barplot
plt.bar(height = education.gmat, x = np.arange(1, 774, 1)) # initializing the parameter

# Histogram
plt.hist(education.gmat) # histogram
plt.hist(education.gmat, bins = [600, 680, 710, 740, 780], color = 'green', edgecolor="red") 
plt.hist(education.workex)
plt.hist(education.workex, color='red', edgecolor = "black", bins = 6)

help(plt.hist)

# Histogram using Seaborn
import seaborn as sns
sns.distplot(education.gmat) # Deprecated histogram function from seaborn

sns.displot(education.gmat) # Histogram from seaborn


#sns.displot(pharmacy_2.NetSales) # Histogram from seaborn

# Boxplot
plt.figure()
plt.boxplot(education.gmat) # boxplot

help(plt.boxplot)


# Density Plot
sns.kdeplot(education.gmat) # Density plot
sns.kdeplot(education.gmat, bw = 0.5 , fill = True)


# Descriptive Statistics
# describe function will return descriptive statistics including the 
# central tendency, dispersion and shape of a dataset's distribution.

education.describe()


# Bivariate visualization
# Scatter plot
import pandas as pd
import matplotlib.pyplot as plt

cars = pd.read_csv(r"F:\Liser Time\360digitmg\2.EDA\Data Sets\Cars.csv")

cars.info()

plt.scatter(x = cars['HP'], y = cars['MPG']) 

plt.scatter(x = cars['HP'], y = cars['SP'], color = 'green') 

