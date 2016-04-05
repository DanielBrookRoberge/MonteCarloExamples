#!/usr/bin/env python3

import random

import const
from particle import Particle
from detector import Detector
from initial import Beam, Profile, Energy

random.seed(91400)

N = 100000

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

detector = Detector(
    voxels=5,
    size=100
)

for _ in range(N):
    particle = Particle(beam)
    while particle.energy > 0 and detector.voxel(particle.position):
        particle.propagate(detector)

detector.output()
