import numpy as np
import matplotlib.pyplot as plt
import time

N=10000
arr = []
ar1 = []
x = np.zeros(N)
a = 26801522
c = 152783930
m = 250678291
ini = 1256822
arr.append(ini)
ar1.append(ini/(m-1))

start_time = time.time()

for i in range (1,N):
    x[i] = i
    ty = ((arr[i-1]*a+c)%m)
    ar1.append(ty/(m-1)) 
    arr.append(ty)

print("Congruential random number generator took %s seconds " % (time.time() - start_time),"to genrate %s random numbers" %N)

plt.hist(ar1)
plt.show()

start_time_2 = time.time()

ar1 = np.random.rand(N)

print("The inbuilt numpy random number generator took %s seconds " % (time.time() - start_time_2)," to generate %s random numbers" %N)

plt.hist(ar1)
plt.show()