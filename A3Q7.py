from scipy import stats
from scipy import random
import numpy as np
import matplotlib.pyplot as plt 

N = 144
# scipy.stats.chi2.cdf(18.7625,10.00)
x = np.random.randint(1,7,size=N)+np.random.randint(1,7,size=N) 
p = [1/36,1/18,1/12,1/9,1/6,7/36,1/6,5/36,1/9,1/12,1/18,1/36]

l=0

v, n = np.unique(x,return_counts=True)
# sum =0

for i in range (0,11):
    l+=((n[i]-N*p[i])**2)/(N*p[i])
print(l)
test = stats.chi2.cdf(l,10.0)
print(test)
if ((test<=1 and test>=0.99) or (test>=0 and test<0.01)):
    print("Not sufficiently random")
elif (test<=0.05 or test>=0.95):
    print("Suspect") #whne the imposter is sus-amogus
elif(test<=0.1 or test>=0.9):
    print("almost suspect") #sus-amogus season-2 
elif(test>0.1 and test<0.9):
    print("Sufficiently random") 
else:
    print("Error")
