'''
Multiprocessing implemntation of testing multiple 
Potential Energy Functions in the Schrodinger Equation.

Run with:

python schrodinger1D.py
   
'''

# Import the packages we need
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse import linalg as sla
import time

# Native python packages needed
from multiprocessing import Pool
import multiprocessing

# Everything same as before until main...

def schrodinger1D(Vfun):
    """
    Solves the 1 dimensional Schrodinger equation numerically
    
    ------ Inputs ------
    Vfun: function, potential energy function
    
    ------- Returns -------
    evl: np.array, eigenvalues
    evt: np.array, eigenvectors
    x: np.array, x axis values
        
    ------- Params to set -------
    xmin: minimum value of the x axis
    xmax: maximum value of the x axis
    Nx: number of finite elements in the x axis
    neigs: number of eigenvalues to find
    """
    
    xmin = -10
    xmax = 10
    Nx = 250
    neigs = 5

    # for this code we are using Dirichlet Boundary Conditions
    x = np.linspace(xmin, xmax, Nx)  # x axis grid
    dx = x[1] - x[0]  # x axis step size
    # Obtain the potential function values:
    V = Vfun(x)
    # create the Hamiltonian Operator matrix:
    H = sparse.eye(Nx, Nx, format = "lil") * 2
    for i in range(Nx - 1):
        H[i, i + 1] = -1
        H[i + 1, i] = -1
        
    H = H / (dx ** 2)
    # Add the potential into the Hamiltonian
    for i in range(Nx):
        H[i, i] = H[i, i] + V[i]
    # convert to csc matrix format
    H = H.tocsc()
    
    # obtain neigs solutions from the sparse matrix
    [evl, evt] = sla.eigs(H, k = neigs, which = "SM")
    for i in range(neigs):
        # normalize the eigen vectors
        evt[:, i] = evt[:, i] / np.sqrt(
                                np.trapz(np.conj(
                                evt[:, i]) * evt[:, i], x))
        # eigen values MUST be real:
        evl = np.real(evl)
    
    return evl, evt, x


def plot_H(H,neigs=5):
    evl = H[0] # energy eigen values
    indices = np.argsort(evl)

    print("Energy eigenvalues:")
    for i,j in enumerate(evl[indices]):
        print("{}: {:.2f}".format(i + 1, j))

    evt = H[1] # eigen vectors 
    x = H[2] # x dimensions 
    i = 0

    plt.figure(figsize = (4, 2))
    while i < neigs:
        n = indices[i]
        y = np.real(np.conj(evt[:, n]) * evt[:, n])  
        plt.subplot(neigs, 1, i+1)  
        plt.plot(x, y)
        plt.axis('off')
        i = i + 1  
    plt.show()
    

def Vfun1(x, params=[1]):
    '''
    Quantum harmonic oscillator potential energy function
    '''
    V = params[0] * x**2
    return V
    
    
def Vfun2(x, params = 1e10):
    '''
    Infinite well potential energy function
    '''
    V = x * 0
    V[:100]=params
    V[-100:]=params
    return V
   
    
def Vfun3(x, params = [-0.5, 0.01, 7]):
    '''
    Double well potential energy function
    '''
    A = params[0]
    B = params[1]
    C = params[2]
    V = A * x ** 2 + B * x ** 4 + C
    return V


# In its simplest form the multiprocessing method must be protected by the main function.
# This is because of the way it spawns additional Python instances to run. See the docs:
# https://docs.python.org/3/library/multiprocessing.html

if __name__ == "__main__":
    
    #print(len(os.sched_getaffinity(0)))
    print(multiprocessing.cpu_count())

    print("Running multiprocessing ...")
    
    ncpus=multiprocessing.cpu_count()
    print(ncpus, "cpus available for use")
    tic=time.time()
    with Pool(processes=ncpus) as pool: 
        y=pool.imap(schrodinger1D, [Vfun1,Vfun2,Vfun3])
        pool.close()
        pool.join()
        outputs = [result for result in y]
        
    print("Done multiprocessing in {:.4f} s".format(time.time()-tic))
    
#     print(outputs)
    plot_H(outputs[0])
    plot_H(outputs[1])
    plot_H(outputs[2])
