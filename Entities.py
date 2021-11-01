import random

class Entities():


        @staticmethod
        def generate_entity_class(entities_dict, class_attr, idnumber):
                global entities
                
                entities_dict[idnumber] = dict()
                for attr in class_attr.keys():
                        entities_dict[idnumber][attr] = class_attr[attr]
                entities_dict[idnumber]["individuals"] = dict()
                return entities_dict

        @staticmethod
        def generate_entities(surface, terrain_gen_properties, individuals_pool, n):

                for i in range(n):
                        new_entity = dict()
                        x = random.randint(0,terrain_gen_properties["shape"][0]-1)
                        y = random.randint(0,terrain_gen_properties["shape"][1]-1)
                        new_entity["coords"] = [x,
                                                y,
                                                surface[y][x]+.002] #entity laying on the surface
                        individuals_pool[random.randint(0,1000)] = new_entity
