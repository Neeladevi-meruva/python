"""Analyzing data
1.viewing data
2.info about data
3.data mungning
4.data filtering
5.data merging
6.data reshaping
7.data aggregation
8.data grouping
"""
#1.viewing data
import pandas as pd
ds={'id':pd.Series([1,2,3,4,5]),
    'name':pd.Series(['gowri','swetha','gopi','sai venkat','neela devi']),
    'age':pd.Series([23,27,30,48,50]),
    'branch':pd.Series(['cse','it','eee','ece','civil'])}
df=pd.DataFrame(ds)
print(df)
print("-------------------------viewing of data----------------------------------")
x=df.describe()
print(x)
y=df.head(3)
print(y)
z=df.tail(2)
print(z)
print("----------------------------info of data------------------------------------")
#info of data
df.info()
print(df)
print("-----------------------------data filtering---------------------------------")
#data filtering 
a=df['age']
print(a)
print("-----------------------------data merging------------------------------------")
#data merging
import pandas as pd
ds={'id':pd.Series([1,2,3,4,5]),
    'name':pd.Series(['gowri','swetha','gopi','sai venkat','neela devi']),
    'age':pd.Series([23,27,30,48,50]),
    'branch':pd.Series(['cse','it','eee','ece','civil'])}
df=pd.DataFrame(ds)
print(df)
import pandas as pd
stu={'id':pd.Series([1,2,3,4,5]),
     'sname':pd.Series(['rani','latha','ramya','bhavani','anji']),
     'age':pd.Series([24,35,46,26,34]),
     'study':pd.Series(['btech','bcom','mba','mca','msc'])
     }
df2=pd.DataFrame(stu)
print(df2)
print(pd.merge(df,df2,on='id'))
print("----------------------data aggregation-------------------------------------")
print(pd.concat([df,df2]))
print("----------------------data grouping--------------------------------------------")
print(df.groupby(['age']))
print(df)




