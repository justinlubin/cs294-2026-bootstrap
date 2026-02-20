# %%

import random  # choices
import statistics  # quantiles, mean, median

import matplotlib.pyplot as plt

# %%

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
# https://numpy.org/doc/stable/reference/generated/numpy.percentile.html


def bootstrap(x, estimator, B):
    N = len(x)
    estimates = []
    for _ in range(0, B):
        new_sample = random.choices(x, k=N)
        estimate = estimator(new_sample)
        estimates.append(estimate)
    return estimates


a = [1, 1.5, 0.9, 0.6, 1.3, 1.4, 1.5]
b = [x - 0.8 for x in [2.1, 2.2, 2.1, 2, 1.7, 2.5, 2.5]]
diffs = [x - y for x, y in zip(a, b)]

fig, ax = plt.subplots(1, 1)
ax.hist(diffs)
fig.savefig("out1.png")

estimator = statistics.mean
point_estimate = estimator(diffs)
print("point estimate:", point_estimate)

estimates = bootstrap(diffs, estimator=estimator, B=10000)
print("some bootstrap estimates:", estimates[:10])

fig, ax = plt.subplots(1, 1)
ax.hist(estimates, color="0.5")
ax.axvline(point_estimate, color="red")
fig.savefig("out2.png")

quants = statistics.quantiles(estimates, n=200)
left = quants[5 - 1]  # 2.5 * 2, off by one
right = quants[195 - 1]  # 97.5 * 2, off by one
print("left endpoint:", left)
print("right endpoint:", right)
