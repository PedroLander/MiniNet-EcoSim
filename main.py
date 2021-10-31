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

from Visualization import *
from Entities import *
import noise
import numpy as np

# Terrain Generation Properties
terrain_gen_properties = {
"shape" : (50,50),
"scale" : 100.0,
"octaves" : 6,
"persistence" : 0.5,
"lacunarity" : 2.0
}


def main(args):

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

        Entities.generate_entity_class(terrain_gen_properties, entities, 1,"sheep", 'o', "white", 10, 1)
        Entities.generate_entities(layer1, terrain_gen_properties, entities[1]["individuals"], 10)

        Entities.generate_entity_class(terrain_gen_properties, entities, 2,"wolves", '^', "black", 10, 1)
        Entities.generate_entities(layer1, terrain_gen_properties, entities[2]["individuals"], 5)

        Entities.generate_entity_class(terrain_gen_properties, entities, 3,"plant", 'o', "green", 10, .4)
        Entities.generate_entities(layer1, terrain_gen_properties, entities[3]["individuals"], 500)
        
        Visualization.plot_sim(X, Y, layer1, entities)

        return 0





























if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
