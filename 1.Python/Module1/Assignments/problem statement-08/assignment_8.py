
# 1)Connect MySQL using Python, push "Data.csv" into the database.
from sqlalchemy import create_engine,text
import pandas as pd
from urllib.parse import quote

user= 'root'
pw = 'root'
db= 'harsha'

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user = "root",# user
                               pw = 'root', # passwrd
                               db = "harsha")) #database

data =pd.read_csv('C:/Users/HARSHA/Downloads/Data Sets/datasets/Copy of Data.csv')

data.to_sql('data', con = engine, if_exists = 'replace', chunksize = None, index= False)


sql = "SELECT * FROM data;" # wright query of sql and save into variable
assig = pd.read_sql_query(sql, engine)

# 2)Connect MySQL using Python, push "Indian Cities.csv" into the database, and then use Python to load the data from MySQL.

from sqlalchemy import create_engine,text
import pandas as pd
from urllib.parse import quote

user= 'root'
pw = 'root'
db= 'harsha'

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user = "root",# user
                               pw = 'root', # passwrd
                               db = "harsha")) #database

Indian_city =pd.read_csv('C:/Users/HARSHA/Downloads/Data Sets/datasets/Copy of Indian_cities.csv')

data.to_sql('Indian_city', con = engine, if_exists = 'replace', chunksize = None, index= False)


sql = "SELECT * FROM data;" # wright query of sql and save into variable
ind_city = pd.read_sql_query(sql, engine)
