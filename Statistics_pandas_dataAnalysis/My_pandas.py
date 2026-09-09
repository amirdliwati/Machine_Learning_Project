import pandas as pd

My_list1 = [100,120,140,150,180,210]

s = pd.Series(My_list1)
print(s.describe())

s.plot(kind='bar')

df = pd.DataFrame(My_list1 , columns=['my_numbers'])
df.to_excel('D:\Dropbox\Ph.D\AMIR Ph.D\Python\Projects\Test_project\Statistics_pandas_dataAnalysis\test.xlsx',sheet_name='Sheet1')