from sys import argv
from math import sqrt, trunc
from numpy import zeros, sum, ndarray
import time

from numba import jit, float32, boolean, int32, float64, int64

compile_start = time.time()

@jit([boolean()])
def check_prime(num):
  has_divisor = False

  if(num ==2):
    return True
  #Check 2 specially
  if num%2 == 0:
  # Don't need to check any further - return right now
    return False
  for i in range(3, trunc(sqrt(num))+1, 2):
    if num%i == 0:
      has_divisor = True
      # Don't need to check any further - at least one divisor exists
      break
  #Either we found a divisor, or there are none
  return not has_divisor

compile_end = time.time()
print("Compilation of check_prime took {} seconds".format(compile_end-compile_start))

def check_prime_nj(num):
  has_divisor = False

  if(num ==2):
    return True
  #Check 2 specially
  if num%2 == 0:
  # Don't need to check any further - return right now
    return False
  for i in range(3, trunc(sqrt(num))+1, 2):
    if num%i == 0:
      has_divisor = True
      # Don't need to check any further - at least one divisor exists
      break
  #Either we found a divisor, or there are none
  return not has_divisor


compile_start = time.time()

@jit((int64, int64, float64))
def main_loop(lower, length, flags):
  for i in range(1, length):
    flags[i] = check_prime(lower+i)

compile_end = time.time()
print("Compilation of main_loop took {} seconds".format(compile_end-compile_start))

def main_loop_nj(lower, length, flags):
  for i in range(1, length):
    flags[i] = check_prime_nj(lower+i)


def main(lower, upper, do_jit=True):

  length = upper - lower
  flags = zeros(length)
  start_time = time.time()
  if(do_jit):
    main_loop(lower, length, flags)
  else:
    main_loop_nj(lower, length, flags)
  end_time = time.time()
  print("Found ", int(sum(flags)), " primes in", end_time-start_time, ' s')

if __name__ == "__main__":

  try:
    lower = int(input('Enter lower bnd: '))
  except:
    print("I didn't understand. I'll try 100000")
    lower = 100000
  try:
    upper = int(input('Enter upper bnd: '))
  except:
    print("I didn't understand. I'll try 200000")
    upper = 200000

  main(lower, upper)

