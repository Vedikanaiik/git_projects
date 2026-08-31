# Name: Vedika Pradeep Naik, prn: 26070122230, CSE C-3
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv('student data.csv')

plt.hist(data['Maths'], bins=5, color='green', alpha=0.7)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Maths Marks")
plt.show()
