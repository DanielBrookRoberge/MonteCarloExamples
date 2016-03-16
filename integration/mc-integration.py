#!/usr/bin/env python3
# Usage: mc-integration.py N seed
# N is the number of random points to draw
# Seed is used in the Python RNG to ensure repeatability of results

import random
import sys

# INITIALIZATION-----------------
try:
    N = int(sys.argv[1])
except IndexError:
    N = 100

try:
    seed = int(sys.argv[2])
except IndexError:
    seed = 12345

random.seed(seed)

aboveCount = 0
belowCount = 0

# DRAWING-----------------------
def f(x):
    return 1 - x*x

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(0, 1)
    if y > f(x):
        aboveCount += 1
    else:
        belowCount += 1

# CALCULATION-------------------
totalArea = 2
areaUnder = totalArea * belowCount / N

print('Estimate to the integral from %d points: %f' % (N, areaUnder))
