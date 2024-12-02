import numpy as np

file = open("input.txt", "r")
lines = file.read().splitlines()

safes = []
for line in lines:
    arr = np.fromstring(line, dtype=int, sep=' ')
    diffs = np.diff(arr)
    diffs = np.stack((diffs, np.negative(diffs)))
    diffs = np.logical_and(diffs >= 1, diffs <= 3)
    diffs = np.all(diffs, axis=-1)
    diffs = np.any(diffs, axis=0)
    safes.append(diffs)

print(sum(safes))
