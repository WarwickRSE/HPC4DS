#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4571
#SBATCH --time=00:01:00

module load GCC/8.3.0  OpenMPI/3.1.4
module load Python/3.7.4


export NUMBA_NUM_THREADS=4
srun python3 pythonNumbaParallel.py
