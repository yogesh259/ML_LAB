import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

theta1=np.arange(-10,10,0.1)
theta2=np.arange(-10,10,0.1)
x,y=np.meshgrid(theta1,theta2,sparse=False,indexing='xy')

z=np.zeros((len(theta1),len(theta1)))

for i in range(len(theta1)):
    for j in range(len(theta2)):
        z[i,j]=theta1[i]**2+theta2[j]**2


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z)
ax.set_zlabel(r"$L(\theta)$", fontsize=17)
ax.set_xlabel(r"$\theta1$", fontsize=17)
ax.set_ylabel(r"$\theta2$", fontsize=17)

