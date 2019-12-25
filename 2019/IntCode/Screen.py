from collections import defaultdict

import numpy as np


class Screen:
    def __init__(self, *, default_factory=int):
        self.default_factory = default_factory
        self.states = defaultdict(default_factory)
        self.xrange, self.yrange = None, None

    def set_state(self, x, y, val):
        self.states[(x, y)] = val
        if not self.xrange:
            self.xrange = (x, x)
        else:
            self.xrange = (min(self.xrange[0], x), max(self.xrange[1], x))
        if not self.yrange:
            self.yrange = (y, y)
        else:
            self.yrange = (min(self.yrange[0], y), max(self.yrange[1], y))

    def __setitem__(self, key, value):
        assert (isinstance(key, tuple) or isinstance(key, np.ndarray)) and len(key) == 2
        self.set_state(*key, value)

    def __getitem__(self, item):
        return self.states[tuple(item)]

    def to_arr(self, *, highlight=None, highlightval=4):
        arr = np.full((self.yrange[1] - self.yrange[0] + 1, self.xrange[1] - self.xrange[0] + 1),
                      self.default_factory())
        for x, y in list(self.states.keys()):
            arr[y - self.yrange[0], x - self.xrange[0]] = self.states[x, y]
            if highlight is not None and (x, y) in highlight:
                arr[y - self.yrange[0], x - self.xrange[0]] = highlightval
        return arr

    def print(self, chars=" #", flip=False, no_char=False):
        state_coords = np.array(list(self.states.keys())).reshape((-1, 2))
        if isinstance(chars, str):
            if np.max(list(self.states.values())) >= len(chars):
                raise ValueError(
                    f"chars '{chars}' does not contain enough characters to print; "
                    f"expected length >= {np.max(self.states.values()) + 1}"
                )
        minx, maxx = self.xrange
        miny, maxy = self.yrange

        def getchar(ch):
            if no_char:
                return ch
            return chars[int(ch)]

        if flip:
            print('\n'.join(
                ' '.join(getchar((self.states[(x, y)])) for y in range(miny, maxy + 1)) for x in
                range(minx, maxx + 1)))
        else:
            print('\n'.join(
                ' '.join(getchar((self.states[(x, y)])) for x in range(minx, maxx + 1)) for y in
                range(miny, maxy + 1)))
