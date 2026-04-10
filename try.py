import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
x3 = np.linspace(0, 50, 1000)


fig, ax = plt.subplots()
line, = ax.plot(x3, np.exp(-x3)*np.cos(x3))

def update(frame):
    line.set_ydata(np.exp(-x3)*np.cos(5*(x3 + frame)))
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 50))

plt.show()