#!/usr/bin/env python3

import json
import random

import const
from const import MM, MEV
from particle import Particle
from detector import Detector
from initial import Beam, Profile, Energy

random.seed(91400)

N = 1000

# Define the beam parameters
beam = Beam(
    # Initial position is in a centered uniform disc with 50 mm diameter
    profile=Profile(
        centre=0,
        diameter=50*MM,
        shape=const.UNIFORM,
    ),
    # Energy has a Gaussian distribution with a mean of 25 MeV and a
    # standard deviation of 5 MeV
    energy=Energy(
        mean=25*MEV,
        width=5*MEV,
        shape=const.GAUSSIAN
    ),
    # Initial direction is in a cone between 0 and 30 degrees
    divergence=30
)

# Define the detector
detector = Detector(
    voxels=5,
    size=100*MM
)

for _ in range(N):
    # Generate a new particle from the beam
    particle = Particle(beam)
    # We keep tracking as long as we have energy left and the particle
    # is within the detector.
    while particle.energy > 0 and detector.voxel(particle.position):
        particle.propagate(detector)

result = detector.dump()

with open('energy-deposit.json', 'w') as outfile:
    outfile.write(json.dumps(result))
