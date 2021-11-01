import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Simulator:
    def __init__(self, timesteps = 1000, ):
        self.simulation_time = np.linspace(0, timesteps, 10*(timesteps)+1)
        self._theta = np.sin(self.simulation_time) # I've changed this so one could see the plot being drawn

    def init_plot(self):
        self._p1, = self.axes.plot(self.simulation_time[0], self._theta[0])
        return self.fig,

    def update_plot(self, i):
        self._p1.set_data(self.simulation_time[:i], self._theta[:i])
        self.axes.set_xlim(right=self.simulation_time[i])
        return self._p1,

    def start_simulation(self):
        self.fig, self.axes = plt.subplots()
        self.ani = FuncAnimation(fig=self.fig, func=self.update_plot, init_func=self.init_plot,
                          interval=5, blit=True)

