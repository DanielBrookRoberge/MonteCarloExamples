import random

import numpy as np

import const

class Particle(object):
    def __init__(self, beam):
        self.position = np.array(beam.generate_position())
        self.energy = beam.energy.generate()
        self.direction = np.array(beam.generate_direction())
        self.alive = True

    def propagate(self, detector):
        voxel = detector.voxel(self.position)
        self.position = self.position + self.direction * const.STEP_DISTANCE

        if random.random() < const.ABSORPTION_PROB:
            energy_deposit = self.energy
        elif random.random() < const.COLLISION_PROB:
            energy_deposit = min(self.energy, const.COLLISION_DEPOSIT)
        else:
            energy_deposit = min(self.energy, const.PROPAGATION_DEPOSIT)

        self.energy -= energy_deposit
        voxel.deposit(energy_deposit)
        if self.energy <= 0:
            self.alive = False
