import matplotlib.pyplot as pt
import numpy as np
x = np.linspace(1,100 , 10)
y = x**2
y1 = x**2+1000
fig , axes = pt.subplots(4,2)
axes[0][0].plot(x , y , color="r" , marker="s" , label="y=X^2")
axes[1][1].plot(x , y1 , color="#40aa5b" , marker="s" , label="y=X^2+4")
axes[0][1].bar([1,5,7],[2,4,3] , [1,1,1])
axes[0][0].legend()
pt.xlabel("X")
fig.set_facecolor("pink")
pt.show()
