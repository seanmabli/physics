# a solution to 3b1b collision pi video

import copy

for m in range(0, 20, 2):
  a_mass = 1 # kg
  b_mass = 10 ** m # kg
  
  initial_a_velocity = 0 # m/sec
  initial_b_velocity = -1 # m/sec
  
  collisions = 0
  step = 0
  
  while initial_a_velocity > initial_b_velocity or step < 2:
    final_b_velocity = (2 * (initial_a_velocity * a_mass) + initial_b_velocity * (b_mass - a_mass)) / (a_mass + b_mass)
    final_a_velocity = (initial_b_velocity - initial_a_velocity + final_b_velocity)
    
    initial_a_velocity = copy.copy(final_a_velocity)
    initial_b_velocity = copy.copy(final_b_velocity)
    
    if initial_a_velocity < 0:
      initial_a_velocity = abs(initial_a_velocity)
      collisions += 1

    # print(str(initial_a_velocity) + ' ' + str(initial_b_velocity))
    
    collisions += 1
    step += 1
  
  print(collisions)
