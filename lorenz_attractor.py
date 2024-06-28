import matplotlib.pyplot as plt
import signal
import sys
from matplotlib.animation import FuncAnimation

def Lorenz(xyz=[0, 1, 0.5], s=10, r=28, b= 2.667, time= 0.01):
    '''The routine makes three lists x,y,z in xyz. A new value will be added to the three column x,y,z every iteration'''
    x, y, z = [xyz[0]], [xyz[1]], [xyz[2]]
    for i in range(1, 10000):

        x0, y0, z0 = x[-1], y[-1], z[-1]

        x.append(x0 + time * (s * (y0-x0)))
        y.append(y0 + time * (r * x0 - y0 -x0 * z0))
        z.append(z0 + time * (x0 * y0 - b*z0))

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
x_values, y_values, z_values= Lorenz()
ln = ax.plot(x_values, y_values, z_values)

animation = FuncAnimation(fig, animate, frames= len(x_values), init_func= init, interval= .01)

plt.show()
