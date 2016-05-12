from math import *
import random

import const

class Profile(object):
    """
    An object encapsulating the spatial distribution of the particle origins.
    """
    def __init__(self, centre, diameter, shape):
        self.centre = centre
        self.diameter = diameter
        self.shape = shape

    def generate(self):
        """
        Generate an initial position in the XY plane based on the defined shape
        """
        # Generate a random polar angle
        theta = random.uniform(0, 2*pi)
        if self.shape == const.UNIFORM:
            # This generates a uniform distribution over the disc,
            # since there are fewer points at small radii
            r = self.diameter * sqrt(random.uniform(0, 1))
        elif self.shape == const.GAUSSIAN:
            r = self.diameter * sqrt(random.uniform(0, 1)) * random.gauss(0, 1)
        else:
            print('Unknown shape of beam')
            r = 0
        # convert from polar to rectangular
        return self.centre + r * cos(theta), r * sin(theta)

# Generate a random number from the given distribution.
energy_shapes = {
    const.UNIFORM: lambda mean, width: random.uniform(mean - width, mean + width),
    const.GAUSSIAN: random.gauss,
    const.LORENTZIAN: lambda location, scale: location + scale * tan(pi*random.uniform(-0.5, 0.5))
}

class Energy(object):
    def __init__(self, mean, width, shape):
        self.mean = mean
        self.width = width
        self.generator = energy_shapes.get(shape, None)
        if self.generator == None:
            raise ValueError('Invalid choice for energy shape')

    def generate(self):
        return self.generator(self.mean, self.width)


class Beam(object):
    def __init__(self, profile, energy, divergence=0):
        self.profile = profile
        self.energy = energy
        self.divergence = divergence * pi/180

    def generate_position(self):
        x, y = self.profile.generate()
        return x, y, 0.0

    def generate_direction(self):
        phi = random.uniform(0, 2*pi)
        theta = random.uniform(0, self.divergence)

        return sin(theta)*sin(phi), sin(theta)*cos(phi), cos(phi)
