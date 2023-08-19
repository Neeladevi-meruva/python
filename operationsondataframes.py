DATAFRAMES OPERATIONS
1.selection
2.addition
3.deletion
import pandas as p
ds={'sno':p.Series([1,2,3,4,5,6,7]),
    'name':p.Series(['neela','nani','subbu','sasi','swapna','santhos','suma']),
    'age':p.Series([12,23,45,67,22,11,45])}
df=p.DataFrame(ds)
print(df)
ds=df.copy(deep=True)
print(ds)
print(df['name'])#selection
****************output*****************
 sno     name  age
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
0      neela
1       nani
2      subbu
3       sasi
4     swapna
5    santhos
6       suma
Name: name, dtype: object
2)addition
df['bloodgroup']=p.Series(['A-','B+','A-','O-','AB+','O+','AB+'])
print(df)
************************output*********************
   sno     name  age bloodgroup
0    1    neela   12         A-
1    2     nani   23         B+
2    3    subbu   45         A-
3    4     sasi   67         O-
4    5   swapna   22        AB+
5    6  santhos   11         O+
6    7     suma   45        AB+
3)deletion
   a)using pop()
df.pop('age')
print(df)
 sno     name bloodgroup
0    1    neela         A-
1    2     nani         B+
2    3    subbu         A-
3    4     sasi         O-
4    5   swapna        AB+
5    6  santhos         O+
6    7     suma        AB+
by using del
del df['sno']
print(df)
      name bloodgroup
0    neela         A-
1     nani         B+
2    subbu         A-
3     sasi         O-
4   swapna        AB+
5  santhos         O+
6     suma        AB+
