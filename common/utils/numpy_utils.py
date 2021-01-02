import numpy as np


def str_to_array(s: str, mapping: dict = None) -> np.ndarray:
    """
    Converts a string to a 2D numpy array, with the given mapping.
    The mapping defaults to '#': 1 and '.': 0.
    """
    if mapping is None:
        mapping = {'#': 1, '.': 0}
    return np.array([[mapping[c] for c in row] for row in s.split('\n')])


def print_array(arr: np.ndarray) -> None:
    """Pretty-prints a numpy array of booleans."""
    s = '\n'.join(
        ''.join('\u2593' if char else '\u2591' for char in row)
        for row in arr
    )
    print(s)
