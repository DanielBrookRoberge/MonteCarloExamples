from math import floor

class Voxel(object):
    def __init__(self):
        self.energy = 0
    def deposit(self, energy):
        self.energy += energy

class Detector(object):
    def __init__(self, voxels, size):
        self.size = size
        self.voxels = [Voxel() for _ in range(voxels**3)]
        self.voxel_length = size / voxels

    def index(self, xi, yi, zi):
        i = xi + self.size*yi + self.size**2*zi
        if i < 0:
            raise IndexError
        return i

    def voxel(self, position):
        x, y, z = position

        # Translate to the detector coordinates
        x += self.size / 2
        y += self.size / 2

        xi = int(floor(x / self.voxel_length))
        yi = int(floor(y / self.voxel_length))
        zi = int(floor(z / self.voxel_length))

        try:
            return self.voxels[self.index(xi, yi, zi)]
        except IndexError:
            return None

    def output(self):
        pass
