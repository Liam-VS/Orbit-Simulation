import numpy as np

class Body:
    def __init__(self, name, radius, mass, pos, velocity, color= 'white'):
        # Constructors
        self.name = name
        self.mass = mass # in kilograms
        self.pos = np.array(pos, dtype= float)
        self.velocity = np.array(velocity, dtype= float)
        self.color = color

        # Going to need to store and calculate
        self.acceleration = np.array([0.0, 0.0])
        # Keeping track of the trails to make it more visually pleasing
        self.trail = []