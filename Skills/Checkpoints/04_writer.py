#This code generates an estimate for Pi by selecting two random numbers
#This version runs to half the number of iterations as the baseline simulation
#and outputs intermediate state using Pickle, but also outputs the state of the
#RNG when it pickles it
import numpy as np
import pickle

np.random.seed(128)

ct = 0
cti = 0

for i in range(50000):
  rnds = np.random.random(2001)
  ct += 1000
  cti += np.sum(np.sqrt(rnds[0:1000]**2+rnds[1001:2001]**2) < 1.0)

pickle.dump([ct,cti,np.random.get_state()],open('data.pyc','wb'))
print(4.0*cti/ct)
