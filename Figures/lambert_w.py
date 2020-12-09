import numpy as np
from scipy.special import lambertw
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
    'lines.linewidth': 2,
    'font.size': 24,
})

n = 1000
z_0 = np.linspace(-1.0/np.e, 6, n)
z_1 = np.linspace(-1.0/np.e, 0.0, n)

w_0 = np.real(lambertw(z_0, k=0))
w_1 = np.real(lambertw(z_1, k=-1))

plt.plot(z_0, w_0, 'k')
plt.plot(z_1, w_1, '0.7')
plt.xlabel('z')
plt.ylabel('x')
plt.legend([r'$W_0$', r'$W_{-1}$'])
plt.savefig(
    'W.pdf',
    bbox_inches='tight',
    pad_inches=0.1,
)
