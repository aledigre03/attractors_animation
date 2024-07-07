import matplotlib.pyplot as plt
import signal
import sys
import numpy as np
from matplotlib.animation import FuncAnimation

def Bouali(xyz=[1, 0.1, 0.1], a=0.3, s=1, time= 0.006):
    '''The routine makes three lists x,y,z in xyz. A new value will be added to the three column x,y,z every iteration'''
    x, y, z = [xyz[0]], [xyz[1]], [xyz[2]]
    for i in range(1, 40000):

        x0, y0, z0 = x[-1], y[-1], z[-1]

        x.append(x0 + time * (x0 * (4-y0)+a*z0))
        y.append(y0 + time * (-y0 * (1-np.power(x0, 2))))
        z.append(z0 + time * (-x0 * (1.5 - s * z0)- 0.05 * z0))

    return x,y,z

def init():
    '''This routine contains the line which represent the attractor. It is used by animation to start the attractor which will star at
       frame 0. Thus, with the initial conditions given before.'''
    return ln

def animate(i):
    ln.set_data([x_values[:i], y_values[:i]])
    ln.set_3d_properties(z_values[:i])
    return ln

def handle_close(sig, frame):
    print("Stopping animation...")
    animation.event_source.stop()
    plt.close(fig)
    sys.exit(0)

signal.signal(signal.SIGINT, handle_close)
#ctlr + C gracefully stops the animation if you load the program on your terminal

fig= plt.figure(facecolor="black")
ax= fig.add_subplot(projection='3d')
x_values, y_values, z_values= Bouali()
ln, = ax.plot(x_values, y_values, z_values)

animation = FuncAnimation(fig, animate, frames= len(x_values), init_func= init, interval= .01)

plt.show()