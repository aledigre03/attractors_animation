import matplotlib.pyplot as plt
import signal
import sys
from matplotlib.animation import FuncAnimation

def Aizawa(xyz=[0.1, 0, 0], a=0.95, b=0.7, c= 0.6, d=3.5, e=0.25, f=0.1, time= 0.01):
    """the xyz array determines the inital points. With x[-1] we make sure that the function chooses the previous value during the iteration."""
    x, y, z = [xyz[0]], [xyz[1]], [xyz[2]]
    for i in range(1, 20000):
        x0, y0, z0 = x[-1], y[-1], z[-1]

        x.append(x0 + time * ((z0 - b) * x0 - d*y0))
        y.append(y0 + time * (d * x0 + (z0-b) * y0))
        z.append(z0 + time * (c + a*z0-((np.power(z0, 3))/3)- ((np.power(x0, 2))+(np.power(y0, 2))) * (1+ e *z0)+ f*z0*(np.power(x0, 3))))

    return x,y,z

def init():
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
x_values, y_values, z_values= Aizawa()
ln, = ax.plot(x_values, y_values, z_values)

#interval sets the speed of the animation
animation = FuncAnimation(fig, animate, frames= len(x_values), init_func= init, interval= .01)

plt.show()
