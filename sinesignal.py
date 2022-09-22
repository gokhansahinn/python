import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,6,100)
y=np.sin(x)
y1=np.cos(x)

plt.plot(x,5*y)
plt.plot(x,y1,'r')
plt.show()