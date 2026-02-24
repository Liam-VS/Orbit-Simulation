import numpy as np

G = 6.674e-11 # Gravitational Constant

class Simulation:
    def __init__(self, bodies):
        self.bodies = bodies

    def compute_accelerations(self):
        # Reset accelerations
        for body in self.bodies:
            body.acceleration = np.array([0.0, 0.0])
        

