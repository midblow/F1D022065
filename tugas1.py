from mpi4py import MPI
import os

comm = MPI.COMM_WORLD
home_dir = os.path.expanduser('~')

# Mengatur bilangan ganjil atau genap yang akan diproses oleh setiap proses
if comm.rank % 2 == 0:
    status = "Genap"
else:
    status = "Ganjil"

# Mencetak pesan sesuai dengan status bilangan
print(f"{comm.rank} --> Anda proses {status}: (%s)" % home_dir)
