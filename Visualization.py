#  This code has been fetched from 
#
#  Jack McKew's Blog 
#    (https://jackmckew.dev/3d-terrain-in-python.html)
#  How to Build Software
#    https://www.howtobuildsoftware.com/index.php/how-do/VXR/matlab-matplotlib-plot-surface-display-the-maximum-surface-in-matplotlib
#  Matplotlib documentation
#    https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html

import noise
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random

# Terrain Generation Properties
terrain_gen_properties = {
    "shape" : (50,50),
    "scale" : 100.0,
    "octaves" : 6,
    "persistence" : 0.5,
    "lacunarity" : 2.0
}

# Generate the coordinates
X = np.arange(0, terrain_gen_properties["shape"][0], 1)
Y = np.arange(0, terrain_gen_properties["shape"][1], 1)
X, Y = np.meshgrid(X, Y)

# Generate the layers
layer1 = np.zeros(terrain_gen_properties["shape"])

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

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


alpha = 0.25

surf1 = ax.plot_surface(X, Y, layer1, cstride=2, rstride=1, linewidth=0, antialiased=False, alpha=alpha)

entities = dict()

def generate_entities():
        for i in range(10):
                new_entity = dict()
                x = random.randint(0,terrain_gen_properties["shape"][0]-1)
                y = random.randint(0,terrain_gen_properties["shape"][1]-1)
                new_entity["coords"] = [x,
                                        y,
                                        layer1[y][x]] #entity laying on the surface
                print (x, y)
                print (layer1[x-1][y-1])
                new_entity["species"] = "o"
                entities[random.randint(0,1000)] = new_entity
generate_entities()


# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

#sheep
xs = [entities[entity]["coords"][0] for entity in entities.keys()]
ys = [entities[entity]["coords"][1] for entity in entities.keys()]
zs = [entities[entity]["coords"][2] for entity in entities.keys()]
ax.scatter(xs, ys, zs, marker='o', c="brown")


plt.show()
