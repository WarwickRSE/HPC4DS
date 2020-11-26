#This code generates an estimate for Pi by selecting two random numbers
#This version loads the pickle from 02_broken_writer.py but seeds the RNG
#with a different value. This means that it generates new random numbers
#having statistical power and produces a better estimate for pi. THE RESULT
#IS NOT THE SAME AS NOT HAVING RESTARTED BUT THE RESULT IS STATISTICALLY VALID
#You have to decide if this is acceptable to you.
import numpy as np
import pickle

np.random.seed(256)

ct, cti = pickle.load(open('data.pyc','rb'))

for i in range(50000):
  rnds = np.random.random(2001)
  ct += 1000
  cti += np.sum(np.sqrt(rnds[0:1000]**2+rnds[1001:2001]**2) < 1.0)

print(4.0*cti/ct)
