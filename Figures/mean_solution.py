import numpy as np
import matplotlib.pyplot as plt
from model import sphere_under_mean_curvature

import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 2
font = {
    'size'   : 16
}

mpl.rc('font', **font)

b_range = [1., 2.5, 5.0, 7.5, 10.]
r_0 = 10.
n = 1000
t = np.linspace(0, 10., n)
colors = [str(x) for x in [0., 0.3, 0.5, 0.5, 0.7]]
print(colors)

for b, c  in zip(b_range, colors):
    print(b,c)
    r = sphere_under_mean_curvature(t, r_0, b)
    plt.plot(t, r, color=c)
plt.ylabel('Radius')
plt.xlabel('Time')
plt.legend(['b = {}'.format(b) for b in b_range])
plt.savefig(
    'mean.pdf',
    bbox_inches='tight',
    pad_inches=0.1,
)
