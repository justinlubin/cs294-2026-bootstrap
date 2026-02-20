import random
import statistics

import matplotlib.pyplot as plt

# For real analyses, just use SciPy's bootstrap!
#   https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
# It also gives you a 95% confidence interval.


def bootstrap(sample, estimator, B):
    N = len(sample)
    estimates = []

    for _ in range(B):
        new_sample = random.choices(sample, k=N)
        estimate = estimator(new_sample)
        estimates.append(estimate)

    return estimates


one_second = [
    0.78,
    1.3,
    1.31,
    1.16,
    0.96,
    0.63,
    0.76,
    1.33,
    0.86,
    1.03,
    0.85,
    1.11,
]

two_second = [
    2.15,
    2.04,
    1.93,
    1.97,
    1.96,
    2.35,
    2.08,
    2.38,
    1.71,
    2.23,
    2.11,
    1.6,
]

diffs = [x - y for x, y in zip(one_second, two_second)]

fig, ax = plt.subplots(1, 1)
ax.hist(diffs)
fig.savefig("empirical_distribution.png")

estimator = statistics.mean
point_estimate = estimator(diffs)
print("point estimate:", point_estimate)

estimates = bootstrap(diffs, estimator, B=10000)
print("some bootstrap estimate:", estimates[:10])

fig, ax = plt.subplots(1, 1)
ax.hist(estimates, color="0.5")
ax.axvline(point_estimate, color="red")
fig.savefig("sampling_distribution.png")
