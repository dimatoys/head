import numpy as np
# camera positions
camera = np.array([4134, 4008, 3900, 3795, 3685, 3500, 3450, 3300, 3210, 3110, 2950, 2800, 2594, 2519, 2411, 2342, 2134, 1989, 1905, 1708, 1649, 1485])

# position of DOF_G to grab
G = np.array([5000, 5000, 4900, 4800, 4700, 4600, 4300, 4000, 3700, 3500, 3000])

# position of DOF_A to grab
A = np.array([3505, 3372, 3372, 3372, 3372, 3400, 3450, 3600, 3730, 3800, 4100])

# distance of the object
D = np.array([150, 161, 170, 178, 190, 199, 211, 217, 227, 236, 242, 255, 263, 274, 283, 298, 316, 335, 349, 377, 388, 420])

print np.polyfit(camera[:len(G)], G, 2)
#>>> array([ -1.49456287e-03,   1.22899765e+01,  -2.02715561e+04])

print np.polyfit(camera[:len(A)],A,2)
#>>> array([  1.10394583e-03,  -8.32805109e+00,   1.90537250e+04])

print np.polyfit(camera,D,3)
#>>>  -1.57454850e-08   1.50684580e-04  -5.48962738e-01   9.54443852e+02
