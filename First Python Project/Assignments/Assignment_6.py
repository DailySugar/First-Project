"""
Created November 11, 2021
Alex Sun
20289530
CISC-121

Plotting the Lotka-Volterra equations using matplotlib
"""

# Plotting template code borrowed from Assignment Page.
from matplotlib import pyplot as plt


sheep = 100
hyenas = 25
points_1 = []
points_2 = []

for i in range(10001):
    points_1.append(sheep)
    points_2.append(hyenas)
    # Scenario 1
    # delta_s = 0.005 * sheep - 0.0009 * sheep * hyenas
    # delta_h = 0.0005 * sheep * hyenas - 0.02 * hyenas
    # Scenario 2
    delta_s = 0.01 * sheep - 0.0001 * sheep * hyenas
    delta_h = 0.0002 * sheep * hyenas - 0.03 * hyenas
    sheep += delta_s
    hyenas += delta_h

fig = plt.figure(figsize=(20, 8))

fig.suptitle("Sheep and hyena populations")
plt.plot(points_1, label="sheep")
plt.plot(points_2, label="hyenas")

plt.legend()
plt.show()
