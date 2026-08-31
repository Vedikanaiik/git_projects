# Name: Vedika Pradeep Naik, prn: 26070122230, CSE C-3
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv('student data.csv')
plt.bar(data['Name'], data['Average'], color='skyblue')
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()
