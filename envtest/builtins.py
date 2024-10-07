import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import pandas as pd


__all__ = ['rand_array', 'smooth_image', 'my_mat_solve','my_dataf']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()

def my_dataf(M):
    return pd.DataFrame(np.array(M))
