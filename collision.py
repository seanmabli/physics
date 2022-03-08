def twoobject(amass, a_velocity, bmass, b_velocity):
  final_b_velocity = (2 * (a_velocity * a_mass) + b_velocity * (b_mass - a_mass)) / (a_mass + b_mass)
  final_a_velocity = (b_velocity - a_velocity + final_b_velocity)
  return final_a_velocity, final_b_velocity

a_mass = 1 # kg
b_mass = 100 ** 2 # kg

a_velocity = 0 # m/sec
b_velocity = -1 # m/sec

collisions = 0
step = 0
num = 0

while a_velocity > b_velocity or step < 2:
  a_velocity, b_velocity = twoobject(a_mass, a_velocity, b_mass, b_velocity)

  if a_velocity < 0:
    a_velocity = abs(a_velocity)
    collisions += 1

  collisions += 1

print(collisions)