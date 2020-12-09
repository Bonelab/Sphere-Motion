import numpy as np
import matplotlib.pyplot as plt
from model import sphere_under_mean_curvature

import matplotlib as mpl
mpl.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
    'lines.linewidth': 2,
    'font.size': 24,
})

a = 1.
b = 10.
n = 1000
r1 = np.linspace(1., 20., 10)
dr1 = a - b / r1

r2 = r1 + 0.1*dr1
dr2 = a - b / r2

delta_r = r2 - r1
delta_dr = dr2 - dr1

m = np.sqrt(delta_r*delta_r + delta_dr*delta_dr)
x = delta_r / m
y = delta_dr / m

r = np.linspace(1., 20., n)
dr = a - b / r

plt.hlines([0], 0, max(r), colors='0.6', linestyles='dashed')
plt.vlines([b/a], -10., 2.5, colors='0.6', linestyles='dashed')
plt.plot(r, dr, 'k')
plt.quiver(r1, dr1, x, y)
plt.xlabel(r'$r$')
plt.ylabel(r'$\frac{dr}{dt}$')
plt.yticks([2.5, 0., -2.5, -5.0, -7.5, -10.0])
plt.xticks([0., 10., 20.])
plt.text(b/a-1.5, np.min(dr), r'$r=b/a$')
plt.savefig(
    'loss.pdf',
    bbox_inches='tight',
    pad_inches=0.1,
)
