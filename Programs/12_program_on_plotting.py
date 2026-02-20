"""
Plotting graphs using seaborn and matplotlib
Seaborn: https://pypi.org/project/seaborn/
matplotlib: https://pypi.org/project/matplotlib/
"""
print("Get my_expenses.xlsx")
print("-"*20)
# ---------------

import pandas as pd
my_expenses_df = pd.read_excel("my_expenses.xlsx")
print(my_expenses_df)

print("#"*40, end="\n\n")
############################

print("Seaborn Graph-1")
print("-"*20)
# ---------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.lineplot(x="Month", y="Amount Spent", data=my_expenses_df)

plt.show()

print("#"*40, end="\n\n")
############################

print("Seaborn Graph-2")
print("-"*20)
# ---------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.barplot(x="Month", y="Amount Spent", data=my_expenses_df)

plt.show()

print("#"*40, end="\n\n")
############################

print("matplotlib Graph-1")
print("-"*20)
# ---------------

import matplotlib.pyplot as plt

plt.bar(my_expenses_df["Month"], my_expenses_df["Amount Spent"])
plt.show()

print("#"*40, end="\n\n")
############################