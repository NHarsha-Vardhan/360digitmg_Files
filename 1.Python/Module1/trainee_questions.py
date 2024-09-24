'''Python Contact Doubts to anaconda contact through
https://www.anaconda.com/contact
'''
'''Python_Reference Material '''

#================================================================================#

#================================================================================#
#1.Write a function to check if a given string is palindrome or not
'''string is palindrome or not'''
def isPalindrome(s):
    """Check if a string is a palindrome."""
    rev = map(lambda x: x == x[::-1], s)
    return list(rev)

# Example: Check if each string in the list is a palindrome
string_list = ['abcde', 'radar']
result = isPalindrome(string_list)
print(result)

#2.Write a function to calculate the factorial of number
'''Number of factorial '''
def fact(N):
  if N < 0:
    print("Input the positive number")
  elif N == 0:
    print(f'Factorial of {N}! is {1}')
  elif N == 1:
    return 1
  else:
    return (N * fact(N-1))
    
fact(5)

#3.Write a function to check if a given number is prime.
'''function to check given number is prime'''
def is_prime_1(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime_1(4))


#================================================================================#
'''22-12-2023'''
#================================================================================#
#1.Difference between generator and function with example
'''Generator :'''
    Generator is a object that yeilds a sequence of values using "yeild" method
def squence(N):  
  for i in range(N):
      yield i
    

blist = squence(100000)
print(blist)

print(next(blist))


'''Functions:'''
    functions are used to reduce the code
# Simple function 
def squence(N):
  x = []
  for i in range(N):
    x.append(i)
  return x

alist = squence(10000)

print(alist)
  
    
#2.Difference between SEARCH and MATCH
'''SEARCH'''
search is used the search the any  kind of words.
'''MATCH'''
match is used to get the simialr kind of words.

#3.Explain the concept of parameter passing in python functions & What is the difference between positional parameter and keyword arguments 
#Provide the example 
In python functions parameter passing is used to help in buliding the arguments make less code.
positinal arguments is giving the values in a function stutured format
In keyword arguments it will help to pass the multiple paramters values.

#4.Explain  using " return " and print within the function Provide an example for each.
'''return keyword in function'''
def add(a,b):
    c=0
    c=a+b
    return c
add(5,6)

return keyword is used to return values mentioned in function.

#5.Define a function named multiply and that takes two parameters a and b and returns their product.

def multiply(a,b):
    return a*b
multiply(5,3)

#6.If a given number is prime , generate the first 10 numbers in the fibonacci sequences.
'''Printing the fibonacci series based on whether prime number'''
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_fibonacci(limit):
    """Generate the first n numbers in the Fibonacci sequence."""
    a,b = 0,1
    while a<limit:
        yield a
        a,b = b,a+b


# Example: Check if 7 is prime and generate the first 10 Fibonacci numbers
number_to_check = 7
if is_prime(number_to_check):
    fibonacci_sequence = generate_fibonacci(10)
    print(f"The first 10 Fibonacci numbers for the prime number {number_to_check}:")
    for number in fibonacci_sequence:
            print(number)

else:
    print(f"{number_to_check} is not a prime number.")

#7.Use List comprehension to create a list of squares of even numbers from 1 to 10.                                    

list_comprehension = [ i**2 for i in range(0,10)  if i%2==0]               
print(list_comprehension)

########################################################
'''27-12-2023'''
####################

# what does the the findall() function do in python

findall is used to find the given string from left to right and returned in ordered.

# How do you use groups in regular expressions

groups is used to give the ouput in tuple format.

# diffrenece between the match and search

match is used to regex pattern it returns true if match is found otherwise false.

where search is used to match object if there is a match is found in the string.

# How can you use the re module in python search for a pattern in a string

re.search() function searches for a pattern any where in a string.

###################################
'''29-12-2023'''
################################
# creating the array
from array import *
import numpy as np
import pandas as pd

T = np.array([[1,2,3,4,5],[5,4,3,2,1]])
T[0]
type(T)
#1. create a numpy array from 1-10
a= np.arange(10)
a=np.array(a)
# calculating the mean and standard deviation of array
a.mean()
a.std()
#2. calculate the dot product of 2 arrays

print(a)
b= np.array([np.arange(10)])
a_reshaped = a.reshape(10, 1)
print(a_reshaped)
c = a_reshaped.dot(b)
print(c)

#3.write a function that takes a numpy array as input and returns a new array containing only the unique elements

def function1(a):
    unique_elements = np.unique(a)
    print(unique_elements)
   
arr1 = np.array([1,1,2,3,3])
result = function1(arr1)

#4. Load the CSV file into the pandas dataframe .Display first 5 rows of the data frame.
education = pd.read_csv(r"F:/Liser Time/360digitmg/Python/Module1/Assignments/problem statement-08/datasets/education.csv")
education.head()

#5. given a pandas dataframe with columns 'Name' Age and salary filter the rows where the age is greater than 25 
#and the salary less than 50000

import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [22, 30, 25, 28],
        'Salary': [45000, 60000, 48000, 55000]}

df = pd.DataFrame(data)
df
# Filtering rows based on conditions
filtered_df = df[(df['Age'] > 25) & (df['Salary'] < 50000)]
filtered_df
# Display the result
print("Filtered DataFrame:")
print(filtered_df)


#6. group a pandas dataframe by a specific column and calculate the mean value for each group 

import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Value': [10, 15, 20, 25, 30, 35]}

df = pd.DataFrame(data)
df

# Group by 'Category' and calculate the mean for each group
mean_by_category = df.groupby('Category')['Value'].mean()

# Display the result
print(mean_by_category)

df = pd.DataFrame(columns =['x1','x2','x3'],index=[201,202,203])
print(df)
df['x1'] = [10,20,30]
df['x2'] = [1,2,3]
df['x3'] = [3,2,1]


############################

'''02-01-2024'''
###########################

#1. What specific business goals does your orgiazation aim to achieve through data analysis.
Informed Decision-Making:

Use data analysis to provide decision-makers with insights and information to make informed and strategic decisions.
Improved Operational Efficiency:

Identify areas for process improvement and optimization through the analysis of operational data.
Customer Insights and Personalization:

Understand customer behavior and preferences to enhance customer experiences, and tailor products and services to individual needs.
Risk Management:

Analyze data to identify potential risks, fraud, or anomalies, and implement strategies to mitigate them.
Revenue Growth:

Use data analysis to identify new business opportunities, target specific markets, and optimize pricing strategies to drive revenue growth.
Cost Reduction:

Identify cost-saving opportunities through the analysis of operational and financial data.
Market Research and Competitive Intelligence:

Analyze market trends, competitor activities, and consumer sentiment to stay competitive in the market.
Product Development and Innovation:

Utilize data to inform the development of new products or services and improve existing ones based on customer feedback and market trends.
Employee Productivity and Engagement:

Analyze workforce data to enhance employee productivity, satisfaction, and retention.
Compliance and Governance:

Ensure compliance with regulations and industry standards through the analysis of relevant data, minimizing legal and regulatory risks.
These goals can vary depending on the industry, the size of the organization, and its specific challenges and objectives.
Data analysis plays a crucial role in helping organizations extract valuable insights from their data, enabling them to achieve 
these goals and stay competitive in a data-driven business environment.

#2.How is data currently managed to and processed with in your organization from collection to storage and analysis 
The methods and technologies organizations use to manage and process data can vary widely based on their industry, size, and specific needs. However, I can provide a general overview of the typical stages involved in data management and processing:

Data Collection:

Organizations collect data from various sources, such as customer interactions, transactions, sensors, social media, and more. Data may be structured (e.g., databases), semi-structured, or unstructured.
Data Storage:

Data is stored in databases, data warehouses, or data lakes. The choice of storage depends on factors like the volume, variety, and velocity of the data. Cloud-based solutions are increasingly popular for scalable and flexible storage.
Data Cleaning and Preprocessing:

Raw data often requires cleaning and preprocessing to handle missing values, outliers, and inconsistencies. This stage ensures that the data is suitable for analysis.
Data Integration:

In some cases, data from multiple sources needs to be integrated for a comprehensive view. ETL (Extract, Transform, Load) processes are commonly used for this purpose.
Data Analysis:

Data analysts and data scientists use various tools and techniques to analyze the data. This could involve descriptive statistics, machine learning algorithms, or other statistical methods depending on the goals of the analysis.
Data Visualization:

Visualizations, such as charts and graphs, are often created to communicate insights and trends effectively.
Data Storage and Retrieval:

Analyzed data or derived insights may be stored for future reference or used to update business intelligence dashboards. Results may also be fed back into operational systems.
Security and Compliance:

Organizations implement security measures to protect sensitive data. Compliance with data protection regulations is crucial, especially when handling personal or sensitive information.
Continuous Improvement:

Organizations regularly assess and refine their data management and processing strategies. This includes evaluating new technologies, improving data quality, and adapting to changing business needs.

Its important to note that advancements in technologies, such as cloud computing, big data processing frameworks, and machine learning tools, continue to shape how organizations manage and analyze data. For the most accurate 
and up-to-date information about a specific organization, its recommended to refer to their official documentation or statements.

#3.What are the primary sources of data that drive desicion making in your business, how is data quality assured

data that drive decision-making in businesses and how data quality is typically assured:

Customer Interactions:

Customer data from various touchpoints, such as sales transactions, customer support interactions, and feedback, provides insights into customer behavior and preferences.
Sales and Revenue Data:

Data related to sales performance, revenue, and profitability helps businesses understand the financial health of the organization and identify opportunities for growth.
Market Research and Surveys:

Information gathered from market research, customer surveys, and feedback helps businesses stay informed about market trends, competitor activities, and customer satisfaction.
Operational Data:

Internal operational data, including supply chain information, production data, and logistics data, supports decision-making related to operational efficiency and resource allocation.
Financial Data:

Financial statements, budget data, and cost-related information are critical for financial decision-making, budgeting, and forecasting.
Social Media and Online Presence:

Data from social media platforms, website analytics, and online interactions provide insights into brand perception, marketing effectiveness, and customer engagement.
Employee Performance and HR Data:

HR data, including employee performance metrics, turnover rates, and workforce demographics, assists in workforce planning, talent management, and employee engagement initiatives.
Supply Chain Data:

Information about the supply chain, including supplier performance, inventory levels, and production schedules, helps optimize the supply chain and minimize disruptions.
Ensuring Data Quality:

Data Governance: Implementing data governance practices helps define standards, policies, and procedures for data management, ensuring consistency and accuracy.

Data Validation and Cleaning: Regularly validating and cleaning data to identify and correct errors, inconsistencies, or missing values is crucial for maintaining data quality.

Data Security: Implementing robust security measures protects data from unauthorized access and ensures data integrity.

Documentation: Proper documentation of data sources, definitions, and transformations facilitates understanding and reduces the likelihood of errors.

Data Quality Metrics: Establishing key performance indicators (KPIs) for data quality and regularly monitoring these metrics helps identify and address issues promptly.

User Training: Ensuring that users who interact with data are trained on data quality standards and best practices promotes a culture of data quality throughout the organization.

Data Audits: Periodic data audits and assessments help identify areas for improvement and ensure ongoing data quality.

Every organization may have unique sources of data and approaches to ensuring data quality based on its industry, size, and specific needs. The above practices provide a foundation for maintaining high-quality data that supports effective decision-making.


#4.Can you describe the typical desicion making processes with in your organization and the role data plays in these processess.
Identifying Decision Needs:

Organizations begin by identifying the decisions that need to be made. These could range from strategic decisions at the executive level to operational decisions at lower levels of the organization.
Defining Decision Criteria:

Criteria are established to evaluate potential options. These criteria could include financial metrics, market conditions, risk factors, and other relevant aspects depending on the nature of the decision.
Data Collection and Integration:

Relevant data is collected from various sources. This could include internal databases, external market data, customer feedback, and other information deemed critical for the decision at hand. Data integration may involve combining data from multiple sources to create a comprehensive view.
Data Cleaning and Preprocessing:

Raw data often requires cleaning and preprocessing to address issues such as missing values, outliers, and inconsistencies. This step ensures that the data used for decision-making is accurate and reliable.
Data Analysis:

Statistical analysis, machine learning, and other analytical methods are applied to extract insights from the data. This step helps organizations understand patterns, trends, and correlations that inform decision-makers.
Data Visualization:

Visualizations such as charts, graphs, and dashboards are created to present complex data in a comprehensible format. Visualizations aid decision-makers in understanding the implications of the data.
Scenario Analysis and Modeling:

Organizations may use scenario analysis and modeling to simulate different outcomes based on varying assumptions. This helps decision-makers assess the potential impact of different courses of action.
Decision-Making Meetings:

Decision-makers convene to review the analyzed data, discuss insights, and make informed decisions. These meetings may involve collaboration among different departments and levels of the organization.
Implementation and Monitoring:

After a decision is made, it is implemented, and the impact is monitored. Organizations may use key performance indicators (KPIs) to track the success of the decision over time.
Feedback Loop:

Decision-making processes often include a feedback loop where the outcomes of decisions are assessed, and lessons learned are used to improve future decision-making.
Data plays a central role in this process by providing evidence-based insights, supporting informed decision-making, and enabling organizations to adapt to changing circumstances. The integration of data-driven decision-making is a key aspect of creating a more agile and responsive organizational culture.

#5.what are the key challanges or obstacles your organization faces in effectively utilizing data for business insights.
Data Quality and Consistency:

Inaccurate or inconsistent data can lead to flawed insights. Ensuring data quality and consistency across different sources and systems is a persistent challenge.
Data Security and Privacy:

Organizations need to balance the need for data access with maintaining data security and privacy, especially when dealing with sensitive information.
Data Integration:

Integrating data from diverse sources, which may have different formats and structures, can be complex. This challenge often arises in creating a unified view of the organization's data.
Lack of Data Governance:

Absence or inadequate implementation of data governance policies can result in issues related to data ownership, accountability, and overall management.
Limited Skills and Expertise:

The shortage of skilled professionals who can analyze and interpret data is a common challenge. Organizations may face difficulties in recruiting and retaining data scientists, analysts, and other experts.
Legacy Systems and Infrastructure:

Legacy systems that are not designed for modern data analytics can hinder the organization's ability to leverage new technologies and processes effectively.
Resistance to Cultural Change:

Encouraging a data-driven culture may face resistance from employees who are accustomed to traditional decision-making processes. Overcoming this resistance requires effective change management.
Scalability Issues:

As data volumes grow, organizations may encounter scalability issues in terms of storage, processing power, and analytical capabilities.
Cost Constraints:

Investing in the necessary technology, infrastructure, and talent for effective data utilization can be costly. Budget constraints may limit the organization's ability to make these investments.
Regulatory Compliance:

Compliance with data protection regulations, such as GDPR, HIPAA, or industry-specific standards, poses challenges for organizations, especially those operating in multiple jurisdictions.
Keeping Up with Technology Advancements:

The rapidly evolving landscape of data analytics technologies requires organizations to stay updated and invest in training to keep their teams proficient.
Defining Clear Objectives:

Setting clear and achievable goals for data-driven initiatives is crucial. Lack of well-defined objectives can lead to misalignment and ineffective use of resources.
Its important to note that addressing these challenges requires a holistic and strategic approach, involving collaboration across different departments, leadership support, and a commitment to ongoing improvement. Organizations that successfully navigate these challenges are better positioned to derive valuable insights from their data.

########################
'''03-01-2024'''
#######################
#1. what is first moment of business desicion 
Explotatry data analytics / Measures of central tendecy 

#2. what is secound moment of business desicion
Measures of dispersion
#3. what is third moment of business desicion and formula
finding out the skewness.
skew()
#4.what is the 4th moment of business desicion and formula
Finding out the kurtness 
kurt()
#########################
'''04-01-2024'''
########################
#1. what are the methods used in  winsorization 
from feature_engine.outliers import Winsorizer
They are 3 types of winsorization :
    a)IQR
winsor_iqr = Winsorizer(capping_method = 'iqr', 
                        # choose  IQR rule boundaries or gaussian for mean and std
                          tail = 'both', # cap left, right or both tails 
                          fold = 1.5, 
                          variables = ['Salaries'])
    
    b) Gaussian 
# Define the model with Gaussian method
winsor_gaussian = Winsorizer(capping_method = 'gaussian', 
                             # choose IQR rule boundaries or gaussian for mean and std
                          tail = 'both', # cap left, right or both tails 
                          fold = 3,
                          variables = ['Salaries'])
    
    c) Quantiles

winsor_percentile = Winsorizer(capping_method = 'quantiles',
                          tail = 'both', # cap left, right or both tails 
                          fold = 0.05, # limits will be the 5th and 95th percentiles
                          variables = ['Salaries'])

df_p = winsor_percentile.fit_transform(df[['Salaries']])

#2. Explain the Trimming , swamping , and masking.
Trimming :
    Trimming typically refers to the process of removing unwanted or excess parts from something.
    e.g: In statistics, trimming can sometimes refer to the removal of a certain percentage of extreme values (outliers) from a dataset to reduce their influence on statistical measures.
swamping:
    Swamping generally means overwhelming or dominating something.
    e.g: In the context of machine learning, swamping might be used to describe a situation where the effect 
    of one feature overwhelms the impact of other features in a predictive model, leading to skewed results.    
Masking:
    Masking typically involves covering or concealing something.
    e.g:  In statistics, masking could refer to the situation where the presence of one variable hides the effect 
    of another variable, leading to difficulty in identifying the true relationship between variables.    
    
#3.How much fold will we take in IQR method 
In IQR we will fold 1.5 i.e 75%

#4. Explain 3R techniques:
    Rectify , Retain , Remove.

####################
'''05-01-2023'''
####################
#1. what is an outlier in a data set ,a nd how can be identified
An outlier is an null value which will be in null values in data set i.e represented in NA form.
#2.why are outliers considered important in statsical analysis analysis and data modeling
Outliers will play crucial role while in statstical analysis and data modeling because based on that the data cruciality 
depends.


##################
'''08-01-2024: EDA'''
##################
#1. Explain the transformation techniques in detail and purpose of using each one
They are 2 kinds of transformations:
a) Logarthamatic Transformation
b) Exponential Transformation

They are 5 types of Tranformations:
a) Power Transformation 
b) square, cube and Polynomial Transformation
c) Reciprocial Tranformation
d) Box-Cox Tranformation
e)Yeo-Johnson Tranformation    
#2. What is Data Scaling
It nothing but shrinking of data.It is mostly used in the machine learning to shrink and explain the data while training to model.
Types are:
    Normalization/ Min-Max scalar/ Range method
    Standardization 
    Robust Scaling 
#3.Explain the formula of normailization.    
Formula: X-min(X)/max(X) - min(X)
#4. Explain the formula of standirization.
Formula: X - mean(X) / stdev(X)
#5. Explain the formula for Robust scaling 
Formula: X-median(X)/IQR
################
'''09-01-2024 -> Revision on numpy and pandas '''
###############
# Reading the file from cloud through pandas
import pandas as pd
excel_file_url = 'https://docs.google.com/spreadsheets/d/1EEgUlxiX3dRX2H-lLRlqRHrrFaiUovCj/edit?usp=drive_link&ouid=114958149974290883966&rtpof=true&sd=true'#
df =pd.read_excel(excel_file_url, engine='openpyxl')#
print(df)


###############
'''10-01-2024'''
##############
# Ecxplain the auto EDA and there concepts and types with commands
'''In Auto they are 5 types :
     1.Sweetviz
     2.Autoviz
     3.Dtale
     4.Pandas Profiling
     5.Dataprep'''
     
#1.Sweetviz
import sweetviz as sv

s = sv.analyze(df)
s.show_html()

#2.Autoviz
from autoviz.AutoViz_Class import AutoViz_Class

av = AutoViz_Class()
a = av.AutoViz(r"F:\Liser Time\360digitmg\2.EDA\Data Sets\education.csv", chart_format = 'html')
 
#3.Dtale
import dtale
d = dtale.show(df)
d.open_browser()  

#4.pandas Detailing
from pandas_profiling import ProfileReport 
p = ProfileReport(df)

p.to_file("output.html")

#5.Data prep

from dataprep.eda import create_report

report = create_report(df, title = 'My Report')

report.show_browser()    
##########
'''11-01-2024 Revise concepts on EDA business concepts'''
##########
 '''12-01-2024 Hands on EDA & Data Preprocessing'''
##########  

import pandas as pd 
import numpy as np
import seaborn as sns

cars = pd.read_csv(r'F:\Liser Time\360digitmg\2.EDA\Data Sets\InClass_DataPreprocessing_datasets\Cars.csv')

cars.info()

''' Data type category:
HP , VOL is discrete 
SP , MPG and WT is continous
'''
#EDA (1st Business Moment)

cars.mean()
cars.median()
cars.mode()

#Measures of Dispersion(2nd Business Moment)

cars.var()
cars.std()

# 3rd moment business decision
cars.skew()
# 4th moment business decision
cars.kurt()

# data Preprocessing

#help(cars.astype)
# converting the int64 to str
cars.HP = cars.HP.astype('str')
cars.VOL = cars.VOL.astype('str')

help(cars.duplicated)

# Identifying the duplicates

duplicate = cars.duplicated()  # Returns Boolean Series denoting duplicate rows.
duplicate
sum(duplicate)

# corelation

cars.corr()

cars_1 = cars.drop_duplicates()

'''1.why is data processing important before conducting EDA ?  '''

Importance of Data Processing before EDA:
Data processing is crucial before conducting Exploratory Data Analysis (EDA) for several reasons:

Data Quality: Cleaning and preprocessing data ensure that it is of high quality, reducing errors and inaccuracies in analysis.
Consistency: Standardizing formats and units make data consistent, facilitating meaningful comparisons.
Completeness: Addressing missing values ensures a complete dataset, preventing biased or incomplete analysis.
Normalization: Scaling and transforming variables can enhance comparability and interpretability of results.
Enhanced Analysis: Properly processed data improves the efficiency and effectiveness of subsequent EDA.
    
'''2.what are some common methods for handling missing data during the data preprocessing?  '''

Handling Missing Data:
Common methods for handling missing data during data preprocessing include:

Dropping Rows or Columns: Removing instances or features with missing values.
Imputation: Filling missing values using mean, median, or other statistical measures.
Forward/Backward Fill: Filling missing values with the previous or next available values.
Interpolation: Estimating missing values based on existing data points.
Advanced Techniques: Using machine learning models to predict missing values.

'''3.How does outlier detection contribute to the reliability of findings in EDA?'''
Outlier Detection in EDA:

Improved Accuracy: Identifying and handling outliers prevents skewed results, leading to more accurate findings.
Robust Statistics: Outlier detection ensures that statistical measures are robust and not heavily influenced by extreme values.
Insight into Data Quality: Outliers may indicate errors or anomalies in the dataset, providing insights into data quality.
Enhanced Understanding: Examining outliers helps in understanding the data distribution and potential underlying patterns.
'''4.Explain the role of feature of scaling in improving the results EDA?'''
Role of Feature Scaling in EDA:

Comparability: Scaling ensures that variables with different scales contribute equally to the analysis.
Algorithm Sensitivity: Many machine learning algorithms are sensitive to the scale of features; scaling helps in achieving better results.
Interpretability: Scaled features are easier to interpret and compare, aiding in the understanding of variable contributions.
Enhanced Visualization: Scaling facilitates the visualization of data by preventing domination of certain features due to their scale.
'''5.what visualization techniques are commonly used in EDA to understand the distribution of numerical 
and categorical data?'''
Visualization Techniques in EDA:

Numerical Data:
Histograms: Displaying the distribution of numerical variables.
Box Plots: Visualizing central tendency, spread, and outliers.
Scatter Plots: Illustrating relationships between two numerical variables.
Density Plots: Showing the density of data points along a continuous variable.
Categorical Data:
Bar Charts: Representing the distribution of categorical variables.
Pie Charts: Displaying the proportion of different categories.
Count Plots: Showing the count of observations in each category.
Heatmaps: Visualizing relationships and patterns in a matrix of categorical variables.





###################
'''16-01-2023 SQL''' 
##################

'''
1. what is sql stand for?
'''
sql is strutured query language

'''
2.what is the primary purpose of sql?
'''
The primary purpose of sql is to fetch data from database
'''
3.what arethe main types of sql commands and can you provide examples of each type?
'''
types of sql commands:
    DML,DDL,DCL,TCL
    
'''
4.can you explain the diffrence between the sql and no sql ?
'''    
sql is strutred query language of relational database 
nosql is used to approach the database by key value 

'''
5.craete a database any, create table of 5 columns insert 10 rows atleast?
'''

create database sqldb;
use sqldb;

create table employee(
firstname varchar(20),
lastname varchar(20),
age int,
salary int,
location varchar(20)
);

desc employee;

insert into sqldb.employee (firstname,lastname,age,salary,location) VALUES ('Ram','kumar',25,100000,'Hyd'),('Raj','sigh',30,300000,'Blr');

select * from employee;

select count(distinct location) from employee;
select distinct location from employee;

alter table employee add gender varchar(5);

##############
'''17-01-2023 worked on sql concepts'''
##############
#1 Query to calculate the total sales for each product category and insert the results into a new table named
# "CategorySales" .table: sales"
#Columns:ProductID(int),Category(varchar),SalesAmount(decimal)
#Example Data for 'Sales' table :
#    ProductID  Category     SalesAmount
#    1         'Electronics'  1200.002
#   2         'Electronics'  800.003
#    3         'Clothing'     500.004
#    4         'Clothing'     1000.005
#   5         'Books'        450.006
#    6         'Books'        750.002
    
    

'''-- Create a new table to store total sales for each product category'''
CREATE TABLE category_sales (
	productID REAL NOT NULL PRIMARY KEY,
    product_category VARCHAR(255),
    sales_amount INT
);

#-- Insert the calculated total sales into the new table

INSERT INTO category_sales (productID,product_category, sales_amount) VALUES 
(1,'Electronics',1200.002),(2,'Electronics',800.003),(3,'Clothing',500.004),(4,'Clothing',1000.005),(5,'Books',450.006),(6,'Books',750.002);
SELECT * FROM category_sales;
SELECT product_category, SUM(sales_amount) AS total_sales
FROM category_sales
GROUP BY product_category;


# 2. Retrive the highest paying selling products from each category and display the results in the table:
# of "CategorySales"

#It will give the total sales as per category 
SELECT product_category, SUM(sales_amount) AS total_sales
FROM category_sales
GROUP BY product_category;

#It will give the maximum sales as per category 
SELECT product_category, max(sales_amount) AS maximum_sales
FROM category_sales
GROUP BY product_category;

#3. Insert the average salary of employees in each department in to a table named "DepartmentAvgSalary"
# columns:
#    EmployeeID(int) DepartmentID(int) Salary(decimal)
#    1               101            55000.00
#    2               102            65000.00
#    3               101            60000.00
#    4               103            70000.004
      
#create the table DepartmentAvgSalary
CREATE TABLE DepartmentAvgSalary (
	EmployeeID int  PRIMARY KEY,
    DepartmentID int,
    Salary decimal
);

desc departmentavgsalary;
#inserting the values to the departmentavgsalary 
INSERT INTO departmentavgsalary (EmployeeID,DepartmentID, Salary) VALUES 
(1,101,55000.00),(2,102,65000.00),(3,101,60000.00),(4,103,70000.004);


#4.



##################
'''18-01-2023  worked on sql concepts(datatypes,integrity constraints,autoincrement,composite primary key)'''
##################

#1.what is the primary purpose of   primarykey constraint how it is defined in a table.

primary key is act like the integrity constraint in which it consists both NOTNULL and UNIQUE nature.
create table tablename(
    column_name PRIMARY_KEY
    )

#2.Explain the diffrence between a unique constraint and primary key constraint

a)there can be only 1 primarykey whereas, there can be multiple unique values.
b) primary key cannot be null , whereas unique key could be null.

#3.what is the purpose of NOTNULL constraint in sql, how it is diffrent from CHECK constraint

In SQL, the `NOT NULL` constraint and the `CHECK` constraint serve different purposes, but both are used to enforce data integrity in database tables.

1. **NOT NULL Constraint:**
   - **Purpose:** Ensures that a column cannot contain NULL values.
   - **Usage:** Applied to a specific column when creating or altering a table to specify that the column must always have a value and cannot be left empty.
   - **Example:**
     ```sql
     CREATE TABLE example_table (
         column1 INT NOT NULL,
         column2 VARCHAR(50) NOT NULL
     );
     ```

2. **CHECK Constraint:**
   - **Purpose:** Allows you to specify a condition that must be satisfied for the values in a column.
   - **Usage:** Applied to a specific column when creating or altering a table to enforce a condition on the values in that column.
   - **Example:**
     ```sql
     CREATE TABLE example_table (
         column1 INT CHECK (column1 > 0),
         column2 VARCHAR(50) CHECK (LEN(column2) <= 100)
     );
     ```
     In this example, `column1` must always have a value greater than 0, and `column2` must have a length less than or equal to 100.

**Differences:**
- The `NOT NULL` constraint specifically enforces that a column cannot contain NULL values, ensuring that every row must have a value in that column.
- The `CHECK` constraint allows you to define a broader range of conditions beyond just checking for NULL values. It enables you to specify arbitrary conditions that must be satisfied by the values in a column.

In summary, while the `NOT NULL` constraint focuses on preventing NULL values in a column, the `CHECK` constraint provides more flexibility by allowing you to define custom conditions for the values in a column.

#4.what is foriegn key constraints and why it is important in relational databases? with example.
Foriegn key will plays an important role in RDBMS while we  are combining two tables with a single column 
named ID it is foriegn key with refrence to table A with compared to table B.
    
###############################
'''22-01-2024 worked on sql operators , index and sub-query'''
###############################
#https://www.sqlshack.com/overview-of-the-sql-like-operator/
#1.create a table named "Students" with columns Student_Id(Auto incrementing ,primary key),firstname,lastname,age.
#Define a constraint to ensure that Age column must be greater than 18 and insert values as mentioned.
# student ID  Firstname  Lastname  Age
#   1           John      Doe      20
#   2          Alice     smith     22
#   3          Bob       Johnson   19
#

create table students(
Student_Id int auto_increment ,
firstname varchar(20) ,
lastname varchar(20) ,
age int check (age >18),
primary key(Student_Id)
);
alter table students auto_increment=1;
desc students;
select*from students;
insert into students (Student_Id,firstname,lastname,age) values(1,'John','Doe',20),(2,'Alice','Smith',22),(3,'Bob','Johnson',19);


#2.create orders1 table with columns 



create table orders1(
OrderID int auto_increment ,
CustomerID int ,
orderdate datetime ,
age int check (age >18),
primary key(OrderID)
);
#auto incrementing the orders1 table
alter table orders1 auto_increment=1;
#changing the column in customers table
alter table customers
change column CustomerID  customerid int;
#applying the unique constraint to customers table
ALTER TABLE Customers ADD CONSTRAINT  UNIQUE (email);
#adding the foriegn key to the orders1 table
ALTER table orders1 
add foreign key (CustomerID) references Customers (customerid);
#inserting intothe customers and orders table
insert into customers (customerid,firstname,lastname,email) values(101,'Mary','Smith','mary.smith@email.com'),(102,'John','Doe','john.doe@email.com'),(103,'Alice','Johnson','alice.johnson@email.com');
insert into orders1(OrderID,CustomerID,orderdate) values (1,101,'2023-01-15'),(2,102,'2023-02-10'),(3,103,'2023-03-05');
select * from Customers;
select * from orders1;


########################################
'''23-01-2024  worked on sql joins and sub queries'''
########################################
#create a employee table of mentioned parameters
#EmployeeID	int
#Firstname	varchar(20)
#Lastname	varchar(20)
#Department	varchar(20)
#Salary	int
#departmentid	int
#
#create a department table with mentioned parameters
#departmentid	int
#departmentname	varchar(30)

#1. given 2 tables employees and departments provides an SQL query that retrieves a list of employees 
#and their corresponding department names

select e.Firstname,e.Lastname,e.Department from employee as e 
inner join department as d where e.departmentid = d.departmentid;

#create a customers table of mentioned parameters
#customerid	int
#firstname	varchar(20)
#lastname	varchar(20)
#email	varchar(50)
#create a orders table of mentioned parameters
#OrderID	int
#CustomerID	int
#orderdate	datetime

#2. write a sql statement to find all customers who had placed orders and list their 
# order details .

select c.firstname,c.lastname,o.OrderID from  customers as c inner join orders1 as o 
on c.customerid = o.CustomerID;

#create a product table 
#productID	int
#productname	varchar(20)
#CategoryID	int
#insert the values into the product table
insert into product(productID,productname,CategoryID) values (1,'Laptop',101),(2,'Smartphone',102),(3,'Printer',101);

#create the sales table
#productID	int
#quantity	int
#salesamount	int

insert into sales(productID,quantity,salesamount) values(1,5,25000),(2,2,39000),(3,1,21000);
# 4.fetch the record of product details .
select * from product;

select p.productname,s.quantity,p.productID from product as p inner join sales as s on p.productID =s.productID;

#craete employee1 table
#create table employee1(
#employeeID int ,
#employeename varchar(50),
#managerID int
#);
#insert into employee1 values
#insert into employee1(employeeID,employeename,managerID) values(1,'Alice',NULL),(2,'Bob',1),(3,'Carol',1);

#5.write a sql query to find employees and their managers using the self-join on a Employee1 table
SELECT 
    e.employeeID AS employee_id,
    e.employeename AS employee_name,
    m.managerID AS manager_id,
    m.employeename AS manager_name
FROM 
    employee1 e
JOIN 
    employee1 m ON e.managerID = m.employeeID;
    
########################################
'''24-01-2024  worked on sql triggers '''
########################################

#1.what is the SQL Trigger what is its purpose.

SQL trigger is a procedural code that is automatically executed in response to a certain event to a particular
table.

a.Enforcing Integrity Constraints.
b.Validating Data.
c.Automating Repetitive Tasks.
d.Implementing Business Rules
e.Logging and Auditing
f.Synchronization with Other Tables
g.Data Transformation
i.Enforcing Security Policies
j.Handling Cascading Actions

#2.what are the different types of triggers in SQL,and how do they differ from each other.

In relational database management systems (RDBMS), triggers can be classified based on when they are executed in relation to the triggering event. The main types of triggers are:

1. **BEFORE Triggers:**
   - A BEFORE trigger is executed before the triggering event (e.g., BEFORE INSERT, BEFORE UPDATE, or BEFORE DELETE).
   - It allows the modification of the data about to be affected by the triggering statement.
   - Commonly used for data validation, data modification, or setting default values before an operation.

2. **AFTER Triggers:**
   - An AFTER trigger is executed after the triggering event (e.g., AFTER INSERT, AFTER UPDATE, or AFTER DELETE).
   - It operates on the data after the triggering statement has been executed and can be used for logging changes, updating related records, or triggering additional actions.

3. **INSTEAD OF Triggers:**
   - An INSTEAD OF trigger is an alternative to the default action of a triggering statement (e.g., INSTEAD OF INSERT, INSTEAD OF UPDATE, or INSTEAD OF DELETE).
   - It replaces the default action with a custom set of actions defined in the trigger.
   - Often used with views to allow updates to underlying tables in a controlled manner.

4. **Compound Triggers (Oracle Database):**
   - A compound trigger is a special type of trigger introduced in Oracle Database.
   - It combines multiple triggers (BEFORE, AFTER, INSTEAD OF) into a single structure, simplifying the management of complex logic.

5. **Row-level Triggers:**
   - Row-level triggers are triggered for each row affected by the triggering statement.
   - They are used to perform actions on a per-row basis.

6. **Statement-level Triggers:**
   - Statement-level triggers are triggered once for each triggering statement, regardless of the number of rows affected.
   - They are suitable for actions that need to be performed once for the entire statement.

7. **DML Triggers (Data Manipulation Language):**
   - DML triggers respond to data manipulation events (e.g., INSERT, UPDATE, DELETE).
   - They are associated with changes to the data in a table.

8. **DDL Triggers (Data Definition Language):**
   - DDL triggers respond to changes in the database schema or structure (e.g., CREATE, ALTER, DROP statements).
   - They are used to track changes to the database structure.

It's important to note that the availability and specific syntax of triggers may vary between different database management systems (DBMS) such as Oracle, MySQL, SQL Server, and PostgreSQL. The types mentioned here are generalized concepts, and their implementation details may differ across DBMS platforms.            


#3.How do you create trigger in SQL and what are the key components of a trigger defination.
Here is the basic syntax for creating a trigger in SQL along with key components:
CREATE [OR REPLACE] TRIGGER trigger_name
{BEFORE | AFTER | INSTEAD OF} -- Trigger Timing
{INSERT | UPDATE | DELETE} -- Trigger Event
ON table_name -- Table or View Name
[REFERENCING {OLD AS old | NEW AS new}] -- Referencing Clause (optional)
[FOR EACH {ROW | STATEMENT}] -- Trigger Scope (optional)
WHEN (condition) -- Trigger Condition (optional)
BEGIN
    -- Trigger Body (SQL statements or PL/SQL block)
END;


Let's break down the key components:

CREATE TRIGGER: This is the statement used to create a new trigger.

OR REPLACE: This optional clause allows you to modify an existing trigger with the same name. If the trigger doesn't exist, it will be created.

TRIGGER trigger_name: Specifies the name of the trigger.

Trigger Timing (BEFORE, AFTER, or INSTEAD OF):

BEFORE: Trigger actions are executed before the triggering event.
AFTER: Trigger actions are executed after the triggering event.
INSTEAD OF: For views, replaces the default action with custom actions.
Trigger Event (INSERT, UPDATE, or DELETE): Specifies the triggering event that activates the trigger.

ON table_name: Specifies the name of the table or view on which the trigger is defined.

Referencing Clause (optional):

REFERENCING OLD AS old: Allows access to the old values of the row being modified (for UPDATE and DELETE).
REFERENCING NEW AS new: Allows access to the new values of the row being modified (for UPDATE and INSERT).
Trigger Scope (FOR EACH ROW or FOR EACH STATEMENT):

FOR EACH ROW: Indicates that the trigger should be fired once for each affected row.
FOR EACH STATEMENT: Indicates that the trigger should be fired once for each triggering statement (not applicable to all databases).
Trigger Condition (WHEN): An optional condition that determines whether the trigger should execute based on a specified condition.

BEGIN and END: Delimit the trigger body, which contains the SQL statements or PL/SQL block 
to be executed when the trigger is activated.

#4.what are some common use cases for using the triggers in a database?

a.Enforcing Integrity Constraints.
b.Logging and Auditing
c.Derived Column values
d.Security and Access Control
e.Complex Validation
f.Automatic Record Maintenance
g.Business Rules Enforcement
h.Notification Systems
i.Cross-Table Actions
j.Data Transformation

#5.what are the potential advantages and disadvantages of using triggers in SQL and what are the best 
# pratices for their effective and efficient use?

Advantages of Using Triggers in SQL:
a.Data Integrity:

Triggers help maintain data integrity by enforcing complex business rules and constraints beyond what standard SQL 
constraints can achieve.
b.Automation:

They automate repetitive tasks and actions, reducing the need for manual intervention in certain database operations.
c.Audit Trails:

Triggers enable the creation of audit trails, allowing tracking of changes made to data over time, including who 
made the changes and when.
d.Derived Data:

Triggers facilitate the calculation or derivation of values for specific columns based on changes in other columns,
ensuring consistency.
e.Complex Validation:

They support the implementation of complex validation logic that may involve multiple tables or conditions.
f.Security:

Triggers can be used for implementing security measures, such as row-level security or masking sensitive information.

Disadvantages and Challenges of Using Triggers:
a.Performance Impact:

Poorly designed triggers can have a significant impact on performance, especially when dealing with large datasets.
b.Debugging Complexity:

Debugging triggers can be challenging, and issues may not be immediately apparent. Triggers that involve complex 
logic or reference multiple tables can be harder to troubleshoot.
c.Implicit Actions:

Triggers perform actions implicitly, and developers or administrators may not be immediately aware of the changes
triggered by database operations.
d.Potential for Recursion:

Recursive triggers can occur if a trigger action results in another operation that invokes the same trigger,
leading to unintended consequences.
f.Maintenance Challenges:

As the number of triggers increases, maintenance becomes more challenging. Understanding the interactions and 
dependencies among triggers is crucial.

########################################
'''25-01-2024  worked on views, unions '''
########################################
#1.suppose you have a database with 2 tables "employees","departments" employee with employee_id,employee_name
#department_id and salary.The department with columns department id and department name 
#craete a view to get the columns employee_ID ,employee_name,department name,salary using the joins.

CREATE VIEW employee_info AS
SELECT e.employee_Id,e.employee_name,d.name,e.salary FROM employees as e 
inner join department as d 
where e.department_id = d.id;

SELECT * FROM employee_info;

#2.Write sql query to list all the customer names including the duplicates from two tables customer_a , 
#customer_b

SELECT * FROM customer_a
UNION ALL
SELECT * FROM customer_b;
#3.write a sql query to retrieve a list of unique product names from two tables , product_a, product_b.
#by using UNION operator

SELECT product_name FROM product_a
UNION
SELECT product_name FROM product_b;


########################################
'''30-01-2024  worked on power BI '''
########################################

#1. what is power BI used for ? How can you connect the data sources to powerBI?
1)Power BI:
power bi is web based and app - based.
Intial investment is modest.
Business Users now have access to data thanks ta a self -service tool.
A business model was established by a business model.
Less reliance on IT.
2) How to connect to data sources in power BI:
Open Power BI Desktop:
Launch Power BI Desktop, which is a free application you can download from the Power BI website.
Get Data:
Click on the "Get Data" option in the Home tab.

#2. what are the main components of a components of a power BI report?
1.Power Query
2.Power Map
3.power view
4.power pivot
5.Power BI services 
6.Power BI Q&A
#3.How does the power BI differ  from Excel for data analysis and visulazation?

power BI is cloud based service,Import feature , consolidated view,predictive Functioning, Custom Context Pack
features that difers from the excel.
#4.what is the power BI service and how does it related to power bi desktop?
1)power bi is used to creating and designing reports and dashboards.
2)power bi service is online platforms to helpful in sharing , publishing,and collaboration 

Power BI Desktop is where you design reports, and Power BI Service is where you publish, share, and 
collaborate on those reports in a cloud environment.

########################################
'''01-02-2024  worked on power BI '''
########################################

#1. what is power BI Query Editor ,and why it is important in power BI development?

Power BI Query Editor is Power Query and it is helpful for the transforming.
#2. How can you use powerBI Query Editor to clean and transform data before loading it into your power BI model?
PowerBI Query editor is helpful for performing diffrent operations like merge ,append, cleaning of error and null 
values .
Load Data ,Accessing Query Editor ,Data Cleaning and Transformation,Applied Steps,Preview Changes,Close and Apply
,Refresh Data.

#3.What are the common data transformation tasks you can perform using the Query Editor in power BI?
Filter Rows,Remove Duplicates,Sort Rows,Remove Columns,Keep Columns,Change Data Types,Replace Values,
Split Columns,Merge Columns,Group By,Aggregate Functions,Add Custom Columns,Text Transformations,
Pivot and Unpivot,Extract,Replace Errors,Conditional Columns,Parameterize Queries,Split Rows,Lookup and Reference.


###################################
'''05-02-2024 worked on power BI DAX'''
##################################

#1. what is DAX in power BI and how does it differ from traditional excel formulas ?


DAX is Data analysis Expressions, In power BI , Traditional excelDAX is helped in calculating aggregation
functions and the diffrenece is while handling with large data sets and visulization of multiple graphs is 
possible in power bi is helpful while at other hand excel will be handle limit amount of data sets.
#2. How can you use the DAX to create calculated columns and calculated tables in power BI and what are some use
#cases for these calculations
We can use the calculated columns and tables in power BI by creating with new column and implementing 
use cases such as 
sum,avg,min,sumx,
countx,count,countblank,countrows
and,or,not,if
isblank,isnumber,istext,iserror
date,hour,eomonth,weekday,
concatenate,len,replace,lower.

#3.What is the importance of context in DAX calculationsand how does it affect the result of 
#measure and calculated columns ?

In summary, understanding and managing context in DAX is critical for creating accurate and flexible 
calculations. Its essential to be aware of when you are working in row context and when you are dealing 
with filter context to ensure your DAX expressions provide the desired results in different situations.

Measures:
    Measures are dynamic calculations that can change based on the context in which they are used.
When a measure is used in a table or a visualization, it inherits the filter context from the surrounding environment.
The result of a measure can be different based on the filters or row context in place.

Calculated Columns:
    Calculated columns, on the other hand, are static and are calculated at the time of the creation of the column.
They are not affected by filter context when they are computed, but their values can be influenced by row context when used in calculations.

#4. How can i use DAX functions to perform advanced calculations like time and intelligence ,filteration 
#ranking with power BI when dealing with large datasets or complex calculations?

Performing advanced calculations in Power BI with large datasets or complex scenarios often involves using
a combination of DAX functions. Here are some common scenarios and the DAX functions that can be used:

Time Intelligence:
1.Calculating Year-to-Date (YTD):    
    YTD Sales = TOTALYTD(SUM('Sales'[SalesAmount]), 'Date'[Date])
2.Comparing to Previous Year:

Sales LY = CALCULATE(SUM('Sales'[SalesAmount]), SAMEPERIODLASTYEAR('Date'[Date]))
3.Moving Averages:
    3-Month Avg Sales = CALCULATE(AVERAGE('Sales'[SalesAmount]), DATEADD('Date'[Date], -3, MONTH))

Time-Based Filtering:
Use the DATESBETWEEN or FILTER functions to filter data based on specific date ranges.

Advanced Calculations:
1.Conditional Aggregations:    
    Total Sales = SUM('Sales'[SalesAmount])
Discounted Sales = CALCULATE([Total Sales], 'Sales'[Discount] > 0.1)
2.Percent of Total:

  % of Total Sales = DIVIDE([Total Sales], CALCULATE([Total Sales], ALL('Sales')))

3.Running Totals:

Running Total = CALCULATE([Total Sales], FILTER(ALL('Date'[Date]), 'Date'[Date] <= MAX('Date'[Date])))

Filtering:

1.Top N Items:

Top 10 Products = CALCULATE([Total Sales], TOPN(10, 'Products', [Total Sales], DESC))
2.Dynamic Slicers:
    
Selected Category Sales = CALCULATE([Total Sales], 'Products'[Category] = SELECTEDVALUE('Products'[Category]))

Ranking:
1.Ranking Items:    
Rank = RANKX(ALL('Products'), [Total Sales], , DESC)
2.Ranking with Ties:
Dense Rank = RANKX(ALL('Products'), [Total Sales], , DESC, Dense)
    

When working with large datasets, its crucial to monitor performance and make optimizations as needed.
 Additionally, leveraging Power BIs built-in features, such as aggregations and incremental refresh, can 
 significantly enhance the performance of your reports and dashboards.



###################################
'''06-02-2024 worked on power BI DAX'''
##################################
#path: 'F:\Liser Time\360digitmg\4.PowerBI'
#Filename:onclass2.pbix

#1. How can create the simple dax measure that calculates the total sales amount from a sales table?
Total_sales_1 = sum('Sales_Amount'[Sales_Amount]) 

#2.How can you use the dax average sales per day for a given period?
Average_sales_perday_1 = AVERAGEX(VALUES(Sales_Amount[Date].[Day]), CALCULATE(SUM(Sales_Amount[Sales_Amount])))

#3. How can you create dax column that assigns the a status of 'High' to products 
#with sales amount greater than 1000 and 'Low' for others 

Status = IF('Product'[Sales_amount]>1000,"High sales","Low Sales")

Link: of DAX Power bI:  https://learn.microsoft.com/en-us/dax/dax-function-reference

Link of Power BI Service_ Real time: https://learn.microsoft.com/en-us/power-bi/connect-data/service-real-time-streaming
###################################
'''12-02-2024 worked on power BI DAX'''
##################################

#1.SWITCH function suppose you have a table named "Sales " with Amount Column Using SWITCH function  create a
# new calculated column that categorizes products as "High" , "Medium","Low" based on following criteria :
# if amount is greater than 1000, categorizes as "HIgh" , if amount is between 500 and 1000 then it is "Medium"
# if amount is less than 500 then itis "Low"

switch_status = SWITCH(TRUE(),'Product'[Sales_amount]>1000,"High",('Product'[Sales_amount]>500 && 'Product'[Sales_amount]<1000),"Medium","Low")

#2.IF function you have a table named "Employee" with columns "Age" and "Tenure" Using IF condition 
#that categorizes employees as "Junior","Intermediate","Senior" based on the following criteria:
    Category = IF(Employee[Age]<=18,"Junior",IF(Employee[Age]>18 && Employee[Age]>30,"Intermediate","Senior")) 

###################################
'''13-02-2024 worked on power BI Visulization'''
##################################

#1. In the Customers table create a new calculated column named 'FullName' that concatentates the 'Firstname'
# and 'Lastname' Columns with a space in between Basic Aggregation?

Details_ID = Customers[Customer Name] & " :" & Customers[Customer ID]

#2. Develop aDAX measure named "Total Sales" that calculates sum of sales amount column from Orders table

Total_Sales = sum(Orders[Sales])

#3.create a new column in the products table called "Profitable products" which should be boolean indicating 
# whether the profit column is greater than zero for each product percentage of total

Profitable products = IF(Products[Profit] > 0, TRUE, FALSE)

#4. create a DAX measure named Sales Measure that calculates the percentage of total sales each each product 
# category that contribute to overall sales ,filter with CALCULATE

Sales Measure = 
VAR TotalSales = CALCULATE(SUM(main_table[Sales]))
RETURN
DIVIDE(SUM(main_table[Sales]), TotalSales)

#5. Using the CALCULATE function,create a measure named Total Sales in West region regardless of other 
# any other applied filters using the table sample superstore.

Total Sales in West region = 
CALCULATE(
    SUM(main_table[Sales]),
   main_table[Region] = "Western Africa"
)


####################
'''15-02-2023 Power Bi Connectivity on Python'''
####################

#1.How can python can integerated into power BI for data connectivity?

we can use python source for get data place code make sure anaconda3 is exists in C:/Users/HARSHA path.

#2. What are the advantages does using python scripts in power BI for data connectivity?
we can use the dataframes which we assign in the python in power BI we can use as tables  by using this data 
connectivity.

#3.How can external data sources can accessed and imported into power BI using Python ?
by using Get Data feature in view tab.

###################
'''16-02-2023 Power BI '''
###################
#1. How do you create a new dashboard in power bi ?
In power BI when we logging with our corresponding mail id in power BI website after publish our reports from our 
power bi , under dashboards we can create a new dashboard and pin our reports to respective dash board which we created.

#2. What are the key principles for effctive data visulaizations in power BI dashboards?
 Here are some key principles:
a) Know Your Audience:
    Understand who will be using the dashboard and their level of expertise with data analysis.

b) Keep it Simple:
    Avoid clutter and unnecessary complexity. Use simple, easy-to-understand visualizations that convey the intended
message clearly.    
c) Use Appropriate Visualizations:
    Choose the right type of visualization for the data and the insights you want to convey. 
Common types include bar charts, line charts, pie charts, scatter plots, and maps. 
Use different visualization types for different types of data and comparisons.
    
d) Provide Context: 
    Add context to your visualizations by including titles, axis labels, legends, and annotations. 
This helps users understand what they re looking at and the significance of the data.

e) Highlight Key Insights:
    Use color, size, and emphasis to highlight important data points or trends. 
 This helps draw attention to the most critical insights and makes them stand out from the rest of the data.

f) Ensure Consistency:
    Maintain consistency in design elements such as colors, fonts, and styles across all 
visualizations in the dashboard. Consistency helps create a cohesive and professional look and makes it
easier for users to navigate and understand the dashboard.

g) Interactivity:

    Enable interactive features such as drill-downs, filters, and tooltips to allow users to explore 
the data in more detail and uncover insights relevant to their specific interests or questions.

h) Performance Optimization:
        Optimize the performance of your dashboard by minimizing data refresh times, 
reducing the number of visualizations on a single page, and using appropriate data aggregation techniques.

i)Accessibility:
    Ensure that your visualizations are accessible to all users, including those with disabilities. 

j) Iterate and Improve:

    Continuously gather feedback from users and stakeholders, and use it to iterate and
improve your dashboard over time

#3. How can users enable drill down functionality in a power BI dashboard?
Create a Hierarchical Data Model: 
    Ensure that your data model includes hierarchical relationships between different levels of data.
For example, you might have a hierarchy like Year > Quarter > Month or Category > Subcategory > Product.

#4. what is the purpose of PowerBI Tiles ,and how do they contribute to dashboard design?
Power BI Tiles is  helpful to share reports which we created in dashboards.

Report>Dashbooard>Tiles

#5. How can you share and collabarate on power BI dashboards with team members?
We can share through the share option with team members.


###################
'''19-02-2023 Power BI Report server and Row Level security '''
###################

#1. what is the purpose of power BI Report server how does it categorises to onpremesis reporting needs?

Power BI Report Server is an on-premises report server that is part of the Microsoft Power BI suite. Its purpose is to allow organizations to host and manage their Power BI reports, as well as traditional paginated reports, on their own infrastructure rather than in the cloud. Here's how it categorizes into on-premises reporting needs:

1. **On-Premises Hosting**: Power BI Report Server enables organizations to host their reports, dashboards, and other BI content on their own servers, providing greater control over data governance, security, and compliance. This is particularly important for organizations with strict regulatory requirements or concerns about data privacy.

2. **Integration with Existing Infrastructure**: For organizations that already have an on-premises infrastructure in place, Power BI Report Server seamlessly integrates with their existing systems and tools. It can be installed on Windows Server and integrated with SQL Server Reporting Services (SSRS), allowing organizations to leverage their investments in Microsoft technologies.

3. **Support for Paginated Reports**: In addition to Power BI reports and dashboards, Power BI Report Server supports traditional paginated reports, which are highly formatted, pixel-perfect reports commonly used for operational and business-critical reporting needs. This ensures that organizations can address a wide range of reporting requirements using a single platform.

4. **Offline Access**: Power BI Report Server allows users to access and interact with reports even when they are disconnected from the internet or the organization's network. This is especially useful for scenarios where users need to access reports while traveling or in remote locations with limited connectivity.

5. **Customization and Extensibility**: Power BI Report Server offers customization and extensibility options, allowing organizations to tailor the platform to their specific needs and requirements. This includes the ability to create custom visuals, integrate with other applications and services, and extend the platform's functionality through APIs and SDKs.

Overall, Power BI Report Server provides organizations with a flexible and scalable solution for hosting and managing their on-premises reporting needs, while also offering integration with cloud-based Power BI services for hybrid deployment scenarios.

#2.Explain the process of deploying a powerbi report to power BI Report server. Highlight
# any key considerations during deployment?


Deploying a Power BI report to Power BI Report Server involves several steps. Here's an overview of the process:

1. **Prepare the Report**: Ensure that the Power BI report is designed and developed according to your requirements. This includes connecting to the appropriate data sources, creating visualizations, applying filters, and optimizing the report layout for viewing on Power BI Report Server.

2. **Save the Report**: Save the Power BI report file (.pbix) locally on your computer or network drive.

3. **Access Power BI Report Server**: Open a web browser and navigate to the Power BI Report Server portal. Log in with appropriate credentials and navigate to the folder where you want to deploy the report.

4. **Upload the Report**: Click on the "Upload" button or drag-and-drop the .pbix file into the desired folder within the Power BI Report Server portal. The report file will be uploaded to the server.

5. **Configure Data Sources**: If the report connects to data sources that are not embedded within the report file, you may need to configure data source connections on the Power BI Report Server. This ensures that the report can retrieve data when viewed or refreshed on the server.

6. **Set Permissions**: Define permissions for the report to control who can view, edit, or manage it. You can set permissions at the folder level or for individual reports. Ensure that appropriate users or groups have the necessary permissions to access the report.

7. **Test the Report**: After deploying the report, it's essential to test it to ensure that it renders correctly and displays the expected data. Verify that interactive features such as filtering, drill-down, and tooltips function as intended.

8. **Schedule Refresh**: If the report includes data that needs to be regularly updated, configure a refresh schedule for the dataset within Power BI Report Server. This ensures that the data is kept up-to-date for users accessing the report.

Key Considerations During Deployment:

- **Data Source Connectivity**: Ensure that the data sources used in the report are accessible from the Power BI Report Server environment. If the data sources are located on-premises or in the cloud, verify that network connectivity and authentication methods are properly configured.

- **Version Compatibility**: Check the compatibility between the Power BI Desktop version used to create the report and the version of Power BI Report Server installed in your environment. Ensure that the report is saved in a compatible format for deployment.

- **Security and Permissions**: Pay close attention to security settings and permissions when deploying the report. Limit access to sensitive data and restrict editing privileges to authorized users.

- **Performance Optimization**: Optimize the report design and data retrieval queries for efficient performance on the Power BI Report Server. Consider factors such as data volume, complexity of visualizations, and hardware resources available on the server.

- **Documentation and Training**: Provide documentation and training for users who will access the deployed report. Ensure that they understand how to navigate the report, interact with visuals, and interpret the data presented.

By following these steps and considering key factors during deployment, you can successfully deploy Power BI reports to Power BI Report Server and make them available for consumption by users within your organization.

#3.What Security measures are available in power BI Report Server to control access to reports and ensure data protection?
Power BI Report Server offers several security measures to control access to reports and ensure data protection. 
Some key security features include:
1.Role-Based Security
2.Authentication
3.Row-Level Security (RLS)
4.Encryption
5.Auditing and Logging
6.Integration with Azure Security Features
7.Content Management Policies
8.Secure Embedded Analytics
#4.Diffrentiate between power BI Report Server and the power BI service focusing on deployment models,accessbility,and key feature 
# variation?

Power BI Report Server and the Power BI service are both offerings from Microsoft aimed at enabling organizations to create, 
publish, and share reports and dashboards. However, they differ in deployment models, accessibility, and key feature variations:

1.Deployment Models:
a)Power BI Report Server:
    Power BI Report Server is an on-premises solution that allows organizations to host and manage their reporting infrastructure 
    within their own data centers or cloud environments. It provides a self-managed environment where organizations have full control 
    over the hardware, software, and security configurations.

b)Power BI Service:    
    The Power BI service is a cloud-based platform that is hosted and managed by Microsoft. Users access the Power BI service 
    through a web browser or mobile app, and Microsoft is responsible for maintaining the underlying infrastructure, including 
    hardware, software updates, and security patches.

2.Accessibility:    
a)Power BI Report Server: 
    Access to reports and dashboards hosted on Power BI Report Server is typically limited to users within
    the organization's network or VPN. Users may need to be connected to the corporate network or authenticate using their 
    organizational credentials to access the reports.
b)Power BI Service: 
    The Power BI service is accessible from anywhere with an internet connection, allowing users to access reports and 
    dashboards from desktops, laptops, tablets, or mobile devices. Users can securely access the Power BI service from any 
    location using a web browser or the Power BI mobile app.
    
3.Key Feature Variation:
a)On-premises hosting: Organizations can host reports, dashboards, and datasets on their own infrastructure.
Customization and control: Organizations have full control over the configuration, security, and customization of the reporting environment.
Support for paginated reports: Power BI Report Server supports paginated reports (RDL) in addition to interactive Power BI reports.

b)Power BI Service:  
    Cloud-based deployment: Reports and dashboards are hosted in the Microsoft Azure cloud, providing scalability, reliability, and 
    global availability.
    Collaboration and sharing: The Power BI service enables seamless collaboration and sharing of reports within teams or across the 
    organization. Users can share reports with colleagues, publish to web, or embed in custom applications.
    Advanced analytics and AI: The Power BI service offers advanced analytics capabilities, including AI-powered insights, predictive 
    analytics, natural language queries, and integration with Azure Machine Learning.
    
#5.How can one schedule and manage report server subscriptions in power BI Report Server and what are the benifits does this feature 
# offer?

Overall, the subscription feature in Power BI Report Server enhances the accessibility and usability of reports by enabling 
automated delivery to stakeholders, thereby improving decision-making processes and organizational efficiency.












