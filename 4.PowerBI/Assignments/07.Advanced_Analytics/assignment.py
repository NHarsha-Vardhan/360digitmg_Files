import pandas as pd
import numpy as np
import seaborn as sns
from pmdarima.arima import auto_arima
data = pd.read_excel(r"F:\Liser Time\360digitmg\4.PowerBI\Power BI Data Sources\Sample - Superstore.xls")

sns.scatterplot(x='Sales', y='Profit', data=data)
plt.xlabel('Accept')
plt.ylabel('GradRate')
plt.title('Acceptance vs Gradrate scatter plot')
plt.grid()
plt.show()

# Perform ARIMA forecasting
model = auto_arima(data['Sales'], seasonal=False, trace=True)  # Adjust parameters as needed
forecast = model.predict(n_periods=10)  # Forecast the next 10 steps
