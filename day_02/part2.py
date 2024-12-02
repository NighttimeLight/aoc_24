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

    arrs_d = np.array([np.delete(arr, dumped) for dumped in range(len(arr))])
    diffs_d = np.diff(arrs_d)
    diffs_d = np.stack((diffs_d, np.negative(diffs_d)))
    diffs_d = np.logical_and(diffs_d >= 1, diffs_d <= 3)
    diffs_d = np.all(diffs_d, axis=-1)
    diffs_d = np.any(diffs_d, axis=-1)
    diffs_d = np.any(diffs_d, axis=0)

    safes.append(diffs or diffs_d)

print(sum(safes))
