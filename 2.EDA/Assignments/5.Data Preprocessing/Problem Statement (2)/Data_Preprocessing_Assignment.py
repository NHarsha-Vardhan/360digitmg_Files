'''
1.Type casting
2.Handling Duplicates
3.Outlier analysis/treatment
4.zero or near zero variance
5.Discretization/Binning/Grouping
6.Dummy variable condition
7.Missing values
8.Transformation
9.Feature scaling/Feature Shrinking
10.string manipulation
################

'''
'''
Duplication_Typecasting-Problem statement.docx 
Q1) Problem statemnt:
Data collected may have duplicate entries, that might be because the data collected were not at regular intervals
 or for any other reason. Building a proper solution on such data will be a tough ask. The common techniques are 
 either removing duplicates completely or substituting those values with logical data. There are various techniques 
 to treat these types of problems.
'''
import pandas as pd,numpy as np, seaborn as sns,matplotlib as plt

'Q1) For the given dataset perform the type casting (convert the datatypes, ex. float to int)'

# Fetching the excel to the df_invoice dataframe through pandas
df_invoice = pd.DataFrame(pd.read_excel(r"F:\Liser Time\360digitmg\2.EDA\Assignments\5.Data Preprocessing\Problem Statement (2)\Data_Preprocessing_assignment_dataset\Duplication_Typecasting-Dataset.xlsx"))

invoice_feature = {'Name of feature':['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country'],
                   'Desription': ['Invoice Number is uniquenumber that keep trackon while transaction','Stock codes are also known as ticker symbols or stock symbols.','Description details','Quantity is the amount present','It is related to transaction date','Amount of price per unit','It is ID of customer of unique value','countryName'],
                   'Type':['Nominal Quantitative','Nominal Quantitative','Qualitative','Nominal','continous','Nominal','Nominal','Nominal','categorical'],
                   'Relevance':[]
                   }
print(invoice_feature.values())

#checking the types of df_invoice dataset
df_invoice.dtypes

df_invoice.describe()

df_invoice.head()

#converting the float to int type 
df_invoice.UnitPrice = df_invoice.UnitPrice.astype('int')


'Q2. Check for duplicate values, and handle the duplicate values (ex. drop)'

#checking duplicates
duplicate_invoice = df_invoice.duplicated()
duplicate_invoice

sum(duplicate_invoice)

'Q3. Do the data analysis (EDA)?'

#boxplot
sns.boxplot(df_invoice['InvoiceNo'])
plt.xlabel('Invoice Number')
plt.title('Invoice Number')
plt.show()

sns.boxplot(x=df_invoice['Quantity'])
plt.xlabel('Quantity')
plt.title('Quantity')
plt.show()

sns.boxplot(x=df_invoice['UnitPrice'])
plt.xlabel('UnitPrice')
plt.title('UnitPrice')
plt.show()

df_invoice['UnitPrice'].median()

sns.boxplot(x=df_invoice['CustomerID'])
plt.xlabel('CustomerID')
plt.title('CustomerID')
plt.show()

#barplot
counts = df_invoice['Quantity'].value_counts()
print(counts)
counts.dtypes
# Plot the counts as a bar chart
counts.plot(kind='bar')
# Add labels and title
plt.xlabel('Quantity')
plt.ylabel('Count of Quantity')
plt.title('Invoice bar plot')
plt.xticks(rotation =0, size = 11)
plt.show()

#histogram
plt.hist(df_invoice['InvoiceNo'], bins=5, color='green')
plt.xlabel('InvoiceNo')
plt.ylabel('Frequency')
plt.title('Histogram of GradRate')
plt.show()

plt.hist(df_invoice['Quantity'], bins=5, color='green')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.title('Histogram of GradRate')
plt.show()

#df_invoice['UnitPrice']
plt.hist(x= counts, bins=5, color='green')
plt.xlabel('UnitPrice')
plt.ylabel('Frequency')
plt.title('Histogram of GradRate')
plt.show()

#scatter plot

# Create scatter plot
sns.scatterplot(x='UnitPrice', y='Quantity', data=df_invoice)
plt.xlabel('UnitPrice')
plt.ylabel('Quantity')
plt.title('UnitPrice vs Quantity scatter plot')
plt.grid()
plt.show()


'''
DataPreparation_Outlier_Treatment.docx
Q2) Problem statemnt:
Problem Statement:  
Most of the datasets have extreme values or exceptions in their observations. These values affect the 
predictions (Accuracy) of the model in one way or the other, removing these values is not a very good option.
 For these types of scenarios, we have various techniques to treat such values. 
'''
# 'https://www.kaggle.com/code/prasadperera/the-boston-housing-dataset'
import pandas as pd,numpy as np, seaborn as sns,matplotlib as plt
import matplotlib.pyplot as plt
df_outlier_treat = pd.DataFrame(pd.read_excel(r"F:\Liser Time\360digitmg\2.EDA\Assignments\5.Data Preprocessing\Problem Statement (2)\Data_Preprocessing_assignment_dataset\DataPreparation_Outlier_Treatment.xlsx"))


outlier_feature = {'Name of feature':['crim','zn','indus', 'chas','nox','rm','age','dis','rad','tax','ptratio','black','lstat'],
                   'Desription': ['per capita crime rate by town','proportion of residential land zoned','proportion of non-retail business acres per town','Charles River dummy variable','nitric oxides concentration','average number of rooms per dwelling','proportion of owner-occupied','weighted distances to five Boston employment centres',' index of accessibility to radial highways','full-value property-tax','pupil-teacher ratio by town','proportion of blacks by town','% lower status of the population'],
                   'Type':['Ratio','Nominal','Ratio','Nominal','Nominal','Nominal','Ratio','Ratio','Nominal','Ratio','Interval','Nominal','Nominal'],
                   'Relevance':[]
                   }
print(outlier_feature.values())

#checking the types of df_outlier_treat dataset
df_outlier_treat.dtypes

df_outlier_treat.describe()

#duplicates
duplicate_outler_treat = df_outlier_treat.duplicated()
duplicate_outler_treat

sum(duplicate_outler_treat)
#Ploting the box plot for the criminal data of original dataset
sns.boxplot(df_outlier_treat.crim)
# Detection of outliers (find limits for salary based on IQR)
IQR = df_outlier_treat['crim'].quantile(0.75) - df_outlier_treat['crim'].quantile(0.25)

lower_limit = df_outlier_treat['crim'].quantile(0.25) - (IQR * 1.5)
upper_limit = df_outlier_treat['crim'].quantile(0.75) + (IQR * 1.5)

############### 1. Remove (let's trim the dataset) ################
# Trimming Technique
# Let's flag the outliers in the dataset

outliers_df = np.where(df_outlier_treat.crim > upper_limit, True, np.where(df_outlier_treat.crim < lower_limit, True, False))

# outliers data
df_out = df_outlier_treat.loc[outliers_df, ]

df_trimmed = df_outlier_treat.loc[~(outliers_df), ]
df_outlier_treat.shape, df_trimmed.shape

sns.boxplot(df_trimmed.crim)

############### 2. Replace ###############
# Replace the outliers by the maximum and minimum limit
df_outlier_treat['df_replaced'] = pd.DataFrame(np.where(df_outlier_treat['crim'] > upper_limit, upper_limit, np.where(df_outlier_treat['crim'] < lower_limit, lower_limit, df_outlier_treat['crim'])))
sns.boxplot(df_outlier_treat.df_replaced)


############### 3. Winsorization ###############
# pip install feature_engine   # install the package
from feature_engine.outliers import Winsorizer

# Define the model with IQR method
winsor_iqr = Winsorizer(capping_method = 'iqr', 
                        # choose  IQR rule boundaries or gaussian for mean and std
                          tail = 'both', # cap left, right or both tails 
                          fold = 1.5, 
                          variables = ['crim'])

df_s = winsor_iqr.fit_transform(df_outlier_treat[['crim']])

# Inspect the minimum caps and maximum caps
# winsor.left_tail_caps_, winsor.right_tail_caps_

# Let's see boxplot
sns.boxplot(df_s.crim)


# Define the model with Gaussian method
winsor_gaussian = Winsorizer(capping_method = 'gaussian', 
                             # choose IQR rule boundaries or gaussian for mean and std
                          tail = 'both', # cap left, right or both tails 
                          fold = 3,
                          variables = ['crim'])

df_t = winsor_gaussian.fit_transform(df_outlier_treat[['crim']])
sns.boxplot(df_t.crim)


# Define the model with percentiles:
# Default values
# Right tail: 95th percentile
# Left tail: 5th percentile

winsor_percentile = Winsorizer(capping_method = 'quantiles',
                          tail = 'both', # cap left, right or both tails 
                          fold = 0.05, # limits will be the 5th and 95th percentiles
                          variables = ['crim'])

df_p = winsor_percentile.fit_transform(df_outlier_treat[['crim']])
sns.boxplot(df_p.crim)

#heat map correlation
plt.figure(figsize=(20,10))
sns.heatmap(df_outlier_treat.corr().abs(),annot= True )

#ploting the scatter plot with indus (vs) nox
sns.scatterplot(x='indus', y='nox', data=df_outlier_treat)
plt.xlabel('proportion of non-retail business acres per town')
plt.ylabel(' nitric oxides concentration (parts per 10 million)')
plt.title('indus vs nox scatter plot')
plt.grid()
plt.show()
#ploting the scatter plot with indus (vs) age
sns.scatterplot(x='indus', y='age', data=df_outlier_treat)
plt.xlabel('proportion of non-retail business acres per town')
plt.ylabel('age')
plt.title('indus vs age scatter plot')
plt.grid()
plt.show()


'''
Zero Variance Features.docx
Q3) Problem statemnt:
Problem Statement:  
Find which columns of the given dataset with zero variance, and explore various techniques used to remove the 
zero variance from the dataset to perform certain analysis.
'''


import pandas as pd,numpy as np, seaborn as sns,matplotlib as plt
import matplotlib.pyplot as plt
df_zero_var = pd.DataFrame(pd.read_excel(r"F:\Liser Time\360digitmg\2.EDA\Assignments\5.Data Preprocessing\Problem Statement (2)\Data_Preprocessing_assignment_dataset\Zero Variance Features.xlsx"))


zero_var_feature = {'Name of feature':['Id','square.length ','square.breadth', 'rec.Length ','rec.breadth','color'],
                   'Desription': ['Identity values','Length of square','Breadth of square','Length of rectangle','Breadth of rectangle'],
                   'Type':['Discrete Nominal','Discrete','Discrete','continous','continous','continous'],
                   'Relevance':[]
                   }
print(zero_var_feature.values())

#checking the types of df_zero_var
df_zero_var.dtypes

df_zero_var.describe()
#df_zero_var['squarelength'].skew()
#duplicates
duplicate_zero_var = df_zero_var.duplicated()
duplicate_zero_var

sum(duplicate_zero_var)

# Detection of outliers (find limits for salary based on IQR)
IQR = df_zero_var['recbreadth'].quantile(0.75) - df_zero_var['recbreadth'].quantile(0.25)

lower_limit = df_zero_var['recbreadth'].quantile(0.25) - (IQR * 1.5)
upper_limit = df_zero_var['recbreadth'].quantile(0.75) + (IQR * 1.5)

############### 1. Remove (let's trim the dataset) ################
# Trimming Technique
# Let's flag the outliers in the dataset

outliers_df = np.where(df_zero_var.squarelength > upper_limit, True, np.where(df_zero_var.squarelength < lower_limit, True, False))
outliers_df = np.where(df_zero_var.squarebreadth > upper_limit, True, np.where(df_zero_var.squarebreadth < lower_limit, True, False))
outliers_df = np.where(df_zero_var.recLength > upper_limit, True, np.where(df_zero_var.recLength < lower_limit, True, False))
outliers_df = np.where(df_zero_var.recbreadth > upper_limit, True, np.where(df_zero_var.recbreadth < lower_limit, True, False))
# outliers data
df_out = df_zero_var.loc[outliers_df, ]

df_trimmed = df_zero_var.loc[~(outliers_df), ]
df_zero_var.shape, df_trimmed.shape


##############
#zero variance and near zero variance ## 

df_zero_var.dtypes
# If the variance is low or close to zero, then a feature is approximately constant and will not improve the performance of the model.
# In that case, it should be removed. 

df_zero_var['squarelength'].var() # variance is 0.08743589743589748
df_zero_var['squarebreadth'].var() # variance is 0.09192307692307693
df_zero_var['recLength'].var() # variance is 0.010897435897435902
df_zero_var['recbreadth'].var() # variance is 0.005769230769230769
 

#df.var() == 0
#df.var(axis = 0) == 0

'''
Discretization problem statement.docx
Q4) Problem statemnt:
Problem Statement:  
1)Convert the continuous data into discrete classes on the iris dataset.
Prepare the dataset by performing the preprocessing techniques, to have the data which improves model performance
'''

import pandas as pd,numpy as np, seaborn as sns,matplotlib as plt
import matplotlib.pyplot as plt
df_discretization = pd.DataFrame(pd.read_excel(r"F:\Liser Time\360digitmg\2.EDA\Assignments\5.Data Preprocessing\Problem Statement (2)\Data_Preprocessing_assignment_dataset\Discretization problem statement.xlsx"))


discretization_feature = {'Name of feature':['SepalLength','SepalWidth ','PetalLength', 'PetalWidth ','Species'],
                   'Desription': ['Length of sepal','width of sepal','sepal of petal','width of petal','a group of living organisms consisting of similar individuals capable of exchanging genes or interbreeding'],
                   'Type':['Discrete Nominal','Interval continous','Discrete','Discrete','continous','continous'],
                   'Relevance':[]
                   }
print(discretization_feature.values())

#checking the types of df_zero_var
df_discretization.dtypes

df_discretization.describe()

# Discretization / Multiple bins
df_discretization['SepalLength_1'] = pd.cut(df_discretization['SepalLength'], 
                              bins = [min(df_discretization.SepalLength), 
                                      df_discretization.SepalLength.quantile(0.25),
                                      df_discretization.SepalLength.mean(),
                                      df_discretization.SepalLength.quantile(0.75),
                                      max(df_discretization.SepalLength)], 
                              include_lowest = True,
                              labels = ["very short", "medium short", "medium", "Long"])


'''
Dummy variables problem statement.docx
Q5)
Problem Statement: 
Data is one of the most important assets. It is often common that data is stored in distinct systems with 
different formats and forms. Non-numeric form of data makes it tricky while developing mathematical equations
 for prediction models. We have the preprocessing techniques to make the data convert to numeric form.

'''
import pandas as pd,numpy as np, seaborn as sns,matplotlib as plt
import matplotlib.pyplot as plt
df_dummy_variables = pd.DataFrame(pd.read_excel(r"F:\Liser Time\360digitmg\2.EDA\Assignments\5.Data Preprocessing\Problem Statement (2)\Data_Preprocessing_assignment_dataset\Dummy variables problem statement.xlsx"))


dummy_variables_feature = {'Name of feature':['Index','Animals ','Gender', 'Homly','Types'],
                   'Desription': ['Index values','Animal types','gender(M/F)','Homly categories','categories of types'],
                   'Type':['Discrete','Discrete','Discrete','Discrete','Discrete','Discrete'],
                   'Relevance':[]
                   }
print(discretization_feature.values())

df_dummy_variables.dtypes

#duplicates
duplicate_dummy_variables = df_dummy_variables.duplicated()
duplicate_dummy_variables

sum(duplicate_dummy_variables)

# Create dummy variables
df_new = pd.get_dummies(df_dummy_variables)
df_new.shape

df_new_1 = pd.get_dummies(df_dummy_variables, drop_first = True) #  It's common to use drop_first=True  when dealing with categorical variables with a high cardinality to avoid multicollinearity in models like linear regression. However, the choice depends on your specific analysis and the requirements of your model.
df_new_1.shape
# Created dummies for all categorical columns

##### One Hot Encoding works

from sklearn.preprocessing import OneHotEncoder
# Creating instance of One-Hot Encoder
enc = OneHotEncoder() # initializing method

enc_df = pd.DataFrame(enc.fit_transform(df_dummy_variables.iloc[:, :]).toarray())


#######################
# Label Encoder
from sklearn.preprocessing import LabelEncoder

# Creating instance of labelencoder
labelencoder = LabelEncoder()

# Data Split into Input and Output variables
X = df_dummy_variables.iloc[:, :4]
y = df_dummy_variables.iloc[:, 4]

X['Gender'] = labelencoder.fit_transform(X['Gender'])
X['Animals'] = labelencoder.fit_transform(X['Animals'])


'''
Imputation(Missing values) problem statement.docx
Q6)
Problem Statement: 
1)Prepare the dataset using various techniques to solve the problem, explore all the techniques available 
 and use them to see which gives the best result.

'''

import numpy as np
import pandas as pd

# Load modified ethnic dataset
df_missing_values = pd.read_excel(r"F:\Liser Time\360digitmg\2.EDA\Assignments\5.Data Preprocessing\Problem Statement (2)\Data_Preprocessing_assignment_dataset\Missing values.xlsx") # for doing modifications
df_missing_values.dtypes
# Check for count of NA's in each column
df_missing_values.isna().sum()

dummy_variables_feature = {'Name of feature':['CASNUM','ATTORNEY ','CLMSEX', 'CLMINSUR','SEATBELT','CLMAGE','LOSS'],
                   'Desription': ['casnum values','attroney id','CLMSEX values','clmnsur values','seatbelt values','clmage values','loss values'],
                   'Type':['Discrete','Discrete','Discrete','Discrete','Discrete','continous'],
                   'Relevance':[]
                   }
print(discretization_feature.values())

df_missing_values.describe()
# Create an imputer object that fills 'Nan' values
# Mean and Median imputer are used for numeric data (Salaries)
# Mode is used for discrete data (ex: Position, Sex, MaritalDesc)

# For Mean, Median, Mode imputation we can use Simple Imputer or df.fillna()
from sklearn.impute import SimpleImputer

# Mean Imputer 
mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
df_missing_values["CLMAGE_mean"] = pd.DataFrame(mean_imputer.fit_transform(df_missing_values[["CLMAGE"]]))
df_missing_values["CLMAGE_mean"].isna().sum()


# Median Imputer
median_imputer = SimpleImputer(missing_values = np.nan, strategy = 'median')
df_missing_values["CLMAGE_median"] = pd.DataFrame(median_imputer.fit_transform(df_missing_values[["CLMAGE"]]))
df_missing_values["CLMAGE_median"].isna().sum()  # all records replaced by median 

df_missing_values.isna().sum()

# Mode Imputer
mode_imputer = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
df_missing_values["CLMAGE_mode"] = pd.DataFrame(mode_imputer.fit_transform(df_missing_values[["CLMAGE"]]))

df_missing_values.isnull().sum()  # all Sex, MaritalDesc records replaced by mode

# Constant Value Imputer
#constant_imputer = SimpleImputer(missing_values = np.nan, strategy = 'constant', fill_value = 'F')
# fill_value can be used for numeric or non-numeric values

#df["Sex"] = pd.DataFrame(constant_imputer.fit_transform(df[["Sex"]]))

# Random Imputer
from feature_engine.imputation import RandomSampleImputer

random_imputer = RandomSampleImputer(['CLMAGE'])
df_missing_values["CLMAGE_random"] = pd.DataFrame(random_imputer.fit_transform(df_missing_values[["CLMAGE"]]))
df_missing_values["CLMAGE_random"].isna().sum()  # all records replaced by median


#Hot deck imputation
#ffill will act as the forward  fill
df_missing_values['CLMAGE'].fillna(method='ffill',inplace = True)

#ffill will act as the backward fill
df_missing_values['CLMAGE'].fillna(method='bfill',inplace = True)

'''
Data Transformation(Q-Q plots) problem statement.docx
Q7)
Problem Statement: 
Prepare the dataset by performing the preprocessing techniques, to have the data which improves model 
performance.

'''
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import pylab
import numpy as np
# Read data into Python
df_transformation = pd.read_excel(r"F:\Liser Time\360digitmg\2.EDA\Assignments\5.Data Preprocessing\Problem Statement (2)\Data_Preprocessing_assignment_dataset\Transformation problem statement.xlsx")


transformation_feature = {'Name of feature':['weightgainedgrams','Caloriesconsumed'],
                   'Desription': ['weight of grams','calories consumed'],
                   'Type':['continous','Discrete'],
                   'Relevance':[]
                   }
print(transformation_feature.values())
df_transformation.dtypes
# Checking whether data is normally distributed
a=stats.probplot(df_transformation.weightgainedgrams, dist = "norm", plot = pylab)

stats.probplot(df_transformation.Caloriesconsumed, dist = "norm", plot = pylab)

# Transformation to make workex variable normal by using log()
stats.probplot(np.log(df_transformation.weightgainedgrams), dist = "norm", plot = pylab)

# Original data
prob = stats.probplot(df_transformation.weightgainedgrams, dist = stats.norm, plot = pylab)

#Boxcox Transform training data & save lambda value
fitted_data, fitted_lambda = stats.boxcox(df_transformation.weightgainedgrams)

# creating axes to draw plots
fig, ax = plt.subplots(1, 2,figsize=(12,5))

# Plotting the original data (non-normal) and fitted data (normal)
sns.distplot(df_transformation['weightgainedgrams'], hist = False, kde = True,
             kde_kws = {'shade': True, 'linewidth': 2},
             label = "Non-Normal", color = "green", ax = ax[0])

sns.distplot(fitted_data, hist = False, kde = True,
             kde_kws = {'shade': True, 'linewidth': 2},
             label = "Normal", color = "green", ax = ax[1])

# adding legends to the subplots
plt.legend(loc = "upper right")

plt.show()
# rescaling the subplots
fig.set_figheight(5)
fig.set_figwidth(10)

print(f"Lambda value used for Transformation: {fitted_lambda}")



# Transformed data
prob = stats.probplot(fitted_data, dist = stats.norm, plot = pylab)

# Original data
prob = stats.probplot(df_transformation.weightgainedgrams, dist = stats.norm, plot = pylab)

from feature_engine import transformation

# Set up the variable transformer
tf = transformation.YeoJohnsonTransformer(variables = 'weightgainedgrams')

edu_tf = tf.fit_transform(df_transformation)

# Transformed data
prob = stats.probplot(edu_tf.weightgainedgrams, dist = stats.norm, plot = pylab)

'''
Standardization problem statement.docx
Q8)
Problem Statement: 
Prepare the dataset by performing the preprocessing techniques, to have the standard scale to data.
'''
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import pylab
import numpy as np
# Read data into Python
df_standardazation = pd.read_excel(r"F:\Liser Time\360digitmg\2.EDA\Assignments\5.Data Preprocessing\Problem Statement (2)\Data_Preprocessing_assignment_dataset\standardization_normalization.xlsx")
df_standardazation.dtypes
transformation_feature = {'Name of feature':['weightgainedgrams','Caloriesconsumed'],
                   'Desription': ['weight of grams','calories consumed'],
                   'Type':['continous','Discrete'],
                   'Relevance':[]
                   }
print(transformation_feature.values())
### Standardization
from sklearn.preprocessing import StandardScaler
# Initialise the Scaler
scaler = StandardScaler()

# To scale data
df = scaler.fit_transform(df_standardazation)
# Convert the array back to a dataframe
dataset = pd.DataFrame(df)
res = dataset.describe()

# Normalization
''' Alternatively we can use the below function'''
from sklearn.preprocessing import MinMaxScaler
minmaxscale = MinMaxScaler()

df_n = minmaxscale.fit_transform(df_standardazation)
dataset1 = pd.DataFrame(df_n)

res1 = dataset1.describe()

'''Robust Scaling
Scale features using statistics that are robust to outliers'''

from sklearn.preprocessing import RobustScaler

robust_model = RobustScaler()

df_robust = robust_model.fit_transform(df_standardazation)

dataset_robust = pd.DataFrame(df_robust)
res_robust = dataset_robust.describe()

'''
String Manipulation.docx
Q9)
Problem Statement: 
Prepare the dataset by performing the preprocessing techniques, to have the standard scale to data.
'''

#1.Create a string “Grow Gratitude”.
#Code for the following tasks:
import re
string = 'Grow Gratitude'
#a)How do you access the letter “G” of “Growth”?
first_letter = string[0]
print(first_letter)
#b)How do you find the length of the string?
length_string = len(string)
print(length_string)
#c)Count how many times “G” is in the string?
count_g = string.count('G')
print(count_g)

#2.Create a string “Being aware of a single shortcoming within yourself is far more useful than being aware 
#of a thousand in someone else.”
#Code for the following:
   string_2 ='Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.'   
#a)Count the number of characters in the string.
count_s = len(string_2)
print(count_s)

list_1 = string_2.split()
print(len(list_1))

#3.Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
#Code for the following tasks:

s_3 = 'Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth'    
list_2 = s_3.split()
#a)get one char of the word
char = s_3[0]
print(char)
#b)get the first three char
char = s_3[0:3]
print(char)
#c)get the last three char
char = s_3[-4:-1]
print(char)

#4.create a string "stay positive and optimistic". Now write a code to split on whitespace.
#Write a code to find if:
 s_4 = 'stay positive and optimistic'    
 list_3 = s_4.split()
 print(list_3)
#a)The string starts with “H”
a = s_4.startswith('H')
print(f'The string starts with H is:{a}')
#b)The string ends with “d”
b = s_4.endswith('d')
print(f'The string starts with d is:{b}')
#c)The string ends with “c”
c = s_4.endswith('c')
print(f'The string starts with c is:{c}')


#5.Write a code to print " 🪐 " one hundred and eight times.
x= "🪐"
#by using lambda function
jupyter = lambda x: x * 108
result = jupyter(x)
print(result)
#by using if clause
if 1 == 1:
    print(x*108)
    
#6.Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”

str_1 ='Grow Gratitude'
replaced_str = str_1.replace('Grow','Growth of')
print(replaced_str)

#7.A story was printed in a pdf, which isn’t making any sense. i.e.:
#“.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”

#You have noticed that the story is printed in a reversed order. Rectify the same and write a code to print the same story in the correct order.

story = '.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A'

crt_story = ''.join(reversed(story))
print(crt_story)
#len(story)
crt_story_1 = story[ :: -1]
print(crt_story_1)























