import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=20, year=2020)
data = session.data.strip()
data = data.split('\n\n')

p1, p2 = 1, 0
dirs = ['U', 'L', 'D', 'R']

target = """
..................#.
#....##....##....###
.#..#..#..#..#..#...""".strip().split('\n')
target = np.array([[char == '#' for char in row] for row in target])


def getrot(s1, s2):
    """how many cc rotations to get from a to b"""
    return dirs.index(s2) - dirs.index(s1)


def cc(s):
    """direction counterclockwise adjacent to s"""
    return dirs[(dirs.index(s) + 1) % 4]


def getside(img, s):
    """"gets side k, always in clockwise order"""
    if s == 'U':
        return img.arr[0]
    elif s == 'D':
        return img.arr[-1][::-1]
    elif s == 'R':
        return img.arr[:, -1]
    elif s == 'L':
        return img.arr[:, 0][::-1]


class Image:
    def __init__(self, arr, id):
        self.arr = arr
        self.id = id
        self.imgdict = {'U': None, 'D': None, 'R': None, 'L': None}

    def set(self, self_side, other_side, other, flipped=False):
        self.imgdict[self_side] = (other_side, flipped, other)


# parse data
images = []
for i, line in enumerate(data):
    tile_id, *img = line.split('\n')
    img = np.array([[c == '#' for c in l] for l in img])
    images.append(Image(img, int(tile_id.split()[-1][:-1])))

# get connected images
for i, img1 in enumerate(images):
    for img2 in images[i + 1:]:
        for s1, s2 in product(('U', 'D', 'R', 'L'), repeat=2):
            img1_side = getside(img1, s1)
            img2_side = getside(img2, s2)
            if np.all(img1_side == img2_side):
                # flipped because both in clockwise order
                img1.set(s1, s2, img2, flipped=True)
                img2.set(s2, s1, img1, flipped=True)
            elif np.all(img1_side[::-1] == img2_side):
                img1.set(s1, s2, img2)
                img2.set(s2, s1, img1)
            else:
                continue
            break

# find corners (part 1)
topleft = None
pairs = [['L', 'U'], ['U', 'R'], ['R', 'D'], ['D', 'L']]
for img in images:
    for a, b in pairs:
        if img.imgdict[a] is None and img.imgdict[b] is None:
            if (a, b) == ('L', 'U'):
                topleft = img
            p1 *= img.id

for img in images:  # remove borders
    img.arr = img.arr[1:-1, 1:-1]

vert = horiz = topleft
vert_side, horiz_side = 'D', 'R'
vert_flip = horiz_flip = False

final_img = None
final_row = horiz.arr
# Stitch image together
while True:
    while horiz.imgdict[horiz_side]:  # go right in image
        cur_side, flip, other = horiz.imgdict[horiz_side]
        horiz_flip ^= flip
        rot = getrot(cur_side, 'L')
        other_arr = np.rot90(other.arr, rot)
        if horiz_flip:
            other_arr = np.flipud(other_arr)
        final_row = np.hstack([final_row, other_arr])
        horiz_side = cc(cc(cur_side))  # opposite side
        horiz = other

    if final_img is None:  # first iteration
        final_img = final_row
    else:
        final_img = np.vstack([final_img, final_row])

    if vert.imgdict[vert_side]:  # go down in image
        cur_side, flip, other = vert.imgdict[vert_side]
        vert_flip ^= flip
        rot = getrot(cur_side, 'U')
        other_arr = np.rot90(other.arr, rot)
        if vert_flip:
            other_arr = np.flipud(other_arr)
        vert = other
        final_row = other_arr
        vert_side = cc(cc(cur_side))  # opposite side
        horiz = vert
        horiz_side = cc(vert_side)
        if vert_flip:  # if flipped, then we're going the wrong way
            horiz_side = cc(cc(horiz_side))
        horiz_flip = vert_flip
    else:  # we're done
        break

# find orientation, get masked positions
tr, tc = target.shape
final_masked = np.zeros_like(final_img)
for _ in range(2):  # flips
    final_img = np.fliplr(final_img)
    for _ in range(4):  # rotations
        final_img = np.rot90(final_img)
        for r, c in np.ndindex(final_img.shape):
            subarr = final_img[r:r + tr, c:c + tc]
            if subarr.shape == target.shape and \
                    np.all(subarr & target == target):  # found match
                np.putmask(final_masked[r:r + tr, c:c + tc], target, 1)
        if np.sum(final_masked) > 0:
            break  # found right orientation
    else:
        continue
    break

p2 = np.sum(np.where(final_img, 1 - final_masked, 0))

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
