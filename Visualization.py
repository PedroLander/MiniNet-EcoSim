#  This code has been fetched from 
#
#  Jack McKew's Blog 
#    (https://jackmckew.dev/3d-terrain-in-python.html)
#  How to Build Software
#    https://www.howtobuildsoftware.com/index.php/how-do/VXR/matlab-matplotlib-plot-surface-display-the-maximum-surface-in-matplotlib


import noise
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Terrain Generation Properties
terrain_gen_properties = {
    "shape" : (5,5),
    "scale" : 100.0,
    "octaves" : 6,
    "persistence" : 0.5,
    "lacunarity" : 2.0
}

# Generate the surface
X = np.arange(0, terrain_gen_properties["shape"][0], 1)
Y = np.arange(0, terrain_gen_properties["shape"][1], 1)
X, Y = np.meshgrid(X, Y)

# Generate the layers
layer1 = np.zeros(terrain_gen_properties["shape"])
layer2 = np.zeros(terrain_gen_properties["shape"])

# Generate elevations
for i in range(terrain_gen_properties["shape"][0]):
    for j in range(terrain_gen_properties["shape"][1]):
        layer1[i][j] = noise.pnoise2(i/terrain_gen_properties["scale"], 
                                    j/terrain_gen_properties["scale"], 
                                    octaves=terrain_gen_properties["octaves"], 
                                    persistence=terrain_gen_properties["persistence"], 
                                    lacunarity=terrain_gen_properties["lacunarity"], 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=42)

        layer2[i][j] = noise.pnoise2(i/terrain_gen_properties["scale"], 
                                    j/terrain_gen_properties["scale"], 
                                    octaves=terrain_gen_properties["octaves"], 
                                    persistence=terrain_gen_properties["persistence"], 
                                    lacunarity=terrain_gen_properties["lacunarity"], 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=42)


for i in range(len(layer2)):
        for j in range(len(layer1[i])):
                layer2[i][j] +=.1

fig = plt.figure()
ax = fig.gca(projection='3d')


alpha = 0.25

surf1 = ax.plot_surface(X, Y, layer1, cstride=2, rstride=1, linewidth=0, antialiased=False, alpha=alpha)

surf2 = ax.plot_surface(X, Y, layer2, cstride=2, rstride=1, linewidth=0, antialiased=False, alpha=alpha)


plt.show()
