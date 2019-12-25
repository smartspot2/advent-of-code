import numpy as np

with open("day8.in", "r") as f:
    img = np.array(list(map(int, list(f.read())))).reshape((-1, 6, 25))

minlayer = np.array([(layer == 0).sum() for layer in img]).argmin(0)
print((img[minlayer].flatten() == 1).sum() * (img[minlayer].flatten() == 2).sum())

cols = img.T
final = np.zeros((6, 25), dtype=int)
for r, row in enumerate(cols):
    for c, elem in enumerate(row):
        final[c, r] = elem[elem != 2][0]
print('\n'.join(''.join(['#' if a else ' ' for a in x]) for x in final))
