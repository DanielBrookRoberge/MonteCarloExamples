from math import floor

import numpy as np

class Voxel(object):
    """
    Represents a single voxel of the detector.

    For simplicity, only accumulates energy.
    """
    def __init__(self):
        self.energy = 0
    def deposit(self, energy):
        self.energy += energy

class Detector(object):
    """
    An idealized detector broken evenly into voxels.
    """
    def __init__(self, voxels, size):
        self.size = size
        self.voxels = [Voxel() for _ in range(voxels**3)]
        self.voxel_length = size / voxels
        self.voxels_per_side = voxels

        self.offset = np.array([self.size / 2, self.size / 2, 0])

    def index(self, xi, yi, zi):
        """
        Converts 3D indices of a voxel into linear indexing.
        """
        i = xi + self.voxels_per_side*yi + self.voxels_per_side**2*zi
        if i < 0:
            raise IndexError
        return int(i)

    def voxel(self, position):
        """
        Retrieves the Voxel object corresponding to the given position.
        """

        # Translate to the detector coordinates
        position = position + self.offset
        # Scale to units of voxel lengths
        position /= self.voxel_length

        # Retrieve the 3D indices of the target voxel
        position = np.floor(position)
        xi, yi, zi = position

        try:
            return self.voxels[self.index(xi, yi, zi)]
        except IndexError:
            return None

    def dump(self):
        """
        Return a JSON-able representation of the energy deposits.
        """
        result = []
        for xi in range(0, self.voxels_per_side):
            for yi in range(0, self.voxels_per_side):
                for zi in range(0, self.voxels_per_side):
                    result.append(dict(
                        x=xi,
                        y=yi,
                        z=zi,
                        energy=self.voxels[self.index(xi, yi, zi)].energy
                    ))
        return result
