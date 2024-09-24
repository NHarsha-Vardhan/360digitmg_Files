'''power bi preprocessing'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler

#from sklearn.model_selection import train_test_split
#from sklearn.tree import DesicionTreeClassifier as DT
#from sklearn.metrics import accuracy_score
#from sklearn.model_selection import GridSearchCV
#import joblib
#import pickle

df = pd.read_excel(r'F:\Liser Time\360digitmg\4.PowerBI\data sets for assignment\Sample - Superstore.xlsm')
df_backup = df
df['Postal Code'] = df['Postal Code'].astype('str')
df.dtypes
column_names = list(df.columns.values)
print(column_names)
df.info()
#checking whether data is having duplicate or not!

duplicate = df.duplicated().sum()
df_duplicates = df.drop_duplicates(subset='Order ID', keep='first')

sum(df_duplicates)

#cleaned_df = df.drop_duplicates(subset=relevant_columns, keep='first')

df.isnull().sum()
df.describe()
#applying imputation if any null values

# Mean Imputer 
#mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
#df["Salaries"] = pd.DataFrame(mean_imputer.fit_transform(df[["Salaries"]]))

# Detection of outliers (find limits for salary based on IQR)
IQR = df['Sales'].quantile(0.75) - df['Sales'].quantile(0.25)

lower_limit = df['Sales'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['Sales'].quantile(0.75) + (IQR * 1.5)


numeric_df = df.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()
plt.boxplot(df['Sales'])
sns.boxplot(df['Sales'])
sns.boxplot(df['Quantity'])
sns.boxplot(df['Discount'])
sns.boxplot(df['Profit'])

Winsor_iqr = Winsorizer(capping_method='iqr',
                        #choose iqr rule boundaries or gaussian for mean and std
                        tail = 'both',#cap left ,right or both tails
                        fold = 1.5,
                        variables= ['Sales']
                        )


df["Sales"] = Winsor_iqr.fit_transform(df[['Sales']])
df['Sales_winsorized'] = Winsor_iqr.fit_transform(df[['Sales']])

sns.boxplot(df['Sales_winsorized'])

# Get the removed outliers
#removed_outliers = Winsor_iqr.right_tail_caps_  # or left_tail_caps_ for left-tail outliers

#print("Removed outliers (upper bounds):", removed_outliers)

# Identify the rows affected by Winsorization
outlier_indices = df[df['Sales'] != df['Sales_winsorized']].index

removed_outliers_df = df.loc[outlier_indices]

# Filter the DataFrame to include only non-outlier data
non_outliers_df = df[df['Sales'] == df['Sales_winsorized']].copy()

# Remove the 'Sales_winsorized' column from the original DataFrame
df.drop(columns=['Sales_winsorized'], inplace=True)

removed_outliers_df.drop(columns=['Sales_winsorized'], inplace=True)

non_outliers_df.drop(columns=['Sales_winsorized'], inplace=True)

removed_outliers_df.info()
sns.boxplot(df['Sales'])
sns.boxplot(non_outliers_df['Sales'])

# Remove the 'Sales_winsorized' column
non_outliers_df.drop(columns=['Sales_winsorized'], inplace=True)
df = non_outliers_df
non_outliers_df.dtypes
non_outliers_df.info() 


# Define the model with Gaussian method
winsor_gaussian = Winsorizer(capping_method = 'gaussian', 
                             # choose IQR rule boundaries or gaussian for mean and std
                          tail = 'both', # cap left, right or both tails 
                          fold = 3,
                          variables = ['Sales']
                          )

df["Sales"] = Winsor_iqr.fit_transform(df[['Sales']])
df['Sales_winsorized'] = Winsor_iqr.fit_transform(df[['Sales']])

sns.boxplot(df['Sales_winsorized'])

# Identify the rows affected by Winsorization
outlier_indices_gaussian = df[df['Sales'] != df['Sales_winsorized']].index

removed_outliers_df_gaussian = df.loc[outlier_indices_gaussian]

# Filter the DataFrame to include only non-outlier data
non_outliers_df_gaussian = df[df['Sales'] == df['Sales_winsorized']].copy()

# Remove the 'Sales_winsorized' column from the original DataFrame
df.drop(columns=['Sales_winsorized'], inplace=True)

removed_outliers_df_gaussian.drop(columns=['Sales_winsorized'], inplace=True)

non_outliers_df_gaussian.drop(columns=['Sales_winsorized'], inplace=True)

df = non_outliers_df_gaussian
removed_outliers_df.info()
sns.boxplot(df['Sales'])
sns.boxplot(df['Sales'])


df_t = winsor_gaussian.fit_transform(df[['Salaries']])
sns.boxplot(df_t.Salaries)



if df['Sales'].equals(df_backup['Sales']):
    print("Both DataFrames have the same values.")
else:
    print("The DataFrames have different values.")



file_path = 'filtered_Original_data.xlsx'

# Convert DataFrame to Excel
df.to_excel(file_path, index=False)


file_path_1 = 'removed_outliers_iqr.xlsx'
removed_outliers_df.to_excel(file_path_1, index=False)



file_path_2 = 'removed_outliers_gaussian.xlsx'
removed_outliers_df_gaussian.to_excel(file_path_2, index=False)




plt.scatter(x=df['Sales'], y=df['Profit'] )


df_1 = pd.read_excel(r'F:\Liser Time\360digitmg\4.PowerBI\Assignments\4.Data visualization\filtered_Original_data.xlsx')


plt.scatter(x=df_1['Sales'], y=df_1['Profit'] )

sns.boxplot(df_1['Sales'])
sns.boxplot(df_1['Profit'])

############################
'''After Removing the Sales Outliers'''
############################


# Detection of outliers (find limits for salary based on IQR)
IQR_Profit = df_1['Profit'].quantile(0.75) - df_1['Profit'].quantile(0.25)

lower_limit_profit = df_1['Profit'].quantile(0.25) - (IQR * 1.5)
upper_limit_profit = df_1['Profit'].quantile(0.75) + (IQR * 1.5)


# Detection of outliers (find limits for salary based on IQR)
IQR_Sales = df_1['Sales'].quantile(0.75) - df_1['Sales'].quantile(0.25)

lower_limit_Sales = df_1['Sales'].quantile(0.25) - (IQR * 1.5)
upper_limit_Sales = df_1['Sales'].quantile(0.75) + (IQR * 1.5)

sales = {'IQR':IQR_Sales,'lower':lower_limit_Sales,'upper':upper_limit_Sales}
profit =  {'IQR':IQR_Profit,'lower':lower_limit_profit,'upper':upper_limit_profit}


# Define the model with Gaussian method
winsor_gaussian = Winsorizer(capping_method = 'gaussian', 
                             # choose IQR rule boundaries or gaussian for mean and std
                          tail = 'both', # cap left, right or both tails 
                          fold = 3,
                          variables = ['Profit']
                          )

#df_1["Profit"] = winsor_gaussian.fit_transform(df[['Profit']])
df_1['Sales_winsorized'] = winsor_gaussian.fit_transform(df_1[['Profit']])

sns.boxplot(df_1['Sales_winsorized'])



# Identify the rows affected by Winsorization
outlier_indices_gaussian = df_1[df_1['Profit'] != df_1['Sales_winsorized']].index

removed_outliers_df_gaussian_profit = df_1.loc[outlier_indices_gaussian]

# Filter the DataFrame to include only non-outlier data
non_outliers_df_gaussian_profit = df_1[df_1['Profit'] == df_1['Sales_winsorized']].copy()

# Remove the 'Sales_winsorized' column from the original DataFrame
df_1.drop(columns=['Sales_winsorized'], inplace=True)

removed_outliers_df_gaussian_profit.drop(columns=['Sales_winsorized'], inplace=True)

non_outliers_df_gaussian_profit.drop(columns=['Sales_winsorized'], inplace=True)

df_1 = non_outliers_df_gaussian_profit
removed_outliers_df.info()
sns.boxplot(df_1['Sales'])
sns.boxplot(df_1['Profit'])

# Convert DataFrame to Excel
df.to_excel(file_path, index=False)


file_path_1 = 'removed_outliers_gaussian_profit.xlsx'
removed_outliers_df_gaussian_profit.to_excel(file_path_1, index=False)



file_path_2 = 'outlier_after_profit.xlsx'
df_1.to_excel(file_path_2, index=False)




plt.scatter(x=df_1['Sales'], y=df_1['Profit'] )
sns.boxplot(df_1['Sales'])
sns.boxplot(df_1['Profit'])

#df_2 = pd.read_excel(r'F:\Liser Time\360digitmg\4.PowerBI\Assignments\4.Data visualization\removed_outliers_gaussian.xlsx')

















