#!/usr/bin/env python3

import random

MUON_LIFETIME_NS = 2196.98
DECAY_PROBABILITY_PER_NS = 1 / MUON_LIFETIME_NS

STEP_SIZE_NS = 50

N = 1000000

random.seed(3414901283)

lifetimes = []
for _ in range(N):
    age = 0
    while True:
        decay_prob = DECAY_PROBABILITY_PER_NS * STEP_SIZE_NS
        if random.uniform(0, 1) < decay_prob:
            break
        age += STEP_SIZE_NS
    lifetimes.append(age)

mean_lifetime = sum(lifetimes)/N

print('Mean lifetime (ns) calculated from %d simulated particles: %f' % (N, mean_lifetime))
