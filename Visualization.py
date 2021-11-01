#  This code has been fetched from 
#
#  Jack McKew's Blog 
#    (https://jackmckew.dev/3d-terrain-in-python.html)
#  How to Build Software
#    https://www.howtobuildsoftware.com/index.php/how-do/VXR/matlab-matplotlib-plot-surface-display-the-maximum-surface-in-matplotlib
#  Matplotlib documentation
#    https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Visualization():
        def plot_sim(X, Y, surface, entities):
                fig = plt.figure()
                ax = fig.add_subplot(projection='3d')
                ax.set(facecolor="grey")

                surf1 = ax.plot_surface(X, Y, surface, cstride=2, rstride=1, linewidth=0, antialiased=False, alpha=0.4)

                #  Plot the entities of each species
                #  Here we search the coordinates of each entity of each class
                for entity_class in entities.keys():
                        xs = [entities[entity_class]["individuals"][entity]["coords"][0] for entity in entities[entity_class]["individuals"].keys()]
                        ys = [entities[entity_class]["individuals"][entity]["coords"][1] for entity in entities[entity_class]["individuals"].keys()]
                        zs = [entities[entity_class]["individuals"][entity]["coords"][2] for entity in entities[entity_class]["individuals"].keys()]
                        ax.scatter(xs, ys, zs, marker=entities[entity_class]["symbol"], c=entities[entity_class]["colour"], s=int(entities[entity_class]["size"]), alpha=float(entities[entity_class]["alpha"]))
                plt.show()

