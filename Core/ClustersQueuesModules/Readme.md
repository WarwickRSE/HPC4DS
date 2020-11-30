# The Codes
The codes here are simple examples of parallel programs.

The first one, pythonRandom.py simply picks a random number. It
attempts to get a different one each time it is run (which should work) and
on each processor (which might be unreliable - why?). Nothing about this
program is inherently parallel. 

The next one, pythonParallel.py, uses a silly trial-division algorithm to try and find prime numbers.
It uses Mpi4Py to parallelise, using a "worker-controller" model - one processor
is the controller which tells the others what to work on. The core functions are in the subdirectory
prime\_finder (if you're interested, this shows how to properly make your own module). By default it
searches between 10000 and 20000.

The last one, pythonNumbaParallel.py, sums the numbers in an array. We use the numbers from 1 to 
the variable 'l' - we know what this answer should be so we can check it. You will need Numba to run this,
and you might need to tell Numba how many threads to use, or it will try and use all your
processors.



# Some Examples 

We also include some examples of submission scripts and output files. Our local
cluster uses Slurm, which is quite common, and is what we demo here. 

The submission scripts might be usable for you, or you can use them as hints for
translating for your required queueing system. They are:
* sub.sbatch - Basic parallel script using 4 processors for 4 total tasks
* sub\_mpi.sbatch - Basic parallel script for an MPI job (start 4 copies of a program)
* sub\_num.sbatch - Basic parallel script for a 4-task Numba job (start one copy with access to 4 processors)


The example output files are:
* slurm-000001.out - An example of the output when a job fails due to a missing module
* slurm-000002.out - An example of the output from pythonRandom.py on 4 processors
* slurm-000003.out - An example of the output from pythonParallel.py on 4 processors
* slurm-000004.out - An example of the output from pythonNumbaParallel.py on 4 processors

