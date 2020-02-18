import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy.linalg as nl
data=pd.read_excel('Problem1.xlsx')
#print(data.iloc[:,1])
x=np.array([data.iloc[:, 0]]).T
y=np.array([data.iloc[:,1]]).T
x=(x-np.mean(x))/np.std(x)
ones = np.ones(x.shape)
x=np.c_[ones,x]
#x=np.insert(x,0,1,axis=1)

theta=(nl.pinv(x.T @ x)@(x.T@y))
print(theta)