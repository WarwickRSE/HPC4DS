from datetime import datetime
from numpy import random

# Get current microseconds (assuming system can do this)
dt = datetime.now()
seed = dt.microsecond

#Swap between these to get either a fixed random number
# Or one that will hopefully differ on multiple processors
seed = 347910

random.seed(seed)

print(random.rand())

