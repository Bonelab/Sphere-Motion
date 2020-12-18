# Imports
import numpy as np
from scipy.special import lambertw

def sphere_under_advection(t, r_0, a):
    '''Compute the radius of a sphere under advection

    Parameters
    ----------
    t : float, np.array
        Time(s) for which to solve
    r_0 : float
        Initial radius of the sphere
    a : float
        Advection constant (positive = grow)
    '''
    # Compute r
    r = a*t + r_0
    
    # Check if disappear
    if np.abs(a) > np.finfo(float).eps:
        t_vanish = -r_0 / a
        if t_vanish > 0:
            r[t >= t_vanish] = 0.0
    
    return r

def sphere_under_mean_curvature(t, r_0, b):
    '''Compute the radius of a sphere under advection

    Parameters
    ----------
    t : float, np.array
        Time(s) for which to solve
    r_0 : float
        Initial radius of the sphere
    b : float
        Mean curvature constant (must be > 0)
    '''
    # Compute vanishing time
    t_vanish = np.Inf
    if np.abs(b) > np.finfo(float).eps:
        t_vanish = r_0**2/(2.0*b)

    # Split t by t_vanish to avoid sqrt(-1)
    t_pos = t[t<t_vanish]
    t_neg = t[t>=t_vanish]

    # Compute r
    r = np.concatenate([
        np.sqrt(r_0**2 - 2*b*t_pos),
        np.zeros_like(t_neg)
    ])

    return r

def sphere_vanish_time(r_0, a, b):
    '''Compute the vanishing time of a sphere under advection and mean curvature flow

    Parameters
    ----------
    r_0 : float
        Initial radius of the sphere
    a : float
        Advection constant (positive = grow)
    b : float
        Mean curvature constant (must be > 0)
    '''
    # Switch on infinity
    cond = a*r_0 < b
    
    t_vanish = np.Inf
    if cond:
        t_vanish = b/a**2 * np.log(b / (b - a *r_0)) - r_0/a
    
    return t_vanish

def sphere_under_advection_and_mean_curvature(t, r_0, a, b):
    '''Compute the vanishing time of a sphere under advection and mean curvature flow

    Parameters
    ----------
    t : float, np.array
        Time(s) for which to solve
    r_0 : float
        Initial radius of the sphere
    a : float
        Advection constant (positive = grow)
    b : float
        Mean curvature constant (must be > 0)
    '''

    # Run simpler methods if possible
    if b == 0:
        return sphere_under_advection(t, r_0, a)
    if a == 0:
        return sphere_under_mean_curvature(t, r_0, b)
    
    # Determine vanishing time
    t_vanish = sphere_vanish_time(r_0, a, b)
    
    # Select k branch of W_k
    k = -1 if a<0 else 0
    
    # Compute our values
    t_not_vanish = t[t<t_vanish]
    x = (a*r_0-b)/b
    z = x * np.exp(x) * np.exp(a**2*t_not_vanish/b)
    w_ = np.real(lambertw(z, k=k))
    r_not_vanish = (b/a) * (w_ + 1.0)
    
    # Combine with vanish
    r = np.concatenate([
        r_not_vanish,
        np.zeros_like(t[t>=t_vanish])
    ])
    
    return r