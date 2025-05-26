
import numpy as np

xa = np.zeros((3,3)).astype(int)
xa[:,1] = xa[1] = [1,0,1]
xb = np.zeros((3,3)).astype(int)
xb[0] = xb[2] = [1,0,1]
xc = np.zeros((3,3)).astype(int)
xc[1,1] = 1

def mk_mapping(x,e):
    nc = x.sum()
    nz = x.flatten.shape[0] - nc
    ne = e.sum()
    
