Data cleaning :A data cleaning is the process of remove or replace the nan(not a null) values
Types of data cleaning:
1.empty cells
2.wrong format
3.wrong data
4.remove duplicates

1.Empty celLS
when a cell contains the NAN values 
".isnull()"
".notnull()"
these are the methods used for the finding the null values
import pandas as pd
import numpy as np
ds={'id':pd.Series([1,2,3,4,5]),
    'name':pd.Series(['gowri',np.nan,'gopi','sai venkat','neela devi']),
    'age':pd.Series([23,27,30,np.nan,50]),
    'branch':pd.Series([np.nan,'it','eee','ece','civil'])}
df=pd.DataFrame(ds)
print("**********************isnull()**********************************")
print(df.isnull())
print("***********************notnull()*********************************")
print(df.notnull())
******************************OUTPUT**********************************
**********************isnull()**********************************
      id   name    age  branch
0  False  False  False    True
1  False   True  False   False
2  False  False  False   False
3  False  False   True   False
4  False  False  False   False
***********************notnull()*********************************
     id   name    age  branch
0  True   True   True   False
1  True  False   True    True
2  True   True   True    True
3  True   True  False    True
4  True   True   True    True

2.Wrong Format
The data in the column is belongs to same data type . If not we treat as a wrong Format

import pandas as pd
import numpy as np
ds={'id':pd.Series([1,2,3,4,5]),
    'name':pd.Series(['gowri',np.nan,'gopi','sai venkat','neela devi']),
    'age':pd.Series([23,'cs',30,np.nan,50]),
    'branch':pd.Series([np.nan,'it','eee','ece','civil'])}
df=pd.DataFrame(ds)
print(df)
print(df['age'].sum())
*******************OUTPUT**************************
   id        name  age branch
0   1       gowri   23    NaN
1   2         NaN   cs     it
2   3        gopi   30    eee
3   4  sai venkat  NaN    ece
4   5  neela devi   50  civil

st-packages/numpy/core/_methods.py in _sum(a, axis, dtype, out, keepdims, initial, where)
     46 def _sum(a, axis=None, dtype=None, out=None, keepdims=False,
     47          initial=_NoValue, where=True):
---> 48     return umr_sum(a, axis, dtype, out, keepdims, initial, where)
     49 
     50 def _prod(a, axis=None, dtype=None, out=None, keepdims=False,

TypeError: unsupported operand type(s) for +: 'int' and 'str'
#Wrong Data
we can treat it as mismatch
WE USE TWO METHODS 
i).fillna()
fillna(method="pad")
fillna(method="bfill")
ii).dropna()
import pandas as pd
import numpy as np
ds={'id':pd.Series([1,2,3,4,5]),
    'name':pd.Series(['gowri',np.nan,'gopi','sai venkat','neela devi']),
    'age':pd.Series([23,'cs',30,np.nan,50]),
    'branch':pd.Series([np.nan,'it','eee','ece','civil'])}
df=pd.DataFrame(ds)
print(df.dropna())
print(df.fillna(10)
print(df.fillna(method="pad"))
print(df.fillna(method="bfill"))
******************************output********************************
 id        name age branch
2   3        gopi  30    eee
4   5  neela devi  50  civil

0   1       gowri  23     10
1   2          10  cs     it
2   3        gopi  30    eee
3   4  sai venkat  10    ece
4   5  neela devi  50  civil

 id        name age branch
0   1       gowri  23    NaN
1   2       gowri  cs     it
2   3        gopi  30    eee
3   4  sai venkat  30    ece
4   5  neela devi  50  civil
   id        name age branch
0   1       gowri  23     it
1   2        gopi  cs     it
2   3        gopi  30    eee
3   4  sai venkat  50    ece
4   5  neela devi  50  civil
Rempove Duplicates
It is the process oof removing the duplicates values from DataSets
duplicated()
drop_duplicates()
import pandas as pd
import numpy as np
ds={'id':pd.Series([1,1,3,4,5]),
    'name':pd.Series(['gopi','gopi','gopi','sai venkat','neela devi']),
    'age':pd.Series([23,23,23,np.nan,50]),
    'branch':pd.Series([np.nan,np.nan,'eee','ece','civil'])}
df=pd.DataFrame(ds)
print(df.duplicated())
print(drop_duplicaes())
0    False
1     True
2    False
3    False
4    False
dtype: bool

   id        name   age branch
0   1        gopi  23.0    NaN
2   3       gowri  23.0    eee
3   4  sai venkat   NaN    ece
4   5  neela devi  50.0  civil



