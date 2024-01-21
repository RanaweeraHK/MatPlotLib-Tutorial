import matplotlib.pyplot as plt
import numpy as np

#limits
plt.plot([1,2,3,4],[2,4,6,8])
#check the limits
left,right = plt.xlim()
bottom,top = plt.ylim()
print(left,right)
print(bottom,top)

#change the limits
left,right = plt.xlim(left=2,right=10)
bottom,top = plt.ylim(bottom=1,top=6)
print(left,right)
print(bottom,top)
plt.show()
