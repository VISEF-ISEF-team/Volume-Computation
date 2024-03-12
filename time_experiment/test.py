import numpy as np
import time
import _bitree_marching_cubes_experiment_cy


pixel_spacing = (0.0858)**(3)
shape = 500
N = M = P = shape 
x = np.linspace(-shape/2, shape/2, N)
y = np.linspace(-shape/2, shape/2, M)
z = np.linspace(-shape/2, shape/2, P)
x, y, z = np.meshgrid(x, y, z)
        
level = 45
volume = np.sqrt(x**2 + y**2 + z**2).astype(np.float64)
mask = np.asarray(volume >= level, dtype="bool").astype(int)
cube = np.array([[[0.0] * (P - 1) for _ in range(M - 1)] for _ in range(N - 1)]).astype(np.float64) 
        
verts, faces, fenwick, cube_ = _bitree_marching_cubes_experiment_cy.MarchingCubesLorensen(volume, mask, cube, level)
        
start_bit = time.time()
print(fenwick.getSum(N-1, M-1, P-1) * pixel_spacing)
end_bit = time.time()
        
start_bf = time.time()
S = 0
for x in range(N-1):
    for y in range(M-1):
        for z in range(P-1):
            S += cube_[x,y,z]
print(S * pixel_spacing)
end_bf = time.time()
                
print(4/3 * np.pi * (level**3) * pixel_spacing)
print(f'BIT: {end_bit-start_bit}, BF: {end_bf-start_bf}')