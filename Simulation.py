from Visualization import *

class Simulation():
        def move_entities( FrameNum, X, Y, surface, entities, fig):
                for entity_class in entities.keys():
                        for entity in entities[entity_class]["individuals"]:
                                
                                entities[entity_class]["individuals"][entity]["coords"][0] += 1
                                #agregar entities[entity_class]["individuals"][entity]["coords"][3] = "surface Z"
                Visualization.plot_sim(X, Y, surface, entities)
