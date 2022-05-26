import numpy as np
import matplotlib.pyplot as plt 

N = 10000

ar0 = np.sqrt(2/np.pi)*np.random.rand(N)
arx = []

for i in range (0,N):
    arx.append((np.random.rand()-0.5)*10)  # generates a random number between -5 and 5

ar2 = []
x = np.linspace(0,1,N)

for i in range (0,N):
    if(np.sqrt(2/np.pi)*np.exp(-(arx[i]**2)/2)-ar0[i]>0): #Condition that point falls below the desired plot
        ar2.append(arx[i])

plt.hist(ar2)
plt.show()