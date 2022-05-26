import numpy as np
import matplotlib.pyplot as plt 

N = 100000
ar0 = []
arx = []

def func(ar):
    ret=0
    for i in range (len(ar)):
        ret += ar[i]**2
    return ret

dim=10   # This value can be changed to get volumes of different n-spheres

ay = np.zeros((N,dim))
for i in range (0,N):
    for j in range (0,dim):
        ay[i][j] = (np.random.rand()-0.5)*2

ct=0
for i in range (0,N):
    if(func(ay[i])<1):
        ct+=1

print("The volume of",dim," dimensional unit-sphere is ",2**(dim)*ct/N,"(units)^",dim )

#Below code can be uncommented to show a nice plot of volume of unit sphere as a function of number of dimensions
# It will take some time (approx. 30 seconds)


# area = []
# for k in range (2,15):
#     ay = np.zeros((N,k))
#     for i in range (0,N):
#         for j in range (0,k):
#             ay[i][j] = (np.random.rand()-0.5)*2

#     ct=0
#     for i in range (0,N):
#         if(func(ay[i])<1):
#             ct+=1
#     area.append(2**(k)*ct/N)
# x = np.linspace(2,15,13)
# plt.plot(x,area)
# plt.show()