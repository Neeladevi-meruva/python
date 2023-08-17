1)zeros()
import numpy as p
a=p.zeros([3,2])
print(a)
#output [[0. 0.]
 [0. 0.]
 [0. 0.]]


2)ones()
import numpy as p
a=p.ones([3,2])
print(a)
#output [[1. 1.]
 [1. 1.]
 [1. 1.]]


3)ones_like()
import numpy as p
a=p.ones_like([2,3])
print(a)
#output[1,1]


4)zeros_like()
import numpy as p
a=p.zeros_like([1,2,4,5,89],dtype=float)
print(a)
#output [0.,0.,0.,0.,0.]


5)reshape()
import numpy as p
a=p.array([1,2,3,4,5,6])
b=a.reshape(2,3)
print(b)
#output [[1 2 3]
 [4 5 6]]


6).arange()
import numpy as p
a=p.arange(2,8)
print(a)
#output [2 3 4 5 6 7]


7)linspace()
import numpy as p
a=p.linsapce(1,2,10)
print(a)
#output [1.         1.11111111 1.22222222 1.33333333 1.44444444 1.55555556
 1.66666667 1.77777778 1.88888889 2.        ]


8)eye()
import numpy as p
a=p.eye(3)
print(a)
#output [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]


9)empty()
import numpy as p
a=p.empyty([2,2])
print(a)
#output [[6.71685658e-312 6.71699899e-312]
 [6.95276983e-310 6.71685658e-312]]


10)empty_like()
a=p.emptylike([2,2,4,5,6,7],dtype=int)
print(a)
#output 0 1 0 2345 0 78653


11)full_like()
import numpy as p
a=p.full_like([2,4,5,6,78,89],3)
print(a)
#output [3 3 3 3 3 3]


12) identity()
import numpy as p
a=p.identity(3)
print(a)
#output [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
