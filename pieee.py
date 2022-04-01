import matplotlib.pyplot as plt
import pandas as pd

df =  pd.read_csv('stat.csv')
country_data = df["Heur"]
medal_data = df["Pourc"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0, 0, 0, 0, 0)  
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=140)
plt.title("statistiques")
plt.show()