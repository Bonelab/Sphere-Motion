import numpy as np
import matplotlib.pyplot as plt
from model import sphere_under_advection_and_mean_curvature

import matplotlib as mpl
mpl.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
    'lines.linewidth': 2,
    'font.size': 24,
})

# First
a = 1
b = 10
r_0 = 11.
n = 1000
t = np.linspace(0, 10., n)

r = sphere_under_advection_and_mean_curvature(t, r_0, a, b)
plt.figure()
plt.plot(t, r, 'k')
plt.ylabel('Radius')
plt.xlabel('Time')
plt.savefig(
    'solution_1.pdf',
    bbox_inches='tight',
    pad_inches=0.1,
)

# Second
a = 1
b = 10
r_0 = 9.
n = 1000
t = np.linspace(0, 10., n)

r = sphere_under_advection_and_mean_curvature(t, r_0, a, b)
plt.figure()
plt.plot(t, r, 'k')
plt.ylabel('Radius')
plt.xlabel('Time')
plt.savefig(
    'solution_2.pdf',
    bbox_inches='tight',
    pad_inches=0.1,
)

# Third
a = -1
b = 10
r_0 = 10.
n = 1000
t = np.linspace(0, 10., n)

r = sphere_under_advection_and_mean_curvature(t, r_0, a, b)
plt.figure()
plt.plot(t, r, 'k')
plt.ylabel('Radius')
plt.xlabel('Time')
plt.savefig(
    'solution_3.pdf',
    bbox_inches='tight',
    pad_inches=0.1,
)