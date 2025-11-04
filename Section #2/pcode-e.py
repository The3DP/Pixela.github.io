##
# Matplotlib Animations
##

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2*np.pi, 200)
fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i / 10))
    return line,

ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
plt.show()
