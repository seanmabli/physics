# a solution to 3b1b collision pi video

import copy
import matplotlib.pyplot as plt

colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]

for w in range(0, 3):
  a_mass = 1 # kg
  b_mass = 100 ** w # kg

  initial_a_velocity = 0 # m/sec
  initial_b_velocity = -1 # m/sec

  collisions = 0
  step = 0
  num = 0

  while initial_a_velocity > initial_b_velocity or step < 2:
    final_b_velocity = (2 * (initial_a_velocity * a_mass) + initial_b_velocity * (b_mass - a_mass)) / (a_mass + b_mass)
    final_a_velocity = (initial_b_velocity - initial_a_velocity + final_b_velocity)

    initial_a_velocity = copy.copy(final_a_velocity)
    initial_b_velocity = copy.copy(final_b_velocity)

    if initial_a_velocity < 0:
      initial_a_velocity = abs(initial_a_velocity)
      collisions += 1

      num += 1
      plt.scatter(num, initial_b_velocity, color=colors[w], s=1)

    num += 1
    plt.scatter(num, initial_b_velocity, color=colors[w], s=1)

    collisions += 1
    step += 1

  plt.show()