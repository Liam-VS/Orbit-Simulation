import numpy as np
from body import Body

g = 6.674e-11      # Gravitational Constant

def calculate_acceleration(planet, sun):
    # Using pythagoras to compute the distance between centers
    dx_dist = sun.pos[0] - planet.pos[0]
    dy_dist = sun.pos[1] - planet.pos[1]
    distance = (np.sqrt((dx_dist**2) + (dy_dist**2)))

    # Computing the force between the entities using F = G*m1*m2/r^2 (Gravitational Force Formula)
    force = (g*sun.mass * planet.mass) / (distance**2)

    # Computing acceleration of the planet using F = ma => a = F/m
    earth_acceleration = (force / planet.mass)

    # Computing the direction vector of the planet pointing towards the sun
    direction = (sun.pos - planet.pos) / distance # e.g., unit vector = [0,0] - [AU, 0] = [-AU, 0]
    
    # Computing the acceleration vector using the direction vector and acceleration
    acceleration_vector = earth_acceleration * direction

    return acceleration_vector