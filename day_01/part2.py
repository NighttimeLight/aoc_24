import numpy as np

arr = np.loadtxt("input.txt", dtype=int)

# arrl, arrr = arr[:, 0].tolist(), arr[:, 1].tolist()
# sims = [num * arrr.count(num) for num in arrl]

values, counts = np.unique(arr[:, 1], return_counts=True)
count_dict = dict(zip(values, counts))
sims = [num * count_dict.get(num, 0) for num in arr[:, 0]]

print(sum(sims))
