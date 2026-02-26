import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from body import Body

# ----- DEFINING THE CELESITAL BODIES -----
# Information is primarily obtained from https://science.nasa.gov/solar-system/planets/
#   Mass is measured in kilograms
#   Radius is measured in kilometers
#   Velocity is measured in kilometers per hour

au = 3000 # Distance from earth to the sun. For the sake of visualization, this value will be reduced by a factor of 5000

sun = Body(
    name = "Sun",
    mass = 1.989e+30,
    radius = 100, # 700000km but exxagerated to 8e9
    pos = [0, 0], # The sun will be the center of this simulation, so it will not move
    velocity = [0, 0], 
    color = 'yellow'
)

earth = Body(
    name = "Earth",
    mass = 5.972e+24,
    radius = 10, # 6378km but exxagerated to 4e9
    pos = [au, 0],
    velocity = [0, 50], 
    color = 'green'
)

bodies = [sun, earth]

fig, axis = plt.subplots(figsize=(8, 8), facecolor='dimgray')
axis.set_facecolor('black')
axis.set_aspect('equal')

limit = 5000
axis.set_xlim(-limit, limit)
axis.set_ylim(-limit, limit)

# Plotting the sun as a fixed central point
sun_point, = axis.plot(sun.pos[0], sun.pos[1], 'o', color=sun.color, markersize=sun.radius)

# Plotting the earth as a moving point
earth_point, = axis.plot([earth.pos[0]], [earth.pos[1]], 'o', color=earth.color, markersize=earth.radius)

def update(frame):
    dt = 1 # step size
    earth.pos += earth.velocity * dt
    print(earth.pos)
    earth_point.set_data([earth.pos[0]][:frame], [earth.pos[1]][:frame])
    #earth_circle.center = (earth.pos[0], earth.pos[1])
    return [earth_point]

stellar_animation = animation.FuncAnimation(fig=fig, func=update, frames=3600, interval=30)
plt.show()
