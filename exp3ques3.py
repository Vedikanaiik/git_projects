# Name: Vedika Pradeep Naik, prn: 26070122230, CSE C-3
import pandas as pd

data = pd.read_csv("student data.csv")

data['Average'] = data[['Physics', 'Chemistry', 'Maths']].mean(axis=1)
print(data[['Name', 'Average']])
