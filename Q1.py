import numpy as np
import matplotlib.pyplot as plt

theta=np.arange(-10,10,0.1)
y=np.square(theta)
plt.plot(theta,y)
plt.xlabel(r'$\theta$')
plt.ylabel(r'L($\theta$)')
