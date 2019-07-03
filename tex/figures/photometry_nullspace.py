# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import starry


ydeg = 10
theta = np.linspace(-180, 180, 1000)
s = np.zeros(((ydeg + 1) ** 2, len(theta)))
map = starry.Map(ydeg, lazy=False)
n = 0
for l in range(ydeg + 1):
    for m in range(-l, l + 1):
        map.reset()
        if l > 0:
                map[l, m] = 1.0
        s[n] = map.flux(theta=theta)
        n += 1

# Set up the plot
fig, ax = plt.subplots(ydeg + 1, 2 * ydeg + 1, figsize=(16, 10), 
                       sharex=True, sharey=True)
fig.subplots_adjust(hspace=0)
for axis in ax.flatten():
    axis.spines['top'].set_visible(False)
    axis.spines['right'].set_visible(False)
    axis.spines['bottom'].set_visible(False)
    axis.spines['left'].set_visible(False)
    axis.set_xticks([])
    axis.set_yticks([])

# Loop over the orders and degrees
n = 0
for i, l in enumerate(range(ydeg + 1)):
    for j, m in enumerate(range(-l, l + 1)):
        j += ydeg - l
        ax[i, j].plot(s[n])
        n += 1

# Labels
for j, m in enumerate(range(-ydeg, ydeg + 1)):
    ax[-1, j].set_xlabel("%d" % m, fontsize=14, fontweight="bold", alpha=0.5)
for i, l in enumerate(range(ydeg + 1)):
    ax[i, ydeg - l].set_ylabel("%d" % l, fontsize=14, fontweight="bold",
                               rotation=45, labelpad=20, alpha=0.5)

# Save
fig.savefig("photometry_nullspace.pdf", bbox_inches="tight")