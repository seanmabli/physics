# a solution to 3b1b collision pi video
a_mass = 1 # kg
b_mass = 1 # kg

initial_a_velocity = 0
initial_b_velocity = -1

# initial_a_velocity + final_a_velocity = initial_b_velocity + final_b_velocity
# (initial_a_velocity * a_mass) + (initial_b_velocity * b_mass) = (final_a_velocity * a_mass) + (final_b_velocity * b_mass)

final_b_velocity = ((initial_a_velocity * a_mass) + (initial_b_velocity * b_mass) - (initial_b_velocity * a_mass) + (initial_a_velocity * a_mass)) / (a_mass + b_mass)
final_a_velocity = (initial_b_velocity - initial_a_velocity + final_b_velocity)
print(str(final_a_velocity) + ' ' + str(final_b_velocity))