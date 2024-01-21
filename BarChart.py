import matplotlib.pyplot as plt
import numpy as np

#bar chart
x = ["Maths","Physics","Chemistry"]
y = [50,90,60]
plt.bar(x,y,width =0.7)
plt.show()

plt.barh(x,y ) #Horizontal barchart
plt.show()
