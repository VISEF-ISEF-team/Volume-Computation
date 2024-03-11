import SimpleITK as sitk
import numpy as np
from stl import mesh
import _bitree_marching_cubes_cy
import time

# Load volumetric data
path = "D:\Documents\GitHub\VascuIAR\DeepLearning\data\VnRawData\VHSCDD_sep_labels\VHSCDD_020_label\ct_020_label_10.nii.gz"  # Paste your path to .nii.gz or .nii file
raw = sitk.ReadImage(path, sitk.sitkFloat64)
volume = sitk.GetArrayFromImage(raw)

# Or if you have the volumetric data (3D array), skip previous step 
level = 0.5
mask = np.asarray(volume >= level, dtype="bool").astype(int)
# cube = np.array([[[0.0] * (volume.shape[2] - 1) for _ in range(volume.shape[1] - 1)] for _ in range(volume.shape[0] - 1)]).astype(np.float32) --> only for applied in software

start_time = time.time()
verts, faces, fenwick, sum = _bitree_marching_cubes_cy.MarchingCubesLorensen(volume, mask, level)
end_time = time.time()

print(end_time - start_time)
print(fenwick.getSum(volume.shape[0] - 1, volume.shape[1] - 1, volume.shape[2] - 1))
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