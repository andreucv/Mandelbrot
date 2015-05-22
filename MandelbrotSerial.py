from mpi4py import MPI
import numpy
from matplotlib import pyplot

x1, x2 = -2.0, 1.0 
y1, y2 = -1.0, 1.0 
w, h = 600, 400
maxit = 127

def mandelbrot(x, y, maxit):
    c = x + y*1j
    z = 0 + 0j
    it = 0
    while abs(z) < 2 and it < maxit:
        z = z**2 + c
        it += 1
    
    return it

# first row to compute here
start = 0
# array to store local result
C = numpy.zeros([h, w], dtype='i')
# compute owned rows
dx = (x2 - x1) / w
dy = (y2 - y1) / h
for i in range(h):
    y = y1 + (i + start) * dy
    for j in range(w):
        x = x1 + j * dx
        C[i, j] = mandelbrot(x, y, maxit)

pyplot.imsave("mandel.png", C, format="png")