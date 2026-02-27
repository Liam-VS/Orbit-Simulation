import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from body import Body

# Information is primarily obtained from https://science.nasa.gov/solar-system/planets/
#   Mass (kg) is measured in kilograms
#   Radius (m) is measured in metres
#   Velocity (m/s) is measured in metres per second

# ----- CONSTANTS -----
au = 1.496e11               # Astronomical Unit (distance from earth to sun)
g = 6.674e-11               # Gravitational Constant in SI units (m, kg, s)

# ----- DEFINING THE CELESITAL BODIES -----
sun = Body(
    name = "Sun",
    mass = 1.989e30,
    radius = 7e8,           # 700 million metres (700000km)
    pos = [0, 0],           # The Sun is the center of this simulation
    velocity = [0, 0],      # The Sun is stationary in this simulation
    color = 'yellow'
)

earth = Body(
    name = "Earth",
    mass = 5.972e24,
    radius = 6.378e6,       # 6.378 million metres (6378km)
    pos = [au, 0],          # Earths initial position will be 1AU to the right of the Sun
    velocity = [0, 29722],  # Earth orbits the sun at about 107000km/h which equates to 29780m/s
    color = 'green'
)

bodies = [sun, earth]

# ----- HELPER FUNCTIONS -----
# Computing the acceleration vector, to account for gravitation towards the Sun
def compute_acceleration(bodies):
    # Using pythagoras to compute the distance between centers
    dx_dist = bodies[0].pos[0]-bodies[1].pos[0]
    dy_dist = bodies[0].pos[1]-bodies[1].pos[1]
    distance = (np.sqrt((dx_dist**2)+(dy_dist**2)))

    # Computing the force between the entities using F = G*m1*m2/r^2 (Gravitational Force Formula)
    force = (g*bodies[0].mass*bodies[1].mass)/(distance**2)

    # Computing acceleration of earth using F = ma
    earth_acceleration = (force/bodies[1].mass)

    # Computing the direction vector of earth pointing towards the sun
    direction = (bodies[0].pos - bodies[1].pos) / distance # vector is calculated by finding the unit vector (e.g., [0,0] - [AU, 0] = [-AU, 0])
    
    # Computing the acceleration vector using the direction vector and acceleration
    acceleration_vector = earth_acceleration * direction

    return acceleration_vector


# ----- CREATING THE ANIMATION -----
# Create the figure
fig, axis = plt.subplots(figsize=(8, 8), facecolor='black') # Can change to 'dimgray' for visualization of axis
axis.set_facecolor('black')
axis.set_aspect('equal')

# Identify axis limit
limit = 2e11 # Big enough to fit earths orbit
axis.set_xlim(-limit, limit)
axis.set_ylim(-limit, limit)

# Plotting celestial objects (sizes of planets are unrealistic to ensure visibility)
sun_point, = axis.plot(sun.pos[0], sun.pos[1], 'o', color=sun.color, markersize=10)
earth_point, = axis.plot([earth.pos[0]], [earth.pos[1]], 'o', color=earth.color, markersize=1)

def update(frame):
    dt = 86400 # one day step size
    earth.velocity += compute_acceleration(bodies) * dt  # update velocity 
    earth.pos += earth.velocity * dt                     # update position
    print(earth.pos)

    earth_point.set_data([earth.pos[0]], [earth.pos[1]])
    return [earth_point]

stellar_animation = animation.FuncAnimation(fig=fig, func=update, frames=365, interval=30)
plt.show()
