import numpy as np
import numpy.linalg as l
a = np.random.random(8)
print(a)
print(type(a))
b = np.linspace(1,10,5)
print(b)
c = np.array([1,2,3,4,5,6,7,8,9])
c = c.reshape((3,3))
print(c)
print(c.size)
print(c.shape)
d = np.zeros((3,4))
x = np.eye(3,4 , k=2)
d = np.random.randint(1,100,1000)
d = d.reshape((50,20))
print(x)
print(d)
print(d[0][1])
print(d[0,1])
print(d[2:5:1,1:4:1])

a = np.array([4,2,3,6]).reshape((2,2))
b = np.array([10,12]).reshape((2,1))

print(l.solve(a,b))