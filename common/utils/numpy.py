import numpy as np


def str_to_array(s, mapping=None):
    """
    Converts a string to a 2D numpy array, with the given mapping.
    The mapping defaults to '#': 1 and '.': 0.
    """
    if mapping is None:
        mapping = {'#': 1, '.': 0}
    return np.array([[mapping[c] for c in row] for row in s.split('\n')])
