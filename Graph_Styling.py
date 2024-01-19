import matplotlib.pyplot as plt
import numpy as np


x= [1,2,3,4,5,6]
plt.plot(x,np.power(x,2),"mo--",linewidth=2)
# plt.plot(x coordination, y coordiantion, "colour,marker,line style")

# 2 graphs in same figure
plt.plot(x,np.power(x,2),"mo--",x,np.power(x,3),"c*--")

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Graph")
plt.show()


