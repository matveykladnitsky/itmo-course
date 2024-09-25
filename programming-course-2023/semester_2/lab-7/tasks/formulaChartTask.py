import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class ThreeDimensionalPlotter:
    def __init__(self, x_range=(-5 * np.pi, 5 * np.pi), num_points=1000):
        self.x_range = x_range
        self.num_points = num_points

    def run(self):
        x = np.linspace(self.x_range[0], self.x_range[1], self.num_points)
        y = np.cos(x)
        z = np.sin(x)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z)

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title('3D Plot of y=cos(x) and z=sin(x)')

        plt.show()
