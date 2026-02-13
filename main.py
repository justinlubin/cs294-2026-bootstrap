# %%

import random  # choices
import statistics  # quantiles, mean, median

import matplotlib.pyplot as plt

# %%

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
# https://numpy.org/doc/stable/reference/generated/numpy.percentile.html


def bootstrap(x, B, estimator):
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
ax.hist(a, alpha=0.5)
ax.hist(b, alpha=0.5)
fig.savefig("out1.png")

fig, ax = plt.subplots(1, 1)

estimator = statistics.mean
point_estimate = estimator(diffs)
print("point estimate:", point_estimate)

estimates = bootstrap(diffs, B=10000, estimator=estimator)
print("some bootstrap estimates", estimates[:10])
ax.hist(estimates, color="0.5")

ax.axvline(estimator(diffs), color="red")

percentiles = statistics.quantiles(estimates, n=200)
left = percentiles[5 - 1]  # 5/2 = 2.5
right = percentiles[195 - 1]  # 195/2 = 97.5
print("left endpoint:", left)
print("right endpoint:", right)

print("left distance:", point_estimate - left)
print("right distance:", right - point_estimate)

ax.axvline(left, color="orange")
ax.axvline(right, color="blue")

fig.savefig("out2.png")
