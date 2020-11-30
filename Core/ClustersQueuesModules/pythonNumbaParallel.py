from numpy import arange
from numba import njit, prange
import numba


# This example is from 
# https://numba.readthedocs.io/en/stable/user/parallel.html#explicit-parallel-loops (30/11/2020)
@njit(parallel=True)
def prange_test(A):
    s = 0
    # Without "parallel=True" in the jit-decorator
    # the prange statement is equivalent to range
    for i in prange(A.shape[0]):
        s += A[i]
    return s

l = 20
arr = arange(l)+1
sm = prange_test(arr)

print("Code is running on {} threads".format(numba.config.NUMBA_NUM_THREADS))

#Check the answer
print("Sum of the numbers from 1 to {} should be {}".format(l, int(l*(l+1)/2)))
print("Parallel code obtained {}".format(sm))
