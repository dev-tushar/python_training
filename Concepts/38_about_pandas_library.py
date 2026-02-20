"""
About pandas library
- pandas library written for tabular data processing like xlsx, csv
- pandas library will be having many functions and many classes
    -- Few functions names are read_csv(), read_excel() etc
    -- Few class names are DataFrame, Series etc
- Main class inside pandas library is 'DataFrame' class

About 'DataFrame' class
- 'DataFrame' class is having methods related tabular data processing

Documentation: https://pypi.org/project/pandas/
"""

print("Inside pandas library")
print("-"*20)
# ---------------
import pandas as pd

print(dir(pd))

print("#"*40, end="\n\n")
############################

print("Inside DataFrame class")
print("-"*20)
# ---------------
import pandas as pd

print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-1")
print("Store Values")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([ [10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]])
print(my_df)

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-2")
print("Store Values and provide column and row names")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([ [10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]],
                     columns=["c1","c2","c3","c4", "c5"],
                     index=["r1", "r2", "r3"]
                     )
print(my_df)

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-3")
print("Trying sum() method on entire data")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([ [10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]])

print("Data:", my_df, sep="\n", end="\n\n")

print("Sum:", my_df.sum(), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-4")
print("Trying sum() method on entire data")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([ [10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]])

print("Data:", my_df, sep="\n", end="\n\n")

print("Sum:", my_df.sum().sum(), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-5")
print("One Cell:")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([
                        [10, 20, 30, 40, 50],
                       [60, 70, 80, 90, 100],
                       [110, 120, 130, 140, 150],
                       [160, 170, 180, 190, 200],
                        [220, 230, 240, 250, 260]
                       ])

print("Data:", my_df, sep="\n", end="\n\n")

# iloc[row_index, column_index]
print("One Cell:", my_df.iloc[1,1]) # 2nd row, 2nd column

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-6")
print("One Row:")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([
                        [10, 20, 30, 40, 50],
                       [60, 70, 80, 90, 100],
                       [110, 120, 130, 140, 150],
                       [160, 170, 180, 190, 200],
                        [220, 230, 240, 250, 260]
                       ])

print("Data:", my_df, sep="\n", end="\n\n")

# iloc[row_index, column_index]
print("One Row:", my_df.iloc[1], sep=" ", end="\n\n") # 2nd row

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-7")
print("One Column:")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([
                        [10, 20, 30, 40, 50],
                       [60, 70, 80, 90, 100],
                       [110, 120, 130, 140, 150],
                       [160, 170, 180, 190, 200],
                        [220, 230, 240, 250, 260]
                       ])

print("Data:", my_df, sep="\n", end="\n\n")

# iloc[row_index, column_index]
print("One Column:", my_df.iloc[: , 1], sep="\n", end="\n\n") # 2nd column

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-8")
print("Few Rows:")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([
                        [10, 20, 30, 40, 50],
                       [60, 70, 80, 90, 100],
                       [110, 120, 130, 140, 150],
                       [160, 170, 180, 190, 200],
                        [220, 230, 240, 250, 260]
                       ])

print("Data:", my_df, sep="\n", end="\n\n")

# iloc[row_index, column_index]
print("Few Rows:", my_df.iloc[1:3], sep="\n", end="\n\n") # 2nd and 3rd row (1st index included, last index excluded.
                                                          # So printing rows with index 1 and 2)

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-9")
print("Few Columns:")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([
                        [10, 20, 30, 40, 50],
                       [60, 70, 80, 90, 100],
                       [110, 120, 130, 140, 150],
                       [160, 170, 180, 190, 200],
                        [220, 230, 240, 250, 260]
                       ])

print("Data:", my_df, sep="\n", end="\n\n")

# iloc[row_index, column_index]
print("Few Columns:", my_df.iloc[: , 1:3], sep="\n", end="\n\n") # 2nd and 3rd column

print("#"*40, end="\n\n")
############################

print("DataFrame class Example-10")
print("Few rows and Few Columns:")
print("-"*20)
# ---------------
import pandas as pd

my_df = pd.DataFrame([
                        [10, 20, 30, 40, 50],
                       [60, 70, 80, 90, 100],
                       [110, 120, 130, 140, 150],
                       [160, 170, 180, 190, 200],
                        [220, 230, 240, 250, 260]
                       ])

print("Data:", my_df, sep="\n", end="\n\n")

# iloc[row_index, column_index]
print("Few Rows and Few Columns:", my_df.iloc[1:3 , 1:3], sep="\n", end="\n\n")
# 2nd and 3rd column
# and
# 2nd and 3rd row

print("#"*40, end="\n\n")
############################