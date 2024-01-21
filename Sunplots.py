import matplotlib.pyplot as plt
import numpy as np
#subplots = more than 1 graph represents in the same figure
import matplotlib.pyplot as plt
import numpy as np

x= np.arange(1,10,0.1)
y1 = x
y2 = np.sqrt(x)
y3 = np.power(x,2)
y4 = np.power(x,3)

plt.figure() #creating a figure object

#graph1
plt.subplot(2,2,1)
plt.plot(x,y1,'ro')
plt.title("$y=x$")

#graph2
plt.subplot(2,2,2)
plt.plot(x,y2,'bo')
plt.title("$y=/sqrt{x}")

#graph3
plt.subplot(2,2,3)
plt.plot(x,y3,'ko')
plt.title("$y=x^2$")

#graph4
plt.subplot(2,2,4)
plt.plot(x,y4,'co')
plt.title("$y=x^3$")

plt.show()
