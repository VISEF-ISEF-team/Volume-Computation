import numpy as np
import _bitree_marching_cubes_cy
from stl import mesh
import time

# ========== EXAMPLE 1: CREATE A SPHERE AND MEASURE VOLUME ==========
x_dim = y_dim = z_dim = 100
x = np.linspace(-50, 50, x_dim)
y = np.linspace(-50, 50, y_dim)
z = np.linspace(-50, 50, z_dim)
x, y, z = np.meshgrid(x, y, z)

level = 35
volume = np.sqrt(x**2 + y**2 + z**2).astype(np.float64)
mask = np.asarray(volume >= level, dtype="bool").astype(int)
<<<<<<< HEAD
# cube = np.array([[[0.0] * (500 - 1) for _ in range(500 - 1)] for _ in range(500 - 1)]).astype(np.float64)  --> only for applied in software
=======
# cube = np.array([[[0.0] * (500 - 1) for _ in range(500 - 1)] for _ in range(500 - 1)]).astype(np.float32)  --> only for applied in software
>>>>>>> 615f458a3ee0d13f7e79dfa49325a2a60e2c5ea0

start_time = time.time()
verts, faces, fenwick, sum = _bitree_marching_cubes_cy.MarchingCubesLorensen(volume, mask, level)
end_time = time.time()

print(end_time - start_time)
print(fenwick.getSum(x_dim-1, y_dim-1, z_dim-1))
print(sum)

'''
If you want to reconstruct with STL for display purpose,
place this code below the line end_time = time.time()

verts = np.array(verts)
faces = np.array(faces)

obj_3d = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    obj_3d.vectors[i] = verts[f]
    
obj_3d.save('sphere.stl')
'''