from scipy import random
import numpy as np
import matplotlib.pyplot as plt 

def shift_or_not(p):
    unif = random.uniform(0,1)
    if unif>=p:
        return False
    else:
        return True

def fug(x):
    if (x>=3 and x<=7):
        return 0.25
    else:
        return 0

def MCMC(hops):
    states = []
    burn_in = int(hops/6)
    aex = []
    current = random.uniform(0,10)
    for i in range(hops):
        states.append(current)
        aex.append(i)
        movement = random.uniform(0,10)

        curr_prob = fug(current)
        move_prob = fug(movement)
        if(curr_prob==0):
            acceptance = 1
        else:
            acceptance = min(move_prob/curr_prob,1)
        if shift_or_not(acceptance):
            current = movement
    plt.plot(aex[burn_in:],states[burn_in:])
    plt.show()
    return states[burn_in:]
    
dist = MCMC(10000)
plt.hist(dist,bins=20) 

plt.show()