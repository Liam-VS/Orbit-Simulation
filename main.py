import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from body import Body

# ----- DEFINING THE CELESITAL BODIES -----
# Information is primarily obtained from https://science.nasa.gov/solar-system/planets/
#   Mass is measured in kilograms
#   Radius is measured in kilometers
#   Velocity is measured in kilometers per hour

AU = 1,496e+8 # Distance from earth to the sun

sun = Body(
    name = "Sun",
    mass = 1.989e+30,
    radius = 700000,
    pos = [0, 0],
    velocity = [0, 0], # The sun will be the center of this simulation, so it will not move
    color = 'yellow'
)

earth = Body(
    name = "Earth",
    mass = 5.972e+24,
    radius = 12756/2,
    pos = [AU, 0],
    velocity = [0, 107000], 
    color = 'green'
)

bodies = [sun, earth]

fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_facecolor('black')
ax.set_aspect('equal')

# Plotting the sun as a fixed central point
sun_point = ax.plot(sun.position[0], sun.position[1], 'o', color=sun.color, markersize=12)
# Plotting the sun as a moving point
earth_point = ax.plot(earth.position[0], earth.position[1], 'o', color=earth.color, markersize=1)

def update(frame):
    dt = 3600 # step size (3600 seconds)
    earth_position += earth.velocity * dt

    earth_point.set_data([earth.position[0], earth.position[1]])
    return [earth_point]

stellar_animation = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()
