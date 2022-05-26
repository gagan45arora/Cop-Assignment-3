import numpy as np
import matplotlib.pyplot as plt 

def box_muller(N):
    z1 = np.random.rand(N)
    z2 = np.random.rand(N)
    w1 = np.sqrt(-2*np.log(z1))*np.cos(2*np.pi*z2)
    w2 = np.sqrt(-2*np.log(z1))*np.sin(2*np.pi*z2)
    plt.hist(w1)
    plt.show()
    
    #Below is the comparision with normally distibuted random numbers
    
    a2 = np.random.normal(0,1,N)
    plt.hist(a2)
    plt.show()

box_muller(10000)