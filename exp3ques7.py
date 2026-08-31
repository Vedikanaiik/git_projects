# Name: Vedika Pradeep Naik, prn: 26070122230, CSE C-3
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv('student data.csv')

plt.pie(data['Average'], labels=data['Name'], autopct='%1.1f%%', startangle=90)
plt.title("Share of Average Marks by Student")
plt.show()

