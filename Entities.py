import random

class Entities():


        @staticmethod
        def generate_entity_class(surface, entities_dict, idnumber, species_name, symbol, colour, size, alpha):
                global entities
                
                entities_dict[idnumber] = dict()
                entities_dict[idnumber]["species_name"] = species_name
                entities_dict[idnumber]["symbol"] = symbol
                entities_dict[idnumber]["colour"] = colour
                entities_dict[idnumber]["size"] = size
                entities_dict[idnumber]["alpha"] = alpha
                entities_dict[idnumber]["individuals"] = dict()

        @staticmethod
        def generate_entities(surface, terrain_gen_properties, individuals_pool, n):
                for i in range(n):
                        new_entity = dict()
                        x = random.randint(0,terrain_gen_properties["shape"][0]-1)
                        y = random.randint(0,terrain_gen_properties["shape"][1]-1)
                        new_entity["coords"] = [x,
                                                y,
                                                surface[y][x]+.005] #entity laying on the surface
                        individuals_pool[random.randint(0,1000)] = new_entity
