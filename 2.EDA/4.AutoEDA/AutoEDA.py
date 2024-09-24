# Load the Data
import pandas as pd

df = pd.read_csv(r"F:\Liser Time\360digitmg\2.EDA\Data Sets\education.csv")

# Auto EDA
# ---------
# Sweetviz
# Autoviz
# Dtale
# Pandas Profiling
# Dataprep

#import jinja2
# Sweetviz
###########
#pip install sweetviz
import sweetviz as sv

s = sv.analyze(df)
s.show_html()

################
#import matplotlib.pyplot as plt

# Temporarily set the Matplotlib style to another valid style
#plt.style.use('ggplot')  # You can choose any valid style from plt.style.available

# Now import AutoViz_Class
#from autoviz.AutoViz_Class import AutoViz_Class
#matplotlib.style.use('seaborn')
#print(matplotlib.__version__)
###############

# Autoviz
###########
# Once try in jyputer 
#!pip install autoviz
from autoviz.AutoViz_Class import AutoViz_Class

av = AutoViz_Class()
a = av.AutoViz(r"F:\Liser Time\360digitmg\2.EDA\Data Sets\education.csv", chart_format = 'html')

import os
os.getcwd()

# If the dependent variable is known:


    
a = av.AutoViz(r"F:\Liser Time\360digitmg\2.EDA\Data Sets\education.csv", depVar = 'gmat') # depVar - target variable in your dataset



# D-Tale
########

#!pip install dtale  
 # In case of any error then please install werkzeug appropriate version (pip install werkzeug==2.0.3)
import dtale
import pandas as pd

df = pd.read_csv(r"F:\Liser Time\360digitmg\2.EDA\Data Sets\education.csv")

d = dtale.show(df)
d.open_browser()


# Pandas Profiling
###################
import sys
print(sys.executable)
#############
#!pip list
#!pip install pandas_profiling


#from pandas_profiling import ProfileReport 
# Do pip install -U pydantic: if we are getting # ModuleNotFoundError: No module named 'pydantic.v1'
from ydata_profiling import ProfileReport

p = ProfileReport(df)
ProfileReport(df)
p.to_file("output.html")


import os
os.getcwd()

# Dataprep
##########

#!pip install dataprep
#from markupsafe import Markup
#from markupsafe import escape as markupsafe_escape
#from jinja2.utils import escape as jinja_escape
#escaped_text = Markup('<script>alert("Hello!");</script>')
#import warnings
#warnings.filterwarnings("ignore", category=FutureWarning)
from dataprep.eda import create_report
#from dataprep.eda import create_report
report = create_report(df, title = 'My Report')

report.show_browser()


