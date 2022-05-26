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
if ((test<=1 and test>=0.95) or (test>0 and test<0.05)):
    print("Not sufficiently random")
elif (test<=0.4 and test>=0.6):
    print("Sufficiently random")
elif((test>0.05 and test<0.4) or (test>0.6 and test<0.95)):
    print("almost suspect") #whne the imposter is sus-amogus
elif((test>0.05 and test<0.4) or (test>0.6 and test<0.95)):
    print("almost suspect") #sus-amogus season-2
else:
    print("Error")