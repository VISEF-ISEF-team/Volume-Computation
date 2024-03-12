import numpy as np
import time
import _bitree_marching_cubes_experiment_cy

configs = [50, 100, 250, 500]
radius = [[10, 15, 20, 25], [20, 25, 30, 35], [30, 35, 40, 45], [20, 30, 40, 45]]

for i in range(len(configs)):
    shape = configs[i]
    N = M = P = shape
    x = np.linspace(-shape/2, shape/2, N)
    y = np.linspace(-shape/2, shape/2, M)
    z = np.linspace(-shape/2, shape/2, P)
    x, y, z = np.meshgrid(x, y, z)
        
    for r in radius[i]:
        level = r
        volume = np.sqrt(x**2 + y**2 + z**2).astype(np.float64)
        mask = np.asarray(volume >= level, dtype="bool").astype(int)
        cube = np.array([[[0.0] * (P - 1) for _ in range(M - 1)] for _ in range(N - 1)]).astype(np.float64) 
        
        verts, faces, fenwick, cube_ = _bitree_marching_cubes_experiment_cy.MarchingCubesLorensen(volume, mask, cube, level)
        
        start_bit = time.time()
        print(fenwick.getSum(N-1, M-1, P-1))
        end_bit = time.time()
        
        start_bf = time.time()
        S = 0
        for x in range(N-1):
            for y in range(M-1):
                for z in range(P-1):
                    S += cube_[x,y,z]
        print(S)
        end_bf = time.time()
                
        print(f'BIT: {round(end_bit-start_bit,2)}, BF: {round(end_bf-start_bf,2)}')