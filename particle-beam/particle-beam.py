#!/usr/bin/env python3

import json
import random

import const
from particle import Particle
from detector import Detector
from initial import Beam, Profile, Energy

random.seed(91400)

N = 1000

# Define the beam parameters
beam = Beam(
    profile=Profile(
        centre=0,
        diameter=50,
        shape=const.UNIFORM,
    ),
    energy=Energy(
        mean=25,
        width=5,
        shape=const.GAUSSIAN
    ),
    divergence=30
)

# Define the detector
detector = Detector(
    voxels=5,
    size=100
)

for _ in range(N):
    particle = Particle(beam)
    # We keep tracking as long as we have energy left and the particle
    # is within the detector.
    while particle.energy > 0 and detector.voxel(particle.position):
        particle.propagate(detector)

result = detector.dump()

with open('energy-deposit.json', 'w') as outfile:
    outfile.write(json.dumps(result))
