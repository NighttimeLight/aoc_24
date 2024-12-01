import numpy as np

arr = np.loadtxt("input.txt", dtype=int)

arrs = np.sort(arr, axis=0)
diffs = abs(arrs[:, 0] - arrs[:, 1])

print(sum(diffs))
