#This code generates an estimate for Pi by selecting two random numbers
#This version runs for half as many iterations as the baseline version
#and then writes out the user defined state using Pickle
import numpy as np
import pickle

np.random.seed(128)

ct = 0
cti = 0

for i in range(50000):
  rnds = np.random.random(2001)
  ct += 1000
  cti += np.sum(np.sqrt(rnds[0:1000]**2+rnds[1001:2001]**2) < 1.0)

pickle.dump([ct,cti],open('data.pyc','wb'))
print(4.0*cti/ct)
