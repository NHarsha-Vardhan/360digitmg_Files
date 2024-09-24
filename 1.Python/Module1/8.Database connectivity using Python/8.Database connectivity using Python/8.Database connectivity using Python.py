# import libraries
import pandas as pd
# Import data (.csv file) using pandas. We are using mba data set
mba = pd.read_csv("education.csv")
 

# - SQLAlchemy is basically referred to as the toolkit of Python SQL that provides developers with the flexibility of using the SQL database. 
# - The benefit of using this particular library is to allow Python developers to work with the language's own objects, and not write separate SQL queries.

# pip install sqlalchemy
from sqlalchemy import create_engine,text

import pandas as pd
# **Engine Configuration**
# The Engine is the starting point for any SQLAlchemy application. 
# It’s “home base” for the actual database and its DBAPI, 
# delivered to the SQLAlchemy application through a connection pool and a Dialect, 
# which describes how to talk to a specific kind of database/DBAPI combination.
# sqlalchemy helps to connect mysql, postgresql, microsoftsql(mssql), etc;

from urllib.parse import quote
# Refer this url for brief Knowledge about "create_engine"
# https://docs.sqlalchemy.org/en/20/core/engines.html
user= 'root'
pw = 'root'
db= 'harsha'

## For mysql
#pip install pymysql
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user = "root",# user
                               pw = 'root', # passwrd
                               db = "harsha")) #database

mba = pd.read_csv(r"F:\Liser Time\360digitmg\1.Python\Module1\Assignments\problem statement-08\datasets\education.csv")
# To send data into DataBase
# DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)
# Go to this link for more details
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# Databases supported by SQLAlchemy are supported. Tables can be newly created, appended to, or overwritten.
mba.to_sql('mba', con = engine, if_exists = 'replace', chunksize = None, index= False) # sending data into database and connecting with Engine by using "DataFrame.to_sql()"

# To get the data From DataBase
sql = "SELECT * FROM mba;" # wright query of sql and save into variable
anime = pd.read_sql_query(sql, engine) # connecting query with Engine and reading the results by using "pd.read_sql_query"


# for sqlalchemy 1.4.x version (old version)
# df = pd.read_sql_query(engine, sql)

# for sqlalchmey 2.x version (new version)
df = pd.read_sql_query(text(sql), engine.connect())
##########################################################
#updated script for data base 

from sqlalchemy import create_engine, text
from urllib.parse import quote
user = 'root' # user name
pw = 'Shiv1998' # password
db = 'shiv' # database
# creating engine to connect database
engine = create_engine(f"mysql+pymysql://{user}:%s@localhost/{db}" %quote(f'{pw}'))

# to_sql() - function to push the dataframe onto a SQL table.
uni.to_sql('univ_tbl1', con = engine, if_exists = 'replace', chunksize = 1000, index = False)



###### To read the data from MySQL Database
sql = 'select * from univ_tbl1;'


# for sqlalchemy 1.4.x version (old version)
# df = pd.read_sql_query(engine, sql)

# for sqlalchmey 2.x version (new version)
df = pd.read_sql_query(text(sql), engine.connect())