from body import Body

'''
The orbits and orbital velocities of the planets are not fixed constants, but rather vary based on position in orbit.
Currently, this simulation does not take this into account and therefore we take in the following assumptions:
1. Each planet has a circular orbit around the Sun
2. Each planet has a constant orbital velocity (infered by assumption 1)
'''

au = 1.496e11               # Astronomical Unit (distance from earth to sun)

sun = Body(
    name = "Sun",
    mass = 1.989e30,
    radius = 7e8,           # 700 million metres (700000km)
    pos = [0, 0],           # The Sun is the center of this simulation
    velocity = [0, 0],      # The Sun is stationary in this simulation
    size = 50,
    color = 'yellow'
)

mercury = Body(
    name = "Mercury",
    mass = 3.285e23,
    radius = 2.440e6,       # 2.440 million metres (2440km)
    pos = [0.39*au, 0],
    velocity = [0, 47900],  # Mercury orbits the sun at an approximate average velocity of 47900m/s
    size = 2,
    color = 'gray'
)

venus = Body(
    name = "Venus",
    mass = 4.867e24,
    radius = 6.052e6,       # 6.052 million metres (6052km)
    pos = [0.72*au, 0],
    velocity = [0,35020],   # Venus orbits the sun at an approxmiate average velocity of 35020m/s
    size = 6,
    color = 'orange'
)

earth = Body(
    name = "Earth",
    mass = 5.972e24,
    radius = 6.378e6,       # 6.378 million metres (6378km)
    pos = [au, 0],          # Earths initial position will be 1AU to the right of the Sun
    velocity = [0, 29722],  # Earth orbits the sun at an approximate average of 107000km/h which equates to 29780m/s
    size = 6,
    color = 'green'
)

planets = [mercury, venus, earth]