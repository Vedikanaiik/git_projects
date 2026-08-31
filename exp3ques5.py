# Name: Vedika Pradeep Naik, prn: 26070122230, CSE C-3
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv('student data.csv')

plt.plot(data['Name'], data['Physics'], marker='o', label='Physics')
plt.plot(data['Name'], data['Chemistry'], marker='o', label='Chemistry')
plt.plot(data['Name'], data['Maths'], marker='o', label='Maths')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Subject-wise Performance")
plt.legend()
plt.show()
