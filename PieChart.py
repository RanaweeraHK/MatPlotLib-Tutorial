import matplotlib.pyplot as plt
#Pie chart
category =["Food","Transport","Sport","Health"]
amount = [980,450,1200,780]
plt.pie(amount,labels=category,radius=1.5, autopct="%0.1f%%" , explode=[0,0.2,0,0])
plt.show()
