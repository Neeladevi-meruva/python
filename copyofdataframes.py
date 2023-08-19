import pandas as p
ds={'sno':p.Series([1,2,3,4,5,6,7]),
    'name':p.Series(['neela','nani','subbu','sasi','swapna','santhos','suma']),
    'age':p.Series([12,23,45,67,22,11,45])}
df=p.DataFrame(ds)
print(df)
ds=df.copy(deep=False)
print(ds)
ds=df.copy(deep=True)
print(ds)
output:
0    1    neela   12
1    2     nani   23
2    3    subbu   45
3    4     sasi   67
4    5   swapna   22
5    6  santhos   11
6    7     suma   45
   sno     name  age
0    1    neela   12
1    2     nani   23
2    3    subbu   45
3    4     sasi   67
4    5   swapna   22
5    6  santhos   11
6    7     suma   45
