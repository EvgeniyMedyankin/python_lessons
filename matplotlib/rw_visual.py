import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(1_000_000)
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9), dpi=52)
point_numbers = range(rw.num_points)
"""Отделить первую и последнюю точки"""
ax.scatter(0, 0, c='green', edgecolors='none', s=1000)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
plt.show()
