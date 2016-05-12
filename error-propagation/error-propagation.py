#!/usr/bin/env python3

import json
import numpy
import random

random.seed(54864218)

def f(a, b):
    coefficients = numpy.array([[2*a + b, a + b], [a - b, a - 2*b]])
    inv_coefficients = numpy.linalg.inv(coefficients)

    vars = numpy.array([2.5306, 10.1])

    elements = numpy.matmul(inv_coefficients, vars)

    return elements[0] / elements[1]

N = 100000

input_a_mean = 3
input_a_stdev = 2

input_b_mean = 6
input_b_stdev = 1

result_sample = []

for _ in range(N):
    a = random.gauss(input_a_mean, input_a_stdev)
    b = random.gauss(input_b_mean, input_b_stdev)

    result_sample.append(f(a, b))

result_mean = numpy.mean(result_sample)
result_stdev = numpy.std(result_sample)

print('Resulting value from %d samples: %f +- %f' % (N, result_mean, result_stdev))

with open('result-values.json', 'w') as outfile:
    outfile.write(json.dumps(result_sample))
