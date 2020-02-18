import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

data=pd.read_excel('Problem1.xlsx')
#print(data.iloc[:,1])
x=np.array([data.iloc[:, 0]]).T
y=np.array([data.iloc[:,1]]).T
x=(x-np.mean(x))/np.std(x)
'''x=np.insert(x,0,1,axis=1)'''
theta1=np.arange(-30,30,0.1)
theta2=np.arange(-30,30,0.1)
z=np.zeros((len(theta1),len(theta1)))

ans=999999999999999999999999.9999
t1=0.0
t2=0.0
for i in range(len(theta1)):
    for j in range(len(theta2)):
        temp=0.0
        for k in range(x.shape[0]):
            temp+=(y[k,0]-theta1[i]-x[k,0]*theta2[j])**2
        z[i,j]=temp
        if temp<ans:
            ans=temp
            t1=theta1[i]
            t2=theta2[j]
print("minima at : ")            
print("theta1=%f"%t1) #23.800000000000765
print("theta2=%f"%t2) #-6.899999999999672
print("min=%f"%ans) #1571.58612144908
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta1,theta2,z)
ax.set_zlabel(r"$L(\theta)$", fontsize=17)
ax.set_xlabel(r"$\theta1$", fontsize=17)
ax.set_ylabel(r"$\theta2$", fontsize=17)

plt.show()



