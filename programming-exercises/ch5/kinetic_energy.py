# Kinetic Energy
# In physics, an object that is in motion is said to have kinetic energy.
# The following formula can be used to determine a moving object's kinetic
# energy:   KE = 1/2 mv**2
# KE = Kinetic Energy
# m = object's mass (kg)
# v = velocity (m/s)
# Write a program that asks the user to enter values for mass and velocity
# and then calls kinetic_energy function to get obj KE

def main():

    mass = Mass()
    velocity = Velocity()
    kinetic_energy = KineticEnergy(mass, velocity)
    
    Results(mass, velocity, kinetic_energy)

def Mass():
    m = int(input('How much does the object weigh in kilograms? '))
    return m

def Velocity():
    v = int(input('What\'s the vehicle\'s velocity in meters/s? '))
    return v

def KineticEnergy(m, v):
    ke = (1/2) * m * (v**2)
    return ke

def Results(m, v, ke):
    print()
    print('================== Results ========================')
    print('Mass:', m, '\tVelocity:', v, '\tKinetic Energy:', ke)

main()
