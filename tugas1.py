from mpi4py import MPI
from math import ceil

comm = MPI.COMM_WORLD
proses_rank = comm.Get_rank()

if proses_rank % 2 == 0:
    print("Anda proses Genap")
else:
    print("Anda proses Ganjil")
