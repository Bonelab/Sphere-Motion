import numpy as np
import matplotlib.pyplot as plt
from model import sphere_under_advection

import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 2
font = {
    'size'   : 16
}

mpl.rc('font', **font)

a_range = [-2, -1, 0, +1, +2]
r_0 = 10.
n = 1000
t = np.linspace(0, 10., n)
colors = [str(x) for x in [0., 0.3, 0.5, 0.5, 0.7]]
print(colors)

for a,c  in zip(a_range, colors):
    print(a,c)
    r = sphere_under_advection(t, r_0, a)
    plt.plot(t, r, color=c)
plt.ylabel('Radius')
plt.xlabel('Time')
plt.legend(['a = {}'.format(a) for a in a_range])
plt.savefig(
    'advection.pdf',
    bbox_inches='tight',
    pad_inches=0.1,
)