import numpy as np
import subprocess
import os
import matplotlib.pyplot as plt


# Utility for visualizing 3D Data using blender
def visualize3D(voxel_data, title='Voxel_Data', thresh=-1.0, percentile=0.8, plot=True):
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/' + title + '.png')
    if thresh < 0:
        ordered_data = voxel_data.copy().reshape(-1)
        ordered_data.sort()
        thresh = ordered_data[int(len(ordered_data)*percentile)]

    # Convert voxel data into string format
    voxel_string = ''
    for x in range(voxel_data.shape[0]):
        for y in range(voxel_data.shape[1]):
            for z in range(voxel_data.shape[2]):
                if voxel_data[x, y, z] > thresh:
                    voxel_string += '1'
                else:
                    voxel_string += '0'

    # Render image using blender
    blender_arguments = ['blender',
                         'stage.blend',
                         '-b',
                         '--python',
                         'blrender.py',
                         '--',
                         'blrender.py',
                         '--width', str(voxel_data.shape[0]),
                         '--height', str(voxel_data.shape[1]),
                         '--depth', str(voxel_data.shape[2]),
                         '--destfile', str(filename),
                         '--voxels', voxel_string]
    process = subprocess.Popen(blender_arguments)
    process.wait()

    if plot:
        img = plt.imread(filename)
        plt.imshow(img)

