from sympy import *
import sympy.plotting as pt
init_printing()
x = Symbol("x")
y = Symbol("y")
z = Symbol("z")

f = x**2+4*x+3

print(f)
pprint(f)
f2 = x*2/(x+y)+x/y
pt.plot(1/x)
pprint(f2)

f = (x-y)*(x+y)
pprint(f.expand())
f2 = (2*x+y)/(x+y)
pprint(f2.apart(x))


f = x**2+1
lim = Limit(f,x,0)
pprint(lim)
pprint(lim.doit())

drv = Derivative(f , x, x)
pprint(drv)
pprint(drv.doit())

interal = Integral(f , (x , -oo, oo))
pprint(interal)
pprint(interal.doit())

sum = Sum(f , (x , 0,10))
pprint(sum)
pprint(sum.doit())

product = Product(f , (x , 0,10))
pprint(product)
pprint(product.doit())

