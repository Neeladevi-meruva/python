ATTRIBUTES OF DATA IN DATAFRAMES
1.size
2.shape
3.info
4.index
5.memory_usage
6.ndim
import pandas as p
ds={'sno':p.Series([1,2,3,4,5,6,7]),
    'name':p.Series(['neela','nani','subbu','sasi','swapna','santhos','suma']),
    'age':p.Series([12,23,45,67,22,11,45])}
df=p.DataFrame(ds)
print(df)
print(df.size)
print(df.shape)
print(df.index)
print(df.memory_usage())
print(df.info())
print(df.ndim)
******************************************************************************************
output:-
   sno     name  age
0    1    neela   12
1    2     nani   23
2    3    subbu   45
3    4     sasi   67
4    5   swapna   22
5    6  santhos   11
6    7     suma   45
21
(7, 3)
RangeIndex(start=0, stop=7, step=1)
Index    132
sno       56
name      56
age       56
dtype: int64
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   sno     7 non-null      int64 
 1   name    7 non-null      object
 2   age     7 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 300.0+ bytes
None
2
