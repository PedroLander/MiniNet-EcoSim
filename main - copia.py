#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2021 user1 <user1@STATION1>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import noise
import numpy as np
from csv import reader
import matplotlib.animation as animation
import matplotlib.pyplot as plt

from Visualization import *
from Entities import *
from Simulator import *

TWOPI = 2*np.pi

fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)
s = np.sin(t)
l = plt.plot(t, s)

ax = plt.axis([0,TWOPI,-1,1])

redDot, = plt.plot([0], [np.sin(0)], 'ro')


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

entities = dict()

# Read the file with the classes parameters
# skip first line i.e. read header first and then iterate over each row od csv as a list
with open('entity_classes.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    idc = 0

    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
                class_attr = {header[attr]:row[attr] for attr in range(len(header))}
                Entities.generate_entity_class(entities, class_attr, idc)
                Entities.generate_entities(layer1, terrain_gen_properties, entities[idc]["individuals"], int(entities[idc]["n_init"]))
                idc += 1
#closes the file
read_obj.close()

fig = Visualization.plot_sim(X, Y, layer1, entities)

def move_sim(i):
        pass



def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=10, \
                                      interval=10, blit=True, repeat=True)

plt.show()
